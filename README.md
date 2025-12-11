# Gemini-chatbot

MyChatbot is an expert Generative AI assistant built using Google’s Gemini 2.5 model. I created two complete versions of the chatbot: a Streamlit application that serves as the main interactive UI, and a Google Colab notebook designed for experimentation, testing, and educational use. The Streamlit app provides a smooth, production-ready chat interface powered by the Gemini API, while the notebook version allows users to explore how the chatbot works step-by-step. Together, they form a beginner-friendly yet powerful project demonstrating how to build a practical Generative AI chatbot from scratch.

Features:

Functional chatbot built with the Gemini API

Simple Streamlit interface

Google Colab notebook for experimentation and learning

Clean and beginner-friendly structure

Repository structure:

gemini-chatbot/

│

├── notebook/                 # Jupyter/Colab notebooks

│   └── mychatbot.ipynb       # Google Colab notebook version

│

├── src/                      # Source code directory

│   └── mychatbot.py          # Main Streamlit application

│

├── README.md                 # Project documentation

└── requirements.txt          # Python dependencies

Running the Streamlit App:

Install required packages:

pip install -r requirements.txt


Set your Gemini API key (from Google AI Studio):

export GEMINI_API_KEY="your_api_key"

Start the application:

streamlit run mychatbot.py

Running the Google Colab Notebook:

Open the file mychatbot.ipynb in Google Colab

Run all cells

Enter your Gemini API key when prompted

Use the notebook interface to chat with the model

Tech Stack:

Python

Streamlit

Google Gemini API

Google Colab
