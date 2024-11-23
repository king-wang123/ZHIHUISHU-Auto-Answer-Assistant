import requests
from tqdm import tqdm

class ChatGLMModel:
    def __init__(self, api_key, model_type='glm-4-plus'):
        self.api_url="https://open.bigmodel.cn/api/paas/v4/chat/completions"
        self.api_key = api_key
        self.model_type = model_type
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_response(self, query, max_new_tokens=2048, num_samples=1, temperature=0.7):
        payload = {
            'model': self.model_type,
            'messages': [{'role': 'user', 'content': query}],
            'max_tokens': max_new_tokens,
            'num_samples': num_samples,
            'temperature': temperature,
            'top_p': 0.95,
            'do_sample': True,
        }
        response = requests.post(self.api_url, json=payload, headers=self.headers)
        response_data = response.json()
        choices = response_data.get('choices', [])
        if len(choices) == 0:
            print(response_data)
        return choices[0]['message']['content']


# # Example usage:
# model = ChatGLMModel(api_key="")
# response = model.get_response(["Hello, who are you? Which is the big one between 1.9 and 1.11, and why?"])
# print(response)