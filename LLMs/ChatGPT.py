import requests
import json

session = requests.Session()

class ChatGPTModel:
    def __init__(self, topic_id):
        self.topic_id = topic_id
        self.cookies = {
            'oai-did': '5c762c4f-2077-486f-b0b4-68a23b0bab8c',
            'oai-nav-state': '1',
            'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4Nzk2NywidXNlcl9uYW1lIjoiemxoX25ldSIsImlzcyI6IkNoYXRTaGFyZSIsImV4cCI6MTczNDYyNTUwOH0.W7Km99U_aRwVuIfguqSCAwgYThhOJVt71nieHQqupaE',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4Nzk2NywidXNlcl9uYW1lIjoiemxoX25ldSIsImlzcyI6IkNoYXRTaGFyZSIsImV4cCI6MTczNDYyNTUwOH0.W7Km99U_aRwVuIfguqSCAwgYThhOJVt71nieHQqupaE',
            'gfsessionid': 'b8c45323-6306-4b8d-b4e9-3211de25f171',
            '_dd_s': 'logs=1&id=a7444baf-2b24-4c89-8e37-75109d87e166&created=1734065770862&expire=1734066893923',
        }
        self.headers = {
            'accept': 'text/event-stream',
            'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
            'authorization': 'Bearer NwCRJvFh9cH',
            'content-type': 'application/json',
            # 'cookie': 'oai-did=5c762c4f-2077-486f-b0b4-68a23b0bab8c; oai-nav-state=1; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4Nzk2NywidXNlcl9uYW1lIjoiemxoX25ldSIsImlzcyI6IkNoYXRTaGFyZSIsImV4cCI6MTczNDYyNTUwOH0.W7Km99U_aRwVuIfguqSCAwgYThhOJVt71nieHQqupaE; authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4Nzk2NywidXNlcl9uYW1lIjoiemxoX25ldSIsImlzcyI6IkNoYXRTaGFyZSIsImV4cCI6MTczNDYyNTUwOH0.W7Km99U_aRwVuIfguqSCAwgYThhOJVt71nieHQqupaE; gfsessionid=b8c45323-6306-4b8d-b4e9-3211de25f171; _dd_s=logs=1&id=a7444baf-2b24-4c89-8e37-75109d87e166&created=1734065770862&expire=1734066893923',
            'oai-device-id': '5c762c4f-2077-486f-b0b4-68a23b0bab8c',
            'oai-echo-logs': '0,196702,1,196703,0,197091,3,197810,1,198689,0,198701,1,199842,0,219870,3,220864,1,222049',
            'oai-language': 'en-US',
            'openai-sentinel-chat-requirements-token': '57c7fada-97f1-40d3-86d3-dc6689268089',
            'origin': 'https://gpt-node1.chatshare.biz',
            'priority': 'u=1, i',
            'referer': 'https://gpt-node1.chatshare.biz/c/675bbf31-e274-800f-b64f-33afc06886bb',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

    def get_response(self, query):
        json_data = {
            'action': 'next',
            'messages': [
                {
                    'id': 'aaa258fe-012b-4ad3-a3b0-ada50fecbeec',
                    'author': {
                        'role': 'user',
                    },
                    'content': {
                        'content_type': 'text',
                        'parts': [
                            query,
                        ],
                    },
                    'metadata': {
                        'serialization_metadata': {
                            'custom_symbol_offsets': [],
                        },
                    },
                    'create_time': 1734065993.925,
                },
            ],
            'conversation_id': '675bbf31-e274-800f-b64f-33afc06886bb',
            'parent_message_id': '18faec84-4f04-41cd-8640-93e3a9855d09',
            'model': 'gpt-4o',
            'timezone_offset_min': -480,
            'timezone': 'Asia/Shanghai',
            'suggestions': [],
            'history_and_training_disabled': False,
            'conversation_mode': {
                'kind': 'primary_assistant',
            },
            'force_paragen': False,
            'force_paragen_model_slug': '',
            'force_rate_limit': False,
            'reset_rate_limits': False,
            'websocket_request_id': 'e26516e4-99b1-4c4c-8f49-3e7664ce7d60',
            'system_hints': [],
            'force_use_sse': True,
            'supported_encodings': [],
            'conversation_origin': None,
            'client_contextual_info': {
                'is_dark_mode': False,
                'time_since_loaded': 224,
                'page_height': 721,
                'page_width': 1278,
                'pixel_ratio': 1.5,
                'screen_height': 1440,
                'screen_width': 2560,
            },
        }

        response = requests.post(
            'https://gpt-node1.chatshare.biz/backend-api/conversation',
            cookies=self.cookies,
            headers=self.headers,
            json=json_data,
        )
        response.encoding = 'utf-8'
        with open('response.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
        data = response.text.replace('event: delta', '')
        data = data.split('data: ')[1:]  # 使用分隔符提取所有的data块
        data = [item.strip() for item in data]  # 去掉每一行的前后空格
        texts = []
        for item in data:
            try:
                json_data = json.loads(item.strip())  # 解析每个JSON字符串
                if 'p' in json_data:
                    continue
                if 'v' in json_data:  # 如果有'text'字段
                    if type(json_data['v']) != str:  # 如果'v'字段不是字符串
                        continue
                    texts.append(json_data['v'])
            except:
                continue  # 跳过无法解析的部分

        return ''.join(texts)


# # Example usage:
# model = KimiModel(topic_id='')
# response = model.get_response("你好，请问有什么可以帮助您？")
# print(response)
