# model.py

class Model:
    def __init__(self, model_name, api_key):
        self.model_name = model_name
        self.api_key = api_key
        self.model = self._instantiate_model()

    def _instantiate_model(self):
        if self.model_name == 'Kimi':
            from LLMs.Kimi import KimiModel
            return KimiModel(self.api_key)
        elif self.model_name == 'ChatGLM':
            from LLMs.ChatGLM import ChatGLMModel
            return ChatGLMModel(self.api_key)
        else:
            raise ValueError(f"Unsupported model name: {self.model_name}")

    def get_response(self, query):
        return self.model.get_response(query)


def get_model():
    model_dict = {
        '1' : 'Kimi',
        '2' : 'ChatGLM'
    }
    while True:
        try:
            model_num = input("请输入模型编号：\n 1. Kimi\n 2. ChatGLM\n")
            assert model_num in model_dict.keys()
            model_name = model_dict[model_num]
            break
        except:
            print("输入错误，请重新输入！")

    api_key = input("请输入api_key：")
    return Model(model_name, api_key)

# # Example usage:
# model = Model('Kimi', 'sk-Jul9lPAlXAewurna49nRwlbJhCeIFLbXDxVNwGjguUoDPzzG')
# response = model.get_response('What is the capital of France?')
# print(response)