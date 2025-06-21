# SmolAgents Toolbelt

A curated collection of practical, lightweight agents built using [`smolagents`](https://github.com/smol-ai/smol-agents) and the OpenAI API.

This repo is a hands-on toolbelt of example agents that demonstrate reasoning, tool usage, multi-agent collaboration, and real-world integrations using minimal code. Each agent serves as a composable blueprint for your own LLM-powered applications.

---

## Included Agents

### 🔍 1. Basic Web Search Agent
A single-agent web search setup that retrieves and summarizes 5 facts about any country.

> **Use case**:  
> “Japan”

## Runing the backend app
```bash
uvicorn web-search:app --reload
```

## Runnig the frontend app
```bash
python gradio_ui.py
```
---

### 2. Multi-Agent System: Manager + Web Search Agents
A coordinated multi-agent framework where a "Manager" agent breaks down a complex task and delegates sub-tasks to Web Search agents.

> **Use case**:  
> “Create a step-by-step roadmap to become a machine learning engineer.”

---

### 3. Tool-Calling Agent
An agent that dynamically selects and uses tools such as web search or calculator, depending on task requirements. Highlights OpenAI function calling with tool wrappers.

> **Use case**:  
> “Check the weather in Tokyo and explain its seasonal climate trends.”

---

### 4. File QA Agent (PDF or TXT Question Answering)
An agent that reads, summarizes, and answers questions from `.txt` or `.pdf` files using retrieval and summarization techniques.

> **Use case**:  
> “Analyze this research paper and extract the main findings.”

---

### 5. GitHub Issue Agent
Pulls open issues from a GitHub repo, classifies them (bug, feature request, etc.), and drafts a triage or response message. Uses OpenAI to automate project maintenance.

> **Use case**:  
> “Automatically label and respond to new GitHub issues.”

---

## Tech Stack

- [`smolagents`](https://github.com/smol-ai/smol-agents)
- OpenAI API (`gpt-3.5-turbo`, `gpt-4`)
- DuckDuckGoSearchTool
- Python 3.10+
- `.env`-based credential management
- Optional: GitHub API, PDF libraries (`pdfminer.six`, `PyMuPDF`)

---

## Getting Started

```bash
git clone https://github.com/your-username/smolagents-toolbelt.git
cd smolagents-toolbelt
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
