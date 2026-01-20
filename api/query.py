"""
AI Assistant Query API Endpoint

This serverless function handles queries to the AI assistant.
It performs semantic search using Pinecone and generates responses using OpenAI.

Deploy to: Vercel, Netlify, or AWS Lambda

Environment Variables Required:
    - OPENAI_API_KEY
    - PINECONE_API_KEY
    - PINECONE_ENVIRONMENT
    - PINECONE_INDEX_NAME (default: 'academic-website')
"""

import os
import json
from http.server import BaseHTTPRequestHandler

try:
    from openai import OpenAI
    import pinecone
except ImportError:
    # Dependencies will be installed during deployment
    pass


# System prompt for the AI assistant
SYSTEM_PROMPT = """You are an AI assistant for Ivan Dedyukhin's academic website.

Your role:
- Answer questions about Ivan's research, publications, CV, teaching, and academic profile
- Provide accurate information ONLY from the provided context
- If information is not in the context, say "I don't have that information in Ivan's website content."
- Cite sources (file names) when answering
- Be concise, professional, and helpful

Guidelines:
- Do NOT make up information or speculate beyond the provided context
- Do NOT answer questions unrelated to Ivan's academic profile
- If asked about topics outside the website scope, politely redirect to relevant content or say you cannot help
- Always maintain a professional, academic tone
- When citing sources, use the format: (Source: filename)

Context format:
Each piece of context includes a [Source: filename] tag. Reference these in your answers when appropriate.
"""


class AcademicAssistant:
    """Handles querying the academic website assistant"""

    def __init__(self):
        """Initialize OpenAI and Pinecone clients"""
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment=os.getenv("PINECONE_ENVIRONMENT", "us-west1-gcp")
        )

        index_name = os.getenv("PINECONE_INDEX_NAME", "academic-website")
        self.index = pinecone.Index(index_name)

    def create_embedding(self, text: str):
        """Generate embedding for query"""
        try:
            response = self.openai_client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error creating embedding: {e}")
            return None

    def semantic_search(self, query: str, top_k: int = 5):
        """Perform semantic search using Pinecone"""
        # Generate query embedding
        query_embedding = self.create_embedding(query)
        if query_embedding is None:
            return []

        # Search Pinecone
        try:
            results = self.index.query(
                vector=query_embedding,
                top_k=top_k,
                include_metadata=True
            )
            return results.matches
        except Exception as e:
            print(f"Error querying Pinecone: {e}")
            return []

    def build_context(self, search_results) -> str:
        """Build context string from search results"""
        if not search_results:
            return ""

        context_parts = []
        for match in search_results:
            source = match.metadata.get('source_file', 'Unknown')
            text = match.metadata.get('text', '')
            content_type = match.metadata.get('content_type', '')

            context_parts.append(
                f"[Source: {source}] [Type: {content_type}]\n{text}"
            )

        return "\n\n---\n\n".join(context_parts)

    def generate_response(self, query: str, context: str) -> dict:
        """Generate response using OpenAI with RAG"""
        if not context:
            return {
                "answer": "I apologize, but I couldn't find relevant information in Ivan's website content to answer your question. Please try rephrasing or ask about Ivan's research, publications, CV, or teaching.",
                "sources": []
            }

        # Build user prompt
        user_prompt = f"""Context from Ivan's website:

{context}

Question: {query}

Instructions:
- Answer based ONLY on the context above
- Cite sources using the format: (Source: filename)
- If the answer is not in the context, say so
- Be concise and professional
"""

        try:
            # Call OpenAI API
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,  # Lower temperature for more factual responses
                max_tokens=500
            )

            answer = response.choices[0].message.content

            # Extract sources from context
            sources = list(set([
                match.metadata.get('source_file', 'Unknown')
                for match in context
            ])) if isinstance(context, list) else []

            return {
                "answer": answer,
                "sources": sources
            }

        except Exception as e:
            print(f"Error generating response: {e}")
            return {
                "answer": "I apologize, but I encountered an error processing your question. Please try again.",
                "sources": []
            }

    def query(self, question: str) -> dict:
        """Main query method"""
        # Perform semantic search
        search_results = self.semantic_search(question, top_k=5)

        # Build context
        context = self.build_context(search_results)

        # Extract sources
        sources = list(set([
            match.metadata.get('source_file', 'Unknown')
            for match in search_results
        ]))

        # Generate response
        result = self.generate_response(question, context)
        result['sources'] = sources

        return result


# Serverless function handler (Vercel/Netlify compatible)
class handler(BaseHTTPRequestHandler):
    """HTTP handler for serverless deployment"""

    def _set_cors_headers(self):
        """Set CORS headers for cross-origin requests"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        """Handle preflight CORS requests"""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def do_POST(self):
        """Handle POST requests"""
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            # Validate request
            if 'question' not in data:
                self.send_response(400)
                self._set_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': 'Missing "question" field in request body'
                }).encode())
                return

            question = data['question'].strip()

            # Basic validation
            if not question or len(question) > 500:
                self.send_response(400)
                self._set_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': 'Question must be between 1 and 500 characters'
                }).encode())
                return

            # Query assistant
            assistant = AcademicAssistant()
            result = assistant.query(question)

            # Send response
            self.send_response(200)
            self._set_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())

        except Exception as e:
            print(f"Error handling request: {e}")
            self.send_response(500)
            self._set_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': 'Internal server error'
            }).encode())


# Alternative: Simple function for AWS Lambda
def lambda_handler(event, context):
    """AWS Lambda handler"""
    try:
        body = json.loads(event.get('body', '{}'))
        question = body.get('question', '').strip()

        if not question:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': 'Missing question'})
            }

        assistant = AcademicAssistant()
        result = assistant.query(question)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }
