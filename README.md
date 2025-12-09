# Gemini-chatbot
A fully functional chatbot using Google Gemini and Streamlit, with an additional Google Colab notebook for testing, exploration, and educational purposes.

🌟 Gemini Chatbot – Streamlit App + Google Colab Notebook

This repository contains two versions of a Gemini-powered chatbot:

✔ 1. A Streamlit App (production-ready chatbot)
✔ 2. A Google Colab Notebook (tutorial/demo version)
🚀 Features

Chat with Google's Gemini 2.5 models

Clean Streamlit UI

Environment-based API key loading

Colab notebook for experiments & teaching

📂 Repository Structure
gemini-chatbot/
├── mychatbot.py # Streamlit application
└── mychatbot.ipynb  # Google Colab notebook version
├── README.md
├── requirements.txt


▶️ Running the Streamlit App
Install dependencies
pip install -r requirements.txt

Set your GEMINI API key

Either as an environment variable:

export GEMINI_API_KEY="your_api_key_here"


or using a .env file (optional).

Start the app
streamlit run mychatbot.py

🧪 Running the Colab Notebook

Open the notebook from:

notebooks mychatbot.ipynb


Run each cell and add your API key inside Colab when prompted.
