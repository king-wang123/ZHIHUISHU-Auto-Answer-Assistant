from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cnocr import CnOcr
from GLM import ChatGLMModel
import time
import random
import logging

# 设置日志级别为WARNING，这样ERROR级别的日志将不会被打印
logging.getLogger('selenium').setLevel(logging.WARNING)

ocr = CnOcr()
# 2feb14563dc5588db13b1093690ab798.9QUuI93Fts6S22eD
api_key = input("请输入您的智普AI平台 api_key：")
model = ChatGLMModel(api_url="https://open.bigmodel.cn/api/paas/v4/chat/completions", api_key=api_key)

def get_driver(url):
    options = webdriver.ChromeOptions()
    # selenium尝试连接https网站时会报SSL handshake failed, 加上以下两行代码可以忽略证书错误
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(random.uniform(0.5, 2))
    return driver

def get_test_num(driver):
    test_list = driver.find_elements(By.XPATH, '//div[@id="examBox"]/div/ul/li')
    return len(test_list)

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
    return model.get_response([prompt])[0][0]


    
# 进入测试页面之后开始自动答题
def auto_answer_test(driver):
    while True:
        question_element = driver.find_element(By.XPATH, '//div[@class="examPaper_subject mt20"]')
        question_element.screenshot('question.png')
        question = text_orc()
        print("题目：{}".format(question))
        alphabet2num = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        answer = get_answer(question) # answer 形如'A'  或 'B,D' 或 '对' 

        # 这里判断题单独处理是因为题目中对与错的顺序可能不一样
        if '对' in answer or '错' in answer: # 判断题
            pass
        else: # 选择题
            answer_list = []
            if ',' in answer: # 多选题
                answer_list = [alphabet2num[i] for i in answer.split(',')]
            else: # 单选题
                answer_list = [alphabet2num[answer]]
        # 下一题
        next_button = driver.find_elements(By.XPATH, '//button[@class="el-button el-button--primary is-plain"]')[-1]
        next_button.click()
        time.sleep(random.uniform(1, 3))
        if next_button.text.strip() == '保存':
            # 提交作业
            submit_button = driver.find_element(By.XPATH, '//button[@class="el-button el-button--text btnStyleX btnStyleXSumit"]')
            submit_button.click()
            time.sleep(random.uniform(1, 3))
            print("提交成功")
            return



# 做第一个测试
def start_answer(driver):
    todo_test = driver.find_element(By.XPATH, '//div[@id="examBox"]/div/ul/li')
    start_button = todo_test.find_element(By.XPATH, './/a[@title="开始答题"]')
    start_button.click()
    print("开始答题")
    time.sleep(random.uniform(1, 3))
    # 获取所有窗口的句柄
    window_handles = driver.window_handles
    # 切换到新的窗口
    driver.switch_to.window(window_handles[-1])
    auto_answer_test(driver)

# 按顺序自动做所有测试
def auto_answer_tests(driver):
    while True:
        test_num = get_test_num(driver)
        print("共有{}个测试待做".format(test_num))
        if test_num == 0:
            print("暂无可做的测试")
            return
        start_answer(driver)

def main(url):
    driver = get_driver(url)
    input("请登录后按回车继续...")
    auto_answer_tests(driver)
    driver.quit()

if __name__ == '__main__':
    # url = 'https://onlineexamh5new.zhihuishu.com/stuExamWeb.html#/webExamList?recruitId=HvvwUjKFpfPJ6AMd1GD5dA%3D%3D'
    # main(url)
    url = 'https://onlineexamh5new.zhihuishu.com/stuExamWeb.html#/webExamList?recruitId=HvvwUjKFpfPJ6AMd1GD5dA%3D%3D'
    driver = get_driver(url)
    input("请登录后按回车继续...")
    test_num = get_test_num(driver)
    print("共有{}个测试待做".format(test_num))
    if test_num == 0:
        print("暂无可做的测试")
    todo_test = driver.find_element(By.XPATH, '//div[@id="examBox"]/div/ul/li')
    start_button = todo_test.find_element(By.XPATH, './/a[@title="开始答题"]')
    start_button.click()
    print("开始答题")
    time.sleep(random.uniform(1, 3))
    # 获取所有窗口的句柄
    window_handles = driver.window_handles
    # 切换到新的窗口
    driver.switch_to.window(window_handles[-1])
    # 获取新页面的源代码
    new_page_source = driver.page_source
    # 保存网页代码
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(new_page_source)
    question_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="examPaper_subject mt20"]')))
    # question_element = driver.find_element(By.XPATH, '//div[contains(@class, "examPaper_subject")]')
    question_element.screenshot('question.png')
    # question = text_orc()
    # print("题目：{}".format(question))
    # alphabet2num = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    # answer = get_answer(question) # answer 形如'A'  或 'B,D' 或 '对' 
    # print(answer)

# class="examPaper_subject mt20"