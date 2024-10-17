import requests
from tqdm import tqdm

class ChatGLMModel:
    def __init__(self, api_url, api_key, model_type='glm-4'):
        self.api_url = api_url
        self.api_key = api_key
        self.model_type = model_type
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_response(self, querys, max_new_tokens=2048, num_samples=1, temperature=0.7):
        all_response_ = []
        for qindex, query in tqdm(enumerate(querys), desc="Processing queries"):
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
            if response.status_code == 200:
                response_data = response.json()
                choices = response_data.get('choices', [])
                all_response_.append([choice['message']['content'] for choice in choices])
            else:
                print(f"Error: {response.status_code}, {response.text}")
        return all_response_

# # Example usage:
# model = ChatGLMModel(api_url="https://open.bigmodel.cn/api/paas/v4/chat/completions", api_key="2feb14563dc5588db13b1093690ab798.9QUuI93Fts6S22eD")
# response = model.get_response(["Hello, who are you? Which is the big one between 1.9 and 1.11, and why?"])
# print(response)