import requests

API_URL = "https://api-inference.huggingface.co/models/openai-gpt"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})
