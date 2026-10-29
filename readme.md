# 🤖 AI Agent — Smart Assistant with LangChain

An intelligent AI agent built with **LangChain, an LLM, and Streamlit** that can answer questions, search the web, retrieve weather information, and convert currencies using external tools.

The project demonstrates how an LLM-powered agent can understand user queries, select the appropriate tools, execute actions, and combine their results into a helpful response.

## ✨ Features

- **🧠 LLM-Powered Reasoning:** Understands natural-language questions and decides how to respond.
- **🔎 Web Search:** Uses the Tavily Search API to retrieve relevant, up-to-date information from the web.
- **🌦️ Weather Information:** Fetches weather information for a specified city using a weather API.
- **💱 Currency Conversion:** Converts amounts between currencies using exchange-rate data.
- **🛠️ Tool Calling:** Integrates external Python functions as tools using LangChain's `@tool` decorator.
- **💬 Interactive UI:** Provides a simple chat interface using Streamlit.
- **🔐 Environment-Based Configuration:** Stores API credentials in a `.env` file rather than hardcoding them in source code.

## 🏗️ Architecture

```text
                ┌──────────────────────┐
                │        User          │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Streamlit UI      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   LangChain Agent    │
                │                      │
                │  LLM + Tool Calling  │
                └──────────┬───────────┘
                           │
               ┌───────────┼───────────┐
               ▼           ▼           ▼
         ┌──────────┐ ┌──────────┐ ┌───────────┐
         │  Tavily  │ │  Weather │ │ Currency  │
         │  Search  │ │   API    │ │ Converter │
         └────┬─────┘ └────┬─────┘ └─────┬─────┘
              │            │             │
              └────────────┼─────────────┘
                           ▼
                ┌──────────────────────┐
                │  Tool Results + LLM  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Response to User    │
                └──────────────────────┘
```

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Agent creation and tool integration |
| LLM | Natural-language understanding, reasoning, and response generation |
| LangChain Groq integration | Connects to supported LLMs hosted by Groq, if Groq is used |
| Tavily Search API | Web search and current information retrieval |
| Weather API | Weather information retrieval |
| Currency Exchange API | Exchange-rate lookup and currency conversion |
| Streamlit | Interactive web interface |
| python-dotenv | Environment variable management |
| uv | Python dependency and project management |

## 📂 Project Structure

```text
ai-agent/
├── app.py                 # Streamlit application
├── agent.py               # Agent initialization and execution
├── tools.py               # Search, weather, and currency tools
├── .env                   # API keys (never commit this file)
├── .gitignore             # Files excluded from Git
├── pyproject.toml         # Project dependencies (uv)
├── uv.lock                # Locked dependency versions
└── README.md              # Project documentation
```

*The filenames are a suggested structure; adjust them to match your actual project.*

## ⚙️ Prerequisites

Before starting, make sure you have:

- Python 3.10 or newer, compatible with your selected dependencies.
- [uv](https://docs.astral.sh/uv/) installed.
- An API key for your selected LLM provider.
- A Tavily API key.
- A valid API key for your chosen weather service.
- Access to a currency exchange-rate API.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-agent.git
cd ai-agent
```

Replace `YOUR_USERNAME/ai-agent` with your actual GitHub repository path.

### 2. Create the environment

```bash
uv sync
```

If you're starting from scratch, initialize a project and install the dependencies:

```bash
uv init
uv add langchain langchain-groq tavily-python streamlit python-dotenv requests
```

Add any additional packages required by your selected weather and currency APIs.

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHER_API_KEY=your_weather_api_key
CURRENCY_API_KEY=your_currency_api_key
```

Replace each placeholder with your actual credential. The variable names in `.env` must match those used in your Python code.

If you use another LLM provider, configure its corresponding credentials instead.

### 4. Run the application

```bash
uv run streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to interact with the agent.

## 🔧 How It Works

1. **User input:** The user submits a natural-language query through the Streamlit chat interface.
2. **Agent reasoning:** The LangChain agent passes the query to the configured LLM.
3. **Tool selection:** Based on the query and tool descriptions, the LLM can request a suitable tool.
4. **Tool execution:** LangChain executes the selected Python function and obtains its result.
5. **Response generation:** The LLM uses the returned result to prepare a natural-language answer.
6. **UI update:** Streamlit displays the answer to the user.

For example, a request about the weather may invoke the weather tool, while a request for the latest technology news may invoke Tavily Search.

## 💡 Example Queries

| User query | Expected capability |
|---|---|
| "What are the latest developments in AI?" | Tavily web search |
| "What is the weather in Mumbai?" | Weather API |
| "Convert 500 USD to INR." | Currency converter |
| "Search for recent advancements in robotics." | Tavily web search |
| "What is the weather in Delhi, and what should I wear?" | Weather lookup followed by an LLM-generated recommendation |

Actual tool selection depends on the agent's instructions, the available tools, and the LLM's tool-calling capabilities.

## 🔐 Security

- Never commit API keys, passwords, or tokens to GitHub.
- Add `.env` to `.gitignore`.
- Use environment variables to load credentials.
- Rotate any API key that has accidentally been exposed.
- Avoid printing secrets in application logs.
- Apply timeouts and handle API errors gracefully.

Example `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
.ipynb_checkpoints/
.streamlit/secrets.toml
```

## 🛣️ Future Improvements

- Add conversation memory for multi-turn interactions.
- Display search sources and citations in the UI.
- Add streaming responses for a more responsive chat experience.
- Implement API timeouts, retry logic, and rate-limit handling.
- Add structured logging and latency measurements.
- Improve error handling for invalid cities and currency codes.
- Add automated tests for individual tools.
- Deploy the application to Streamlit Community Cloud or another hosting platform.

## 🎯 Learning Objectives

This project helps demonstrate practical understanding of:

- LLM-powered AI agents.
- LangChain tool calling and the `@tool` decorator.
- Integration of external REST APIs.
- Agent orchestration with `create_agent()`.
- Environment variables and API credential management.
- Building an interactive AI application with Streamlit.
- Error handling and external-service integration.

## 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request describing your improvements.


