from langsmith import Client
from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatDeepSeek(model="deepseek-chat", temperature=0)
client = Client()
prompt = client.pull_prompt("rlm/rag-prompt")

generation_chain = prompt | llm| StrOutputParser()