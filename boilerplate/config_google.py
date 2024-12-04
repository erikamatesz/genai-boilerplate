import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

TEMPERATURE = 1.0
TOP_P = 0.95
TOP_K = 40
MAX_OUTPUT_TOKENS = 8192
MODEL_NAME = "MODEL NAME HERE"