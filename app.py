# app.py
import streamlit as st
from backend.file_handler import handle_file
from backend.query_handler import detect_intent
from backend.tool_invoker import invoke_tool
from backend.utils import log_history

st.set_page_config(page_title="Financial Chatbot", layout="wide")
st.title("📈 Financial Intelligence Chatbot")

uploaded_file = st.file_uploader("Upload a financial document (PDF, DOCX, CSV, Excel):")
query = st.text_input("Ask your question:")

if uploaded_file and query:
    with st.spinner("Processing..."):
        file_data = handle_file(uploaded_file)
        intent = detect_intent(query)
        response = invoke_tool(intent, file_data, query)
        log_history(query, response)
        st.success("Done")
        st.markdown("### ✉️ Response:")
        st.write(response)