import google.generativeai as genai
import streamlit as st

with open(rf"C:\Users\Dell\OneDrive\Desktop\chatbot.txt") as file:
    key = file.read()

genai.configure(api_key = key)

system_prompt = ''' You are an expert in GenAI upto very recent trends.
Helps answering users queries in very concise and informative way.
'''

model = genai.GenerativeModel('models/gemini-2.5-flash-lite', system_instruction = system_prompt)

st.title('My Chatbot')
st.write('Type your message below to chat with the model')

# Initialize chat session
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

if 'messages' not in st.session_state:
    st.session_state.messages = []

for role, text in st.session_state.messages:
    if role == 'user':
        st.markdown(f'User: {text}')
    else:
        st.markdown(f'Bot: {text}')

user_input = st.chat_input('Type your message here')

if user_input:
    st.session_state.messages.append(('user', user_input))
    response = st.session_state.chat.send_message(user_input)
    st.session_state.messages.append(('Bot', response.text))
    st.rerun()
