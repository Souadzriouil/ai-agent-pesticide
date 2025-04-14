import os
from dotenv import load_dotenv

load_dotenv()

# Configuration de l'API Google (SerpAPI)
SERP_API_KEY = os.getenv('SERP_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configuration des logs
LOGGING_LEVEL = "INFO"
