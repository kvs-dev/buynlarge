import getpass
from typing import TypedDict
from os import getenv
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain import hub
from typing_extensions import Annotated
from langchain.chat_models import init_chat_model
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from langgraph.graph import START, StateGraph

load_dotenv()

if not getenv("GROQ_API_KEY"):
    getenv["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

db = SQLDatabase.from_uri(f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}")
llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str

class QueryOutput(TypedDict):
    """Generated SQL query."""
    query: Annotated[str, ..., "Syntactically valid SQL query."]

query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")

def write_query(state: State):
    """Generate SQL query to fetch information."""
    prompt = query_prompt_template.invoke(
        {
            "dialect": db.dialect,
            "top_k": 10,
            "table_info": db.get_table_info(),
            "input": state["question"],
        }
    )
    structured_llm = llm.with_structured_output(QueryOutput)
    result = structured_llm.invoke(prompt)
    return {"query": result["query"]}

def execute_query(state: State):
    """Execute SQL query."""
    execute_query_tool = QuerySQLDatabaseTool(db=db)
    return {"result": execute_query_tool.invoke(state["query"])}

def generate_answer(state: State):
    """Answer question using retrieved information as context."""
    prompt = (
        "Given the following user question, corresponding SQL query, "
        "and SQL result, answer the user question.\n\n"
        f'Question: {state["question"]}\n'
        f'SQL Query: {state["query"]}\n'
        f'SQL Result: {state["result"]}'
    )
    response = llm.invoke(prompt)
    return {"answer": response.content}

def create_graph():
    graph_builder = StateGraph(State).add_sequence(
        [write_query, execute_query, generate_answer]
    )
    graph_builder.add_edge(START, "write_query")
    return graph_builder.compile()

def process_question(question: str):
    """Process a question and return all steps and final answer."""
    graph = create_graph()
    steps = []
    for step in graph.stream({"question": question}, stream_mode="updates"):
        steps.append(step)
    return steps 