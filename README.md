# Demo LLM - LangChain Agent Research Assistant

A research assistant application built with LangChain using `create_tool_calling_agent` and `AgentExecutor` to generate structured research responses.

## Features

- Uses LangChain's `create_tool_calling_agent` for tool-calling agent creation
- Structured output using Pydantic models
- Research response generation with topic, summary, sources, and tools used

## Requirements

- Python 3.13+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Rajkumarceo/demo-llm.git
cd demo-llm
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

The agent will process queries and return structured research responses in JSON format.

## Project Structure

- `main.py` - Main application file with agent setup and execution
- `tools.py` - Tools module (currently empty, ready for custom tools)
- `requirements.txt` - Python dependencies

## Dependencies

- `langchain` - Core LangChain library
- `langchain-classic` - Provides `create_tool_calling_agent` and `AgentExecutor`
- `langchain-openai` - OpenAI integration
- `langchain-core` - Core LangChain utilities
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation

