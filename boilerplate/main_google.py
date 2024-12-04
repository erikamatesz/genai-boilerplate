import google.generativeai as genai
from utils.prompt_manager import PromptManager
from config import *

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": TEMPERATURE,
  "top_p": TOP_P,
  "top_k": TOP_K,
  "max_output_tokens": MAX_OUTPUT_TOKENS,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name=MODEL_NAME,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[]
)

prompt_manager = PromptManager('src/prompts')

prompt = prompt_manager.generate_prompt(
    "persona", 
    role="software engineer", 
    expertise="backend development", 
    request="Explain how to implement a RESTful API."
)

print(prompt)

response = chat_session.send_message(prompt)

print(response.text)