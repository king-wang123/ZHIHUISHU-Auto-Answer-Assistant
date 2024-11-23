from openai import OpenAI

class KimiModel:
    def __init__(self, api_key, model_type='moonshot-v1-8k'):
        self.api_key = api_key
        self.model_type = model_type

    def get_response(self, query):
        client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.moonshot.cn/v1",
        )
        completion = client.chat.completions.create(
            model=self.model_type,
            messages=[
                {"role": "system",
                "content": "你是Kimi，由Moonshot AI提供的人工智能助手，你更擅长中文和英文的对话。"},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
        )
        return completion.choices[0].message.content


# # Example usage:
# model = KimiModel(api_key="")
# response = model.get_response("你好，请问有什么可以帮助您？")
# print(response)
