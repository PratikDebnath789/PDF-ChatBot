import streamlit as st
import os
from google import genai
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# 1. LOAD API KEY
load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))
api_key = os.getenv("GOOGLE_API_KEY")

# 2. SAFETY CHECK & CLIENT INITIALIZATION
if api_key:
    # This is the new 2026 standard for initializing the Google AI Client
    client = genai.Client(api_key=api_key)
else:
    st.error("❌ API Key not found! Please ensure your file is named exactly '.env' and contains GOOGLE_API_KEY=your_key")
    st.stop()

# ==========================================
# 🎨 UI CONFIGURATION (DARK MODE)
# ==========================================
st.set_page_config(page_title="PDF AI Chatbot", page_icon="🤖")

st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    [data-testid="stSidebar"] { background-color: #161b22; }
    .stTextInput>div>div>input { background-color: #0d1117; color: white; border: 1px solid #30363d; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# ⚙️ BACKEND LOGIC
# ==========================================

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# ==========================================
# 🖥️ APP INTERFACE
# ==========================================

with st.sidebar:
    st.title("🤖 PDF Chatbot")
    uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True, type=['pdf'])
    
    if st.button("Process Documents"):
        if uploaded_files:
            with st.spinner("Reading PDF..."):
                raw_text = get_pdf_text(uploaded_files)
                st.session_state.context = raw_text
                st.success("PDF Loaded!")
        else:
            st.warning("Please upload a PDF first.")

st.title("💬 Chat with PDF")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# USER INPUT & AI RESPONSE
if user_input := st.chat_input("Ask about the PDF..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if "context" in st.session_state:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # NEW 2026 SYNTAX: Replacing old Line 77-85
                full_prompt = f"Context from PDF:\n{st.session_state.context}\n\nQuestion: {user_input}"
                
                # Using the Gemini 2.5 Flash model found in your available models list
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=full_prompt
                )
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    else:
        st.warning("Please upload a PDF and click 'Process' first.")
