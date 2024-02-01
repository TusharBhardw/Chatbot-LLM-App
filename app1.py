from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model= genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(message):
    response=model.generate_content(message)
    return response.text


message=[]

st.set_page_config(page_title="Mental Health Support")
st.header("Check")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input_text=st.text_input("Input: ",key="input")

message.append({'role':'user',
                'parts':[input_text]})

submit=st.button("Enter")

if submit and input_text:
    response=get_gemini_response(message)
    st.session_state['chat_history'].append(("You",input_text))
    st.subheader("The Response is")
    st.write(response)
    st.session_state['chat_history'].append(("Bot",response))
    message.append({'role':'model',
                    'parts':[response]})

st.subheader("The chat History is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")

