import requests
import json

session = requests.Session()

class KimiModel:
    def __init__(self, topic_id):
        self.topic_id = topic_id
        self.headers = {
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'x-msh-device-id': '7376844345082903816',
            'X-Traffic-Id': 'co0oa9ucp7fctgveuro0',
            'sec-ch-ua-mobile': '?0',
            'Authorization': '', # 需要按照 readme 说明填充！
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'x-msh-platform': 'web',
            'x-msh-session-id': '1730154114080551306',
            'Referer': f'https://kimi.moonshot.cn/chat/{self.topic_id}',
            'R-Timezone': 'Asia/Shanghai',
            'sec-ch-ua-platform': '"Windows"',
        }

    def get_response(self, query):
        json_data = {
            'messages': [
                {
                    'role': 'user',
                    'content': query,
                },
            ],
            'use_search': False,
            'extend': {
                'sidebar': True,
            },
            'kimiplus_id': 'kimi',
            'use_research': False,
            'use_math': False,
            'refs': [],
            'refs_file': [],
        }
        response = requests.post(
            f'https://kimi.moonshot.cn/api/chat/{self.topic_id}/completion/stream',
            headers=self.headers,
            json=json_data,
        )
        response.encoding = 'utf-8'
        data = response.text.split('data: ')[1:]  # 使用分隔符提取所有的data块
        texts = []
        for item in data:
            try:
                json_data = json.loads(item.strip())  # 解析每个JSON字符串
                if 'event' in json_data and json_data['event'] == 'rename':
                    continue
                if 'text' in json_data:  # 如果有'text'字段
                    texts.append(json_data['text'])
            except json.JSONDecodeError:
                continue  # 跳过无法解析的部分

        return ''.join(texts)


# # Example usage:
# model = KimiModel(topic_id='')
# response = model.get_response("你好，请问有什么可以帮助您？")
# print(response)
