from sys import modules
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent



import tools

load_dotenv()


class ResearchResponse(BaseModel):
    topic:str
    summary: str
    sources: list[str]
    tools_used:list[str]


llm=ChatOpenAI(model="gpt-4o-mini")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help to generate a research paper.
            Answer the user query and use the necessary tools.
            Wrap the output in this format and provide no other text.
            {format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions()) 

# Create agent using create_tool_calling_agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=[],
    prompt=prompt
)

# Create agent executor
agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)

# Invoke the agent executor
raw_response = agent_executor.invoke({"query": "what is the capital of France?"})
print(raw_response)
