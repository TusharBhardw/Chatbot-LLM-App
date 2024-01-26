from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input,prompt):
    model= genai.GenerativeModel("gemini-pro")
    response=model.generate_content([input,prompt])
    return response



st.set_page_config(page_title="Mental Health Support")
st.header("Check")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
input_text=st.text_input("Input: ",key="input")

submit=st.button("Enter")

input_prompt = """
You are an advanced Mental Health Support Chatbot, you have to talk people like a freind.
You should be capable of understanding and responding empathetically to users expressing various 
emotional states or seeking guidance. 
Your task is to reply like a freind to user inputs related to mental health and reply in 2 to 3 line max 
"""


if submit and input_text:
    response=get_gemini_response(input_text,input_prompt)
    st.session_state['chat_history'].append(("You",input_text))
    st.subheader("The Response is")
    st.write(response.text)
    st.session_state['chat_history'].append(("Bot",response.text))

st.subheader('The chat history is')
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")


