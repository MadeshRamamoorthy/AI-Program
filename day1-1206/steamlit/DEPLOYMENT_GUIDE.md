# Claude Chatbot - Deployment Guide

## 📋 Files You Need

1. `chatbot_app.py` - Main application
2. `requirements.txt` - Dependencies
3. `secrets.toml.template` - Template for API key (rename for local use)

---

## 🚀 Step-by-Step Deployment to Streamlit Cloud

### Step 1: Prepare Your Files

1. **Get a NEW API key** (your old one is compromised):
   - Go to: https://console.anthropic.com/settings/keys
   - Delete the old key
   - Click "Create Key"
   - Copy and save it securely

2. **Create a GitHub repository**:
   - Go to https://github.com
   - Click "New Repository"
   - Name it (e.g., "claude-chatbot")
   - Make it **Private** (recommended for API projects)
   - Click "Create Repository"

### Step 2: Upload Your Files to GitHub

You can upload files via the GitHub web interface:

1. Click "uploading an existing file"
2. Upload these files:
   - `chatbot_app.py`
   - `requirements.txt`
3. Click "Commit changes"

### Step 3: Deploy on Streamlit Cloud

1. **Sign up for Streamlit Cloud**:
   - Go to: https://streamlit.io/cloud
   - Click "Sign up" or "Get started"
   - Sign in with your GitHub account

2. **Deploy your app**:
   - Click "New app"
   - Select your repository: `claude-chatbot`
   - Main file path: `chatbot_app.py`
   - Click "Advanced settings"

3. **Add your API key securely**:
   - In the "Secrets" section, paste:
     ```toml
     ANTHROPIC_API_KEY = "sk-ant-api03-YOUR-NEW-KEY-HERE"
     ```
   - Replace with your NEW API key

4. **Deploy**:
   - Click "Deploy!"
   - Wait 2-3 minutes for deployment

5. **Access your chatbot**:
   - You'll get a URL like: `https://your-app-name.streamlit.app`
   - Share this URL to use your chatbot!

---

## 💻 Running Locally (Optional)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key**:
   - Create a folder: `.streamlit`
   - Create file: `.streamlit/secrets.toml`
   - Add your API key:
     ```toml
     ANTHROPIC_API_KEY = "sk-ant-api03-YOUR-NEW-KEY-HERE"
     ```

3. **Run the app**:
   ```bash
   streamlit run chatbot_app.py
   ```

4. **Open in browser**:
   - The app will open automatically at `http://localhost:8501`

---

## 🔒 Security Best Practices

✅ **DO:**
- Keep your API key in Streamlit secrets (cloud) or `.streamlit/secrets.toml` (local)
- Use a private GitHub repository
- Never commit secrets to Git
- Regenerate keys if exposed

❌ **DON'T:**
- Share your API key publicly
- Commit secrets.toml to GitHub
- Use the API key shown in your original message (delete it!)

---

## 📊 Features

- **Word Limits**: 
  - User questions: Max 200 words
  - Claude responses: Max 500 words
- **Chat History**: Maintains conversation context
- **Clear Chat**: Button to start fresh
- **Error Handling**: User-friendly error messages

---

## 🛠️ Troubleshooting

**"Please add your ANTHROPIC_API_KEY" error:**
- Check that you added the key in Streamlit Cloud secrets
- Verify the key format is correct (starts with `sk-ant-`)

**"Invalid API key" error:**
- Your API key may be deleted or invalid
- Generate a new key at https://console.anthropic.com

**App won't start:**
- Check that all files are uploaded to GitHub
- Verify `requirements.txt` is present
- Check Streamlit Cloud logs for errors

---

## 📞 Support

- Streamlit Docs: https://docs.streamlit.io
- Anthropic Docs: https://docs.anthropic.com
- GitHub Issues: Create an issue in your repository

---

## 🎉 You're Done!

Your Claude chatbot is now live and ready to use!
