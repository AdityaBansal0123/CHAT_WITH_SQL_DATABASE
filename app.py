import streamlit as st
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
import os

st.set_page_config(page_title="LangChain: Chat with MySQL", page_icon="🦜")
st.title("🦜 LangChain: Chat with MySQL")

# MySQL connection input fields
mysql_host = st.sidebar.text_input("MySQL Host", placeholder="e.g., localhost")
mysql_user = st.sidebar.text_input("MySQL User", placeholder="e.g., root")
mysql_password = st.sidebar.text_input("MySQL Password", type="password")
mysql_db = st.sidebar.text_input("MySQL Database", placeholder="e.g., student_db")

# Get GROQ API key from sidebar or environment variable
api_key_input = st.sidebar.text_input(label="GROQ API Key", type="password")
groq_key = api_key_input or os.getenv("GROQ_API_KEY")

# Validate inputs
if not (mysql_host and mysql_user and mysql_password and mysql_db):
    st.warning("Please fill in all MySQL connection fields.")
    st.stop()

if not groq_key:
    st.warning("Please provide the GROQ API key.")
    st.stop()

# Initialize LLM
llm = ChatGroq(groq_api_key=groq_key, model_name="Llama3-8b-8192", streaming=True)

# Connect to MySQL
@st.cache_resource(ttl="2h")
def configure_db(mysql_host, mysql_user, mysql_password, mysql_db):
    return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

db = configure_db(mysql_host, mysql_user, mysql_password, mysql_db)

# Set up LangChain toolkit and agent
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Chat session logic
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you with your MySQL database?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask anything from your MySQL database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
