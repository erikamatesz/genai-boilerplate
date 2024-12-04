import boto3
import json
from utils.prompt_manager import PromptManager
from config import *

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION_BEDROCK,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

prompt_manager = PromptManager('src/prompts')

prompt = prompt_manager.generate_prompt(
    "persona", 
    role="software engineer", 
    expertise="backend development", 
    request="Explain how to implement a RESTful API."
)

request_body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": MAX_TOKENS,
    "temperature": TEMPERATURE,
    "top_p": TOP_P,   
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]
}

request_body_json = json.dumps(request_body, ensure_ascii=False)

response = client.invoke_model(
    body=request_body_json.encode('utf-8'),
    modelId=AWS_MODEL_ID,
    accept="application/json", 
    contentType="application/json"
)

response_body = response['body'].read()

response_json = json.loads(response_body)

content = response_json['content'][0]['text']

print(content)
