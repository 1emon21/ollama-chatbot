# Ollama 聊天机器人

基于 Ollama 本地部署 + Streamlit 的聊天机器人，支持本地私有化运行大模型。

## 技术栈
- Python 3.x
- Ollama（Qwen2.5 3B 蒸馏模型）
- Streamlit

## 功能
- 本地私有化部署，数据不出本机
- 对话式交互界面
- 流式输出

## 运行步骤
1. 安装 Ollama 并拉取模型：`ollama pull qwen2.5:3b`
2. 安装依赖：`pip install streamlit ollama`
3. 启动：`streamlit run ollama-chatbot.py`

## 项目结构
- `ollama-chatbot.py` - 主程序
- `streamlit_text.py` - 界面测试脚本
- `ollama_text.py` - API 测试脚本
## 运行截图

![聊天机器人对话界面]
<img width="1365" height="1213" alt="chatbot" src="https://github.com/user-attachments/assets/c9dee747-53ef-42d7-9451-cd31b94b809c" />

![Ollama 拉取模型]
<img width="917" height="467" alt="ollama_pull" src="https://github.com/user-attachments/assets/775f6152-960b-440e-8221-87286784391f" />


![Streamlit 启动]
<img width="1731" height="607" alt="streamlit_start" src="https://github.com/user-attachments/assets/f45557a6-ec9e-4416-940a-a7c592707bc7" />
