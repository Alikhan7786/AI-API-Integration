# AI API Integration Project

## Project Description
This project demonstrates the integration of multiple Generative AI APIs using Python.  
It allows users to interact with different AI providers by entering prompts and receiving responses.

The following AI providers are implemented:
-> Groq
-> Ollama (Local Model)
-> Hugging Face
-> Google Gemini
-> Cohere


## Features
Multiple AI API integrations
User input-based prompt system
Error handling for API failures
Secure API key management using environment variables
Modular code structure (separate files for each API)



## Technologies Used
- Python
- REST APIs
- Generative AI Models
- VS Code



## Setup Instructions 

Clone the repository:
git clone https://github.com/username/repo-name cd ai-api-integration

Install required dependencies:
pip install -r requirements.txt

How to Obtain API Keys
Groq: https://console.groq.com Cohere: https://dashboard.cohere.ai/api-keys Google Gemini: https://makersuite.google.com/app/apikey HuggingFace: https://huggingface.co/settings/tokens Ollama does not require an API key (runs locally)

Set up API keys as environment variables:
For Windows (PowerShell):

$env:GROQ_API_KEY="your_api_key" $env:COHERE_API_KEY="your_api_key" $env:GOOGLE_API_KEY="your_api_key" $env:HUGGINGFACE_API_KEY="your_api_key"

Run any Python file:
python gemini_example.py python groq.py python huggingface.py python cohere.py python ollama.py