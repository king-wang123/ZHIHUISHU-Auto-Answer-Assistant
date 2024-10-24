from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GLM import ChatGLMModel
from cnocr import CnOcr
import time
import random
import logging

# 设置日志级别为WARNING，这样ERROR级别的日志将不会被打印
logging.getLogger('selenium').setLevel(logging.WARNING)

ocr = CnOcr()
api_key = input("请输入您的智普AI平台 api_key：")
model = ChatGLMModel(api_url="https://open.bigmodel.cn/api/paas/v4/chat/completions", api_key=api_key)

def error_handler(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"函数 {func.__name__} 发生错误: {e}")
                input("请修复错误并按回车键继续...")
    return wrapper

def get_driver(url):
    options = webdriver.ChromeOptions()
    # selenium尝试连接https网站时会报SSL handshake failed, 加上以下两行代码可以忽略证书错误
    options.add_argument('--ignore-certificate-errors')
    # 设置日志级别为3, 仅记录警告和错误
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(random.uniform(0.5, 2))
    return driver

def text_orc(image='question.png'):
    ocr_results = ocr.ocr(image)
    # 提取文本内容
    extracted_text = '\n'.join([item['text'] for item in ocr_results if item['text'].strip()])
    return extracted_text

def get_answer(question):
    prompt = f"""
请仔细阅读以下题目并思考分析，根据题目类型，严格按照以下要求作答：

选择题（单选）： 如果题目为单选题，请从选项中选择一个正确的答案，并仅输出该选项（A、B、C或D），不提供任何额外解释。
选择题（多选）： 如果题目为多选题，请选择所有正确的选项，并仅输出所有正确选项的字母，用','分隔（如A,C），按字母顺序排列，不提供任何额外解释。
判断题： 如果题目为判断题，请分析题目并仅输出 "对" 或 "错"，不提供任何额外解释。
请遵循以上规则直接给出你的答案。

题目：
{question}

你的答案："""
    answer_list = []
    index = 0
    while True:
        cur_answer = model.get_response([prompt])[0][0]
        print(f'大模型第{index+1}次输出：{cur_answer}')
        if cur_answer in answer_list:
            return cur_answer
        answer_list.append(cur_answer)
        index += 1

@error_handler
def answer(driver, index):
    question_element = driver.find_elements(By.XPATH, '//div[@class="examPaper_subject mt20"]')[index]
    question_element.screenshot('question.png')
    question_str = text_orc()
    print(f'第{index+1}题：{question_str}')

    answer = get_answer(question_str) # answer 形如'A'  或 'B,D' 或 '对' 
    print(f'最终答案：{answer}')

    # 判断题中对与错的顺序可能不一样
    if '对' in answer or '错' in answer: # 判断题
        answer_elements = question_element.find_elements(By.XPATH, './/div[@class="label clearfix"]')
        for answer_element in answer_elements:
            if answer_element.text.strip() in answer:
                answer_element.click()
                time.sleep(random.uniform(0.2, 0.5))
                break
                
    else: # 选择题
        answer_list = []
        if ',' in answer: # 多选题
            answer_list = [(ord(i)-ord('A')) for i in answer.split(',')]
        else: # 单选题
            answer_list = [(ord(answer)-ord('A'))]
        for answer in answer_list:
            question_element.find_elements(By.XPATH, './/div[@class="label clearfix"]')[answer].click()
            time.sleep(random.uniform(0.2, 0.5))

def auto_answer(driver):
    index = 0
    while True:
        answer(driver, index)
        # 下一题
        next_button = driver.find_elements(By.XPATH, '//button[@class="el-button el-button--primary is-plain"]')[-1]
        if next_button.text.strip() == '保存':
            # 提交作业
            submit_button = driver.find_element(By.XPATH, '//button[@class="el-button el-button--text btnStyleX btnStyleXSumit"]')
            submit_button.click()
            time.sleep(random.uniform(1, 2))
            # driver.switch_to.alert.accept()
            input("请手动完成提交后按回车继续...")
            # conform_button = driver.find_element(By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary"]')
            # conform_button.click()
            print("提交成功")
            return
        next_button.click()
        time.sleep(random.uniform(0.5, 1))
        index += 1

if __name__ == '__main__':
    # 2feb14563dc5588db13b1093690ab798.9QUuI93Fts6S22eD
    url = input("请输入题目链接：")
    driver = get_driver(url)
    input("请登录后按回车继续...")
    auto_answer(driver)
    input("请按任意键退出...")
    driver.quit()