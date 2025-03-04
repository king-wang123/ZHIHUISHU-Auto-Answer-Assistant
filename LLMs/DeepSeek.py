import requests
import json
from openai import OpenAI


class DeepSeekModel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model_name = 'deepseek-chat'
        self.url = 'https://api.deepseek.com'
        self.client = OpenAI(api_key=self.api_key, base_url=self.url)

    def get_response(self, query):
        messages = [
                {"role": "user", "content": query}
            ]
        completion = self.client.chat.completions.create(
            model = self.model_name,
            messages = messages,
            temperature = 0.7,
            timeout = 60
        )
        return completion.choices[0].message.content


# model = DeepSeekModel(api_key='')

# response = model.get_response("你好，请问你是谁，你可以怎么帮助我呢？")
# print(response)
