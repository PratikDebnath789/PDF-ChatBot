🤖 IntelliDocs AI: Multimodal PDF Chatbot
IntelliDocs AI is a professional-grade document intelligence platform that allows users to have natural conversations with their PDF files. Unlike traditional text-only bots, this project leverages the Gemini 2.5 Flash engine to analyze text, complex charts, and images natively within documents.

📌 About the Project
This project solves the problem of "information overload" by allowing users to instantly extract specific data from long documents. It eliminates the need for manual searching by providing a conversational interface for PDFs.

Context-Aware: Remembers the document content throughout the session.

Vision-Enabled: Understands diagrams, tables, and images.

High Speed: Optimized for near-instant responses using Google's latest Flash models.

✨ Features

Multimodal Analysis: Not just text! Ask questions about graphs, charts, and images inside your PDFs.

Secure API Handling: Uses environment variables to keep your Google AI credentials safe.

Interactive UI: A clean, dark-mode "SaaS-style" dashboard built with Streamlit.

Session Memory: Keeps track of your conversation history for a seamless chat experience.

🗂 Project Structure

Plaintext
PDFChatbot/
│
├── app/
│   ├── app.py          # Main Streamlit application & AI logic
│   └── .env            # Private API keys (not uploaded to GitHub)
├── data/               # Sample PDFs for testing
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🧰 Technologies Used

Python 3.13+

Streamlit: Frontend UI framework.

Google GenAI SDK: For accessing Gemini 2.5 Flash.

PyPDF2: For initial PDF structure handling.

Python-Dotenv: For secure environment variable management.

⚙️ Installation

Clone the repository:

Bash
git clone https://github.com/your-username/PDFChatbot.git
cd PDFChatbot
Set up your API Key:
Create a file named .env in the app/ folder and add your Google API Key:

Plaintext
GOOGLE_API_KEY=your_actual_api_key_here


3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
▶️ Usage

Run the application using Streamlit:

Bash
python -m streamlit run app/app.py
📈 Backend Logic (RAG)
The project uses a Long-Context RAG (Retrieval-Augmented Generation) approach. Instead of traditional chunking, it utilizes Gemini's massive 1-million+ token window to process the entire document as a single context block, ensuring higher accuracy and better understanding of document-wide themes.

🚀 Future Improvements

Multi-File Support: Analyze dozens of PDFs simultaneously.

Export Chat: Save the AI's analysis as a new PDF or Text file.

Cloud Deployment: Host the app on Streamlit Cloud or AWS.

