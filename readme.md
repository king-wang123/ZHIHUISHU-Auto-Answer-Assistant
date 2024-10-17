# 🌟 智慧树自动答题助手

## 📝 项目简介

这是一个基于大语言模型（Large Language Models, LLM）的智慧树自动答题脚本，旨在帮助用户快速、准确地完成智慧树平台上的自动答题任务。本项目通过全自动答题的方式，无需题库，利用 LLM 的强大能力，多次生成答案以确保答案的准确性，能够极大地解放的生产力。

## 🌈 项目展示

<video controls width="320" height="240">
  <source src="./data/auto_answer_zhihuishu.mp4" type="video/mp4">
</video>

## 🚀 功能特点

- **全自动答题**：无需人工干预，自动完成答题过程。
- **准确性保障**：通过多次生成答案，提高答案的准确性。
- **易于使用**：只要你的电脑安装了 Python 环境，注册了对应大模型 API，并安装了必要的库，就可以直接运行脚本。
- **学习价值**：对于想要学习 Python 爬虫或自动化脚本以及大模型使用的同学，这是一个极好的练手项目。

## 🐞 已知问题与优化方向

- **OCR 识别**：当前项目需要调用 OCR 库来识别题目，这可能会影响效率。我们计划使用 Selenium 直接分析题目，以提高效率。
- **答题准确率**：由于依赖大模型，答题准确率可能会受到影响。我们将持续优化大模型的输出，以提高准确性。
- **增加支持的大模型**: 目前项目只支持智谱大模型，我们计划增加其他大模型的支持。

## 🛠️ 安装与使用

### 环境要求

- 确保你的电脑安装了 Python。
- 注册并获取 API-Key, 本项目目前只支持[智谱大模型](https://open.bigmodel.cn/console/overview)

### 安装步骤

1. 克隆项目到本地：

   ```bash
   git clone https://github.com/jason-king123/ZHIHUISHU-Auto-Answer-Assistant.git
   cd ZHIHUISHU-Auto-Answer-Assistant
   ```

2. 安装依赖库：

   ```bash
   pip install -r requirements.txt
   ```

3. 运行脚本：
   ```bash
   python main.py
   ```

## 📝 使用说明

- 运行脚本后，根据提示输入智慧树平台的账号信息。
- 脚本将自动登录并开始答题过程。
- 答题完成后，脚本会显示答题结果。

## 🤝 贡献与反馈

- 如果在使用过程中遇到任何问题，欢迎在项目的[Issues](https://github.com/yourusername/ZHIHUISHU-Auto-Answer-Assistant/issues)页面提出。
- 我们非常欢迎对代码的贡献，可以通过[Pull Requests](https://github.com/yourusername/ZHIHUISHU-Auto-Answer-Assistant/pulls)提交你的改进。
- 如果你觉得这个项目对你有帮助，欢迎点个 Star 支持一下！

---

🌈 希望这份 README 能够帮助你更好地展示和使用你的智慧树自动答题系统项目！如果有任何需要调整的地方，请随时告诉我。🚀🌟
