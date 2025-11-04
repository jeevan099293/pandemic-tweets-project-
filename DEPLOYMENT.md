# Deployment Guide

## 🚀 Deploy to Render.com

### Option 1: Automatic Deployment via render.yaml

1. **Sign up/Login to Render**
   - Go to https://render.com
   - Sign up or login with your GitHub account

2. **Create New Static Site**
   - Click "New +" button
   - Select "Static Site"

3. **Connect GitHub Repository**
   - Choose "Connect a repository"
   - Select: `jeevan099293/pandemic-tweets-project-`
   - Click "Connect"

4. **Configure Deployment**
   - Render will automatically detect `render.yaml`
   - Or manually configure:
     - **Name**: mental-health-tweets-dashboard
     - **Branch**: main
     - **Build Command**: `pip install -r requirements.txt && python generate_data.py`
     - **Publish Directory**: `.` (root)

5. **Deploy**
   - Click "Create Static Site"
   - Wait 2-3 minutes for deployment
   - Your site will be live at: `https://mental-health-tweets-dashboard.onrender.com`

---

## 🌐 Deploy to GitHub Pages (Free & Easy)

1. **Enable GitHub Pages**
   - Go to: https://github.com/jeevan099293/pandemic-tweets-project-/settings/pages
   - Under "Source", select **main** branch
   - Select **/ (root)** folder
   - Click **Save**

2. **Access Your Live Site**
   - Wait 1-2 minutes
   - Visit: https://jeevan099293.github.io/pandemic-tweets-project-/

---

## 📦 Deploy to Netlify

1. **Sign up/Login to Netlify**
   - Go to https://netlify.com
   - Login with GitHub

2. **Import Project**
   - Click "Add new site" → "Import an existing project"
   - Choose GitHub
   - Select: `pandemic-tweets-project-`

3. **Configure**
   - Build command: `pip install -r requirements.txt && python generate_data.py`
   - Publish directory: `.`
   - Click "Deploy site"

4. **Access**
   - Your site: `https://[random-name].netlify.app`
   - Can customize domain name in settings

---

## 🔧 Deploy to Vercel

1. **Sign up/Login to Vercel**
   - Go to https://vercel.com
   - Login with GitHub

2. **Import Repository**
   - Click "Add New" → "Project"
   - Import: `pandemic-tweets-project-`

3. **Configure**
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt && python generate_data.py`
   - Output Directory: `.`

4. **Deploy**
   - Click "Deploy"
   - Live at: `https://pandemic-tweets-project.vercel.app`

---

## 📝 Local Development

To run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate data files
python generate_data.py

# Start local server
python -m http.server 8000

# Open browser
http://localhost:8000
```

---

## ✅ Recommended: GitHub Pages (Easiest)

**Why?**
- ✅ Free
- ✅ No configuration needed
- ✅ Automatic updates on push
- ✅ Custom domain support
- ✅ Built-in SSL

**Your Live URL:**
```
https://jeevan099293.github.io/pandemic-tweets-project-/
```

Just enable it in GitHub Settings → Pages!

---

## 🎯 Show to Your Teacher

Share any of these URLs:
1. **GitHub Pages**: https://jeevan099293.github.io/pandemic-tweets-project-/
2. **GitHub Repo**: https://github.com/jeevan099293/pandemic-tweets-project-
3. **Local Demo**: http://localhost:8000 (if running locally)

---

## 💡 Tips

- GitHub Pages is recommended for academic projects (free, reliable)
- Render is good for dynamic sites with build steps
- All platforms support custom domains
- SSL/HTTPS is automatic on all platforms

---

**Your project is deployment-ready! 🚀**
