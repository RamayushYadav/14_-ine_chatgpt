# 14 line code app
import streamlit as st
from langchain.llms import OpenAI
st.title("🦜🔗Quick Start App")
open_api_key = st.sidebar.text_input('Open API Key')
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, open_api_key=open_api_key)
    st.info(llm(input_text))
with st.form('My_form'):
    text = st.text_area('Enter text:', '...')
    submitted = st.form_submit_button('Submit')
    if not open_api_key.startswith('sk-'):
        st.warning('Please Enter Your OpenAI API Key!', icon='⚠')
    if submitted and open_api_key.startswith('sk-'):
        generate_response(text)
