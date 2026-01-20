# AI Research Assistant - Setup Guide

This document explains how to set up and deploy the AI-powered research assistant for your academic website.

## Overview

The AI assistant allows visitors to ask questions about your research, publications, CV, and teaching. It uses:

- **OpenAI Embeddings** (text-embedding-3-small) for semantic search
- **Pinecone** for vector storage
- **OpenAI GPT-4o-mini** for generating responses
- **RAG (Retrieval Augmented Generation)** to ground answers in your actual content

## Architecture

```
Content Updates (MD/PDF files)
    ↓
GitHub Actions triggers indexing
    ↓
Python script extracts & chunks text
    ↓
OpenAI creates embeddings
    ↓
Vectors stored in Pinecone
    ↓
User asks question on website
    ↓
Query API searches Pinecone
    ↓
Relevant chunks retrieved
    ↓
GPT-4o-mini generates grounded answer
    ↓
Response displayed to user
```

## Setup Instructions

### Step 1: Create Pinecone Account

1. Go to [pinecone.io](https://www.pinecone.io/) and sign up
2. Create a new project
3. Note your:
   - API Key
   - Environment (e.g., `us-west1-gcp`)
4. Create an index named `academic-website` with:
   - Dimensions: 1536
   - Metric: cosine

### Step 2: Get OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Create an API key
3. Add billing information (required for API access)

### Step 3: Configure GitHub Secrets

Add these secrets to your GitHub repository (Settings → Secrets and variables → Actions):

- `OPENAI_API_KEY` - Your OpenAI API key
- `PINECONE_API_KEY` - Your Pinecone API key
- `PINECONE_ENVIRONMENT` - Your Pinecone environment (e.g., `us-west1-gcp`)
- `PINECONE_INDEX_NAME` - Name of your index (default: `academic-website`)

### Step 4: Run Initial Indexing

Option A: Trigger via GitHub Actions
1. Go to Actions tab in GitHub
2. Select "Index Content for AI Assistant"
3. Click "Run workflow"

Option B: Run locally
```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Set environment variables
export OPENAI_API_KEY="your-key"
export PINECONE_API_KEY="your-key"
export PINECONE_ENVIRONMENT="us-west1-gcp"
export PINECONE_INDEX_NAME="academic-website"

# Run indexing
python scripts/index_content.py
```

### Step 5: Deploy API Endpoint

Choose one deployment option:

#### Option A: Vercel (Recommended - Easiest)

1. Install Vercel CLI: `npm install -g vercel`
2. Create `vercel.json` in repo root:
```json
{
  "functions": {
    "api/query.py": {
      "runtime": "python3.9"
    }
  },
  "env": {
    "OPENAI_API_KEY": "@openai-api-key",
    "PINECONE_API_KEY": "@pinecone-api-key",
    "PINECONE_ENVIRONMENT": "@pinecone-environment",
    "PINECONE_INDEX_NAME": "@pinecone-index-name"
  }
}
```
3. Deploy: `vercel --prod`
4. Add environment variables in Vercel dashboard
5. Note your API URL (e.g., `https://yoursite.vercel.app/api/query`)

#### Option B: Netlify Functions

1. Create `netlify.toml`:
```toml
[build]
  functions = "api"

[functions]
  directory = "api"
```
2. Deploy to Netlify
3. Add environment variables in Netlify dashboard

#### Option C: AWS Lambda

1. Use the `lambda_handler` function in `api/query.py`
2. Create Lambda function with Python 3.9+ runtime
3. Add API Gateway trigger
4. Set environment variables

### Step 6: Enable Chat Widget

1. Open `assets/js/main.js`
2. Find line ~220: `// const assistant = new AcademicAssistant();`
3. Uncomment it: `const assistant = new AcademicAssistant();`
4. Update the API endpoint in the `AcademicAssistant` class:
```javascript
this.apiEndpoint = 'https://your-api-url.vercel.app/api/query';
```
5. Commit and push changes

## Cost Estimates

### Indexing Costs (One-time per update)
- ~50 chunks × $0.00002 per 1K tokens = **$0.001 per indexing run**
- With monthly updates: **~$0.01/month**

### Query Costs
- Embedding: $0.00002 per query
- GPT-4o-mini: ~$0.0003 per query (avg 1500 input + 300 output tokens)
- **Total: ~$0.0003 per query**

At 100 queries/month: **~$0.03/month**
At 1000 queries/month: **~$0.30/month**

### Pinecone Costs
- Free tier: 1 index, 100K vectors (more than enough)
- **$0/month** (until you exceed free tier)

**Total estimated cost: $0.03 - $0.50/month depending on usage**

## Customization

### Adding More Files to Index

Edit `scripts/index_content.py`:

```python
MARKDOWN_FILES = [
    "README.md",
    "Research.md",
    "Teaching.md",
    "CV.md",
    "NewPage.md",  # Add your file
]

PDF_FILES = [
    "files/Academic_CV.pdf",
    "files/YourPaper.pdf",  # Add your file
]
```

### Changing System Prompt

Edit `api/query.py` - modify the `SYSTEM_PROMPT` constant to change how the AI responds.

### Adjusting Search Parameters

In `api/query.py`, `semantic_search()` method:
- `top_k=5` - Number of chunks to retrieve (increase for more context)
- `temperature=0.3` - Lower = more factual, higher = more creative

## Testing

### Test Indexing
```bash
python scripts/index_content.py
```

### Test API Locally
```python
# test_api.py
import requests

response = requests.post(
    'http://localhost:8000/api/query',  # Your local/deployed endpoint
    json={'question': 'What does Ivan research?'}
)
print(response.json())
```

### Test UI
1. Open your website
2. Click the "Ask AI" button (bottom right)
3. Try suggested questions or ask your own

## Troubleshooting

### Indexing fails
- Check API keys are set correctly
- Verify Pinecone index exists with correct dimensions (1536)
- Check PDF files are valid and readable

### API returns errors
- Verify environment variables are set in deployment platform
- Check API rate limits (OpenAI, Pinecone)
- Review deployment logs

### Chat widget doesn't appear
- Verify you uncommented the initialization in `main.js`
- Check browser console for JavaScript errors
- Ensure CSS is loading correctly

### Answers are inaccurate
- Re-run indexing to ensure latest content is indexed
- Increase `top_k` in search for more context
- Adjust system prompt for better instructions

## Maintenance

### Automatic Updates
- GitHub Actions automatically re-indexes when you update markdown or PDF files
- No manual action needed after initial setup

### Manual Re-indexing
If needed, trigger the "Index Content" workflow manually in GitHub Actions

## Privacy & Safety

The assistant:
- ✅ Only answers from indexed content
- ✅ Does not store conversation history server-side
- ✅ Cannot access external information
- ✅ Has scope constraints to stay on-topic
- ✅ Cites sources for transparency

It will NOT:
- ❌ Make up information
- ❌ Answer questions outside academic scope
- ❌ Share sensitive information (unless you indexed it)

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review OpenAI/Pinecone documentation
3. Check GitHub Actions logs for indexing errors
4. Review browser console for UI errors

## Future Enhancements

Consider adding:
- Conversation history (stored client-side)
- Multi-turn conversations
- FAQ page showing common questions
- Analytics to track popular queries
- Support for more file types (DOCX, etc.)
