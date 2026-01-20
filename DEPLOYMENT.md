# Deployment Checklist

This checklist will guide you through deploying the website improvements and AI assistant.

## Pre-Deployment Checklist

### 1. Review Changes
- [ ] Review all CSS changes in `assets/css/main.css`
- [ ] Review JavaScript changes in `assets/js/main.js`
- [ ] Review updated page layouts (README.md, Research.md, Teaching.md, CV.md)
- [ ] Test website locally if possible

### 2. Set Up AI Assistant Infrastructure (Optional)

If you want to deploy the AI assistant:

- [ ] Create Pinecone account and index
- [ ] Get OpenAI API key
- [ ] Add GitHub Secrets (see AI_ASSISTANT_README.md)
- [ ] Choose deployment platform (Vercel recommended)

## Deployment Steps

### Phase 1: Deploy Website Updates (No AI Assistant)

These changes improve design, UX, and code quality:

1. **Commit and Push Changes**
```bash
git add .
git commit -m "Refactor: Consolidate CSS/JS, improve UX, optimize for mobile"
git push origin main
```

2. **Verify GitHub Pages Build**
- Go to Settings → Pages
- Verify build completes successfully
- Visit your site and test:
  - [ ] Homepage displays correctly with new tagline
  - [ ] Navigation works on desktop and mobile
  - [ ] Research page cards display properly
  - [ ] Teaching page works
  - [ ] CV page shows download button (not iframe)
  - [ ] Social links work
  - [ ] All pages are mobile-responsive

### Phase 2: Deploy AI Assistant (Optional)

Only proceed if you want the AI assistant feature:

1. **Set Up Services**
- [ ] Create Pinecone account and index (1536 dimensions, cosine metric)
- [ ] Create OpenAI API key
- [ ] Note all credentials

2. **Configure GitHub**
- [ ] Add secrets to GitHub repository:
  - `OPENAI_API_KEY`
  - `PINECONE_API_KEY`
  - `PINECONE_ENVIRONMENT`
  - `PINECONE_INDEX_NAME`

3. **Run Initial Indexing**
```bash
# Option A: Via GitHub Actions
# Go to Actions → "Index Content for AI Assistant" → Run workflow

# Option B: Locally (for testing)
pip install -r scripts/requirements.txt
export OPENAI_API_KEY="your-key"
export PINECONE_API_KEY="your-key"
export PINECONE_ENVIRONMENT="us-west1-gcp"
python scripts/index_content.py
```

4. **Deploy API Endpoint**

**Recommended: Vercel**

```bash
# Install Vercel CLI
npm install -g vercel

# Create vercel.json (already in repo)
# Add environment variables to Vercel

# Deploy
vercel --prod

# Note the API URL (e.g., https://yoursite.vercel.app/api/query)
```

5. **Enable Chat Widget**

Edit `assets/js/main.js`:
```javascript
// Around line 220, uncomment:
const assistant = new AcademicAssistant();

// Around line 45, update API endpoint:
this.apiEndpoint = 'https://your-actual-api-url.vercel.app/api/query';
```

Commit and push:
```bash
git add assets/js/main.js
git commit -m "feat: Enable AI assistant chat widget"
git push origin main
```

6. **Test AI Assistant**
- [ ] Visit your website
- [ ] Click "Ask AI" button in bottom right
- [ ] Try asking: "What does Ivan research?"
- [ ] Verify answer is accurate and cites sources
- [ ] Test on mobile device

## Post-Deployment Verification

### Website Quality Checks
- [ ] All pages load correctly
- [ ] No console errors (check browser DevTools)
- [ ] Mobile responsive design works
- [ ] PDF downloads work
- [ ] Links work (research papers, social links)
- [ ] Typography looks consistent

### AI Assistant Checks (if deployed)
- [ ] Chat widget appears in bottom right
- [ ] Can open and close chat
- [ ] Suggested questions work
- [ ] Custom questions get responses
- [ ] Responses cite sources
- [ ] No API errors in console

### Performance Checks
- [ ] Page loads in < 3 seconds
- [ ] Images load properly
- [ ] No unnecessary large file downloads
- [ ] CSS and JS files load

## Monitoring

### Check Monthly
- [ ] Review Pinecone dashboard (vector count, usage)
- [ ] Review OpenAI usage (embeddings + completions)
- [ ] Check GitHub Actions success rate for indexing
- [ ] Review any error logs

### Update When Needed
- [ ] When you add publications → Update Research.md → Auto-reindexing triggers
- [ ] When you update CV → Replace PDF → Auto-reindexing triggers
- [ ] When you change teaching → Update Teaching.md → Auto-reindexing triggers

## Cost Management

### Expected Costs (with AI Assistant)
- **Pinecone**: $0/month (free tier sufficient)
- **OpenAI Embeddings**: ~$0.01/month (re-indexing)
- **OpenAI Completions**: ~$0.03-0.50/month (depends on queries)
- **Vercel/Netlify**: $0/month (free tier sufficient)

**Total: $0.04 - 0.60/month**

### Cost Optimization
- Use free tier limits (sufficient for academic website)
- Index only necessary files
- Set usage alerts in OpenAI dashboard
- Monitor query volume

## Rollback Plan

If something breaks:

```bash
# Rollback to previous commit
git log  # Find previous commit hash
git revert <commit-hash>
git push origin main

# Or restore specific file
git checkout HEAD~1 -- path/to/file
git commit -m "Restore file"
git push origin main
```

## Support Resources

- **Jekyll**: https://jekyllrb.com/docs/
- **GitHub Pages**: https://docs.github.com/en/pages
- **OpenAI**: https://platform.openai.com/docs
- **Pinecone**: https://docs.pinecone.io/
- **Vercel**: https://vercel.com/docs

## Optional Enhancements (Future)

Consider adding:
- [ ] Google Analytics for visitor tracking
- [ ] SEO optimization (meta tags, sitemap)
- [ ] Newsletter signup
- [ ] Blog section for research updates
- [ ] Image optimization (compress JPEGs)
- [ ] Favicon
- [ ] Open Graph tags for social sharing

## Notes

- **Do not commit API keys** to the repository (use GitHub Secrets)
- **Test locally first** if possible before pushing to production
- **Keep README.md updated** with any manual setup instructions
- **Document any custom changes** you make to the AI assistant

## Quick Start (If skipping AI Assistant)

If you just want the design improvements without AI:

```bash
# 1. Push changes
git add .
git commit -m "Improve website design and code quality"
git push origin main

# 2. Wait for GitHub Pages to rebuild (~2-3 minutes)

# 3. Visit your site and verify

# Done! 🎉
```

The AI assistant can be added later without affecting current functionality.
