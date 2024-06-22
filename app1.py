## Conversational QnA chatbot 
import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage

from langchain.chat_models import ChatOpenAI

## Streamlit UI
st.set_page_config(page_title="Conversational QnA chatbot")
st.header("HEY lets CHAT")
from dotenv import load_dotenv
load_dotenv()
import os

chat=ChatOpenAI(temperature=0.5)

# Function to load OpenAi model and get response
def get_openai_response(question):
    
    response=llm(question)
    return response