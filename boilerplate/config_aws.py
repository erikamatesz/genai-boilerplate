import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_REGION_BEDROCK = "us-west-2"
AWS_MODEL_ID = "MODEL ID HERE"

MAX_TOKENS = 1000
TEMPERATURE = 0.9
TOP_P = 0.7