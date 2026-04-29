# 🤖 IntelliDocs AI: Multimodal PDF Chatbot

**IntelliDocs AI** is a professional-grade document intelligence platform that allows users to have natural conversations with their PDF files. Unlike traditional text-only bots, this project leverages the **Gemini 2.5 Flash** engine to analyze text, complex charts, and images natively within documents.

---

### 📌 About the Project
This project solves the problem of "information overload" by allowing users to instantly extract specific data from long documents. It eliminates the need for manual searching by providing a conversational interface for PDFs.

*   **Context-Aware**: Remembers the document content throughout the session.
*   **Vision-Enabled**: Understands diagrams, tables, and images.
*   **High Speed**: Optimized for near-instant responses using Google's latest Flash models.

---

### ✨ Features
*   **Multimodal Analysis**: Not just text! Ask questions about graphs, charts, and images inside your PDFs.
*   **Secure API Handling**: Uses environment variables to keep your Google AI credentials safe.
*   **Interactive UI**: A clean, dark-mode "SaaS-style" dashboard built with Streamlit.
*   **Session Memory**: Keeps track of your conversation history for a seamless chat experience.

---

### 🗂 Project Structure
```text
PDFChatbot/
│
├── app/
│   ├── app.py          # Main Streamlit application & AI logic
│   └── .env            # Private API keys (Hidden from GitHub)
├── data/               # Sample PDFs for testing
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
