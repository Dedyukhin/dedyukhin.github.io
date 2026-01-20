#!/usr/bin/env python3
"""
Content Indexing Script for Academic Website AI Assistant

This script:
1. Extracts text from markdown files and PDFs
2. Chunks the content into manageable pieces
3. Generates embeddings using OpenAI's API
4. Stores vectors in Pinecone for semantic search

Usage:
    python scripts/index_content.py

Environment Variables Required:
    - OPENAI_API_KEY: Your OpenAI API key
    - PINECONE_API_KEY: Your Pinecone API key
    - PINECONE_ENVIRONMENT: Your Pinecone environment (e.g., 'us-west1-gcp')
    - PINECONE_INDEX_NAME: Name of your Pinecone index (default: 'academic-website')
"""

import os
import sys
import hashlib
import re
from pathlib import Path
from typing import List, Dict, Tuple
import markdown
from datetime import datetime

try:
    from openai import OpenAI
    import pinecone
    from pypdf import PdfReader
except ImportError:
    print("Error: Required packages not installed.")
    print("Please install: pip install openai pinecone-client pypdf python-markdown")
    sys.exit(1)


class ContentIndexer:
    """Indexes academic website content for AI assistant"""

    # Files to index
    MARKDOWN_FILES = [
        "README.md",
        "Research.md",
        "Teaching.md",
        "CV.md",
    ]

    PDF_FILES = [
        "files/Academic_CV.pdf",
        "files/Syllabus SP24-B251-9998.pdf",
        "files/Nursing_Homes_WP_Aug2024.pdf",
        "files/COMP_2024_pres.pdf",
    ]

    # Chunking parameters
    CHUNK_SIZE = 600  # tokens (approx 450 words)
    CHUNK_OVERLAP = 75  # tokens

    def __init__(self):
        """Initialize indexer with API clients"""
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Initialize Pinecone
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment=os.getenv("PINECONE_ENVIRONMENT", "us-west1-gcp")
        )

        self.index_name = os.getenv("PINECONE_INDEX_NAME", "academic-website")

        # Create index if it doesn't exist
        if self.index_name not in pinecone.list_indexes():
            print(f"Creating new Pinecone index: {self.index_name}")
            pinecone.create_index(
                name=self.index_name,
                dimension=1536,  # text-embedding-3-small dimensions
                metric="cosine"
            )

        self.index = pinecone.Index(self.index_name)
        self.repo_root = Path(__file__).parent.parent

    def extract_markdown_text(self, filepath: Path) -> str:
        """Extract plain text from markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove YAML front matter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

            # Remove HTML tags but keep content
            content = re.sub(r'<[^>]+>', ' ', content)

            # Remove markdown link syntax but keep text
            content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)

            # Clean up whitespace
            content = re.sub(r'\s+', ' ', content).strip()

            return content
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return ""

    def extract_pdf_text(self, filepath: Path) -> str:
        """Extract text from PDF file"""
        try:
            reader = PdfReader(filepath)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

            # Clean up whitespace
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        except Exception as e:
            print(f"Error reading PDF {filepath}: {e}")
            return ""

    def chunk_text(self, text: str, metadata: Dict) -> List[Dict]:
        """Split text into overlapping chunks"""
        # Simple word-based chunking (tokens ≈ 0.75 * words for English)
        words = text.split()
        word_chunk_size = int(self.CHUNK_SIZE * 0.75)
        word_overlap = int(self.CHUNK_OVERLAP * 0.75)

        chunks = []
        start = 0
        chunk_index = 0

        while start < len(words):
            end = start + word_chunk_size
            chunk_words = words[start:end]
            chunk_text = ' '.join(chunk_words)

            if chunk_text.strip():
                chunk_metadata = {
                    **metadata,
                    'chunk_index': chunk_index,
                    'chunk_start': start,
                    'chunk_end': min(end, len(words)),
                    'text': chunk_text
                }
                chunks.append(chunk_metadata)
                chunk_index += 1

            start = end - word_overlap

        return chunks

    def generate_chunk_id(self, source_file: str, chunk_index: int) -> str:
        """Generate unique ID for a chunk"""
        content = f"{source_file}_{chunk_index}"
        return hashlib.md5(content.encode()).hexdigest()

    def create_embedding(self, text: str) -> List[float]:
        """Generate embedding using OpenAI API"""
        try:
            response = self.openai_client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error creating embedding: {e}")
            return None

    def determine_content_type(self, filepath: str) -> str:
        """Determine content type based on filename"""
        filepath_lower = filepath.lower()

        if 'readme' in filepath_lower:
            return 'bio'
        elif 'research' in filepath_lower:
            return 'research'
        elif 'teaching' in filepath_lower or 'syllabus' in filepath_lower:
            return 'teaching'
        elif 'cv' in filepath_lower:
            return 'cv'
        elif '.pdf' in filepath_lower:
            if 'nursing' in filepath_lower or 'comp' in filepath_lower:
                return 'research'
            else:
                return 'document'
        else:
            return 'general'

    def index_file(self, filepath: Path, file_type: str):
        """Index a single file"""
        print(f"Indexing {filepath}...")

        # Extract text
        if file_type == 'markdown':
            text = self.extract_markdown_text(filepath)
        elif file_type == 'pdf':
            text = self.extract_pdf_text(filepath)
        else:
            print(f"Unknown file type: {file_type}")
            return

        if not text:
            print(f"No text extracted from {filepath}")
            return

        # Create metadata
        metadata = {
            'source_file': str(filepath.relative_to(self.repo_root)),
            'content_type': self.determine_content_type(str(filepath)),
            'file_type': file_type,
            'indexed_at': datetime.utcnow().isoformat(),
        }

        # Chunk text
        chunks = self.chunk_text(text, metadata)
        print(f"  Created {len(chunks)} chunks")

        # Generate embeddings and upload to Pinecone
        vectors_to_upsert = []
        for chunk in chunks:
            chunk_id = self.generate_chunk_id(
                metadata['source_file'],
                chunk['chunk_index']
            )

            embedding = self.create_embedding(chunk['text'])
            if embedding is None:
                continue

            # Prepare vector for Pinecone
            vector_metadata = {
                'source_file': chunk['source_file'],
                'content_type': chunk['content_type'],
                'file_type': chunk['file_type'],
                'chunk_index': chunk['chunk_index'],
                'text': chunk['text'][:1000],  # Pinecone metadata limit
                'indexed_at': chunk['indexed_at']
            }

            vectors_to_upsert.append((chunk_id, embedding, vector_metadata))

        # Batch upsert to Pinecone
        if vectors_to_upsert:
            batch_size = 100
            for i in range(0, len(vectors_to_upsert), batch_size):
                batch = vectors_to_upsert[i:i + batch_size]
                self.index.upsert(vectors=batch)
            print(f"  Uploaded {len(vectors_to_upsert)} vectors to Pinecone")

    def index_all(self):
        """Index all configured files"""
        print(f"Starting indexing at {datetime.now()}")
        print(f"Repository root: {self.repo_root}")
        print(f"Pinecone index: {self.index_name}")
        print("-" * 50)

        # Clear existing index (full re-index)
        print("Clearing existing index...")
        self.index.delete(delete_all=True)

        # Index markdown files
        for filepath in self.MARKDOWN_FILES:
            full_path = self.repo_root / filepath
            if full_path.exists():
                self.index_file(full_path, 'markdown')
            else:
                print(f"Warning: {filepath} not found")

        # Index PDF files
        for filepath in self.PDF_FILES:
            full_path = self.repo_root / filepath
            if full_path.exists():
                self.index_file(full_path, 'pdf')
            else:
                print(f"Warning: {filepath} not found")

        # Get index stats
        stats = self.index.describe_index_stats()
        print("-" * 50)
        print(f"Indexing complete!")
        print(f"Total vectors in index: {stats.total_vector_count}")
        print(f"Finished at {datetime.now()}")


def main():
    """Main entry point"""
    # Check environment variables
    required_vars = ['OPENAI_API_KEY', 'PINECONE_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print("Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"  - {var}")
        sys.exit(1)

    # Run indexer
    indexer = ContentIndexer()
    indexer.index_all()


if __name__ == '__main__':
    main()
