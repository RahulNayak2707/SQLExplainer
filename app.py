from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as generativeai

# Configure API key
generativeai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Google Gemini
def get_gemini_response(question, prompt):
    model = generativeai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + question)
    return response.text

prompt = """
You are an excellent SQL teacher who explains SQL queries in simple language so that even a non-technical person can understand.
Provide detailed explanations and suggest alternative queries if the given query is incorrect.
"""

st.set_page_config(page_title="SQL Query Explainer")
st.header("Gemini App to Explain SQL Queries")

question = st.text_area("Enter your SQL query:", key='input', height=100)

if st.button("Explain the Query"):
    explanation = get_gemini_response(question, prompt)
    st.subheader('Explanation:')
    st.write(explanation)
