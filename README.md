# AI Agent Monitoring POC

This project demonstrates monitoring of OpenAI GPT calls using Langfuse.

## ✅ Features
- Logs GPT input/output
- Tracks token usage and latency
- Stores logs with Langfuse UI

## 🚀 Usage
1. Clone the repo
2. Create a `.env` file with your API keys
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

## 🔧 Setup Langfuse
- Create a project on [Langfuse Cloud](https://cloud.langfuse.com)
- Get your public & secret keys and add them to `.env`

## 🐳 Run in Docker
```bash
docker build -t ai-agent-monitoring .
docker run --env-file .env ai-agent-monitoring
```

## 🤖 GitHub Actions
- Automatically lints code on push/pull requests

## 📸 Sample Output
```
> Enter a prompt for the AI agent:
Explain credit default swaps.

--- AI Response ---
Credit default swaps are ...
```
```
Then view the trace in the Langfuse dashboard.
```
```