import streamlit as st
import ollama

# 创建标题
st.title("ollamma-chatbot")

# 初始化会话状态
if 'message' not in st.session_state:
    st.session_state['message'] = []

# 分割线
st.divider()

# 聊天输入框
user_input = st.chat_input("请输入你的问题：")

# 创建 Ollama 客户端对象
client = ollama.Client(host="http://localhost:11434")

# 用户消息处理
if user_input:
    # 存入用户对话的信息
    st.session_state['message'].append({'role': 'user', 'content': user_input})

    # 渲染所有历史消息
    for msg in st.session_state['message']:
        st.chat_message(msg['role']).markdown(msg['content'])

    # 机器人消息容器（带加载动画）
    with st.spinner("AI思考中..."):
        # 使用 chat 方法与大模型进行对话
        response = client.chat(
            model='qwen2.5:3b',
            messages=[{'role': 'user', 'content': user_input}]
        )
        # 提取 AI 回复内容
        reply_content = response['message']['content']

        # 把机器人的回答存入历史记录
        st.session_state['message'].append({'role': 'assistant', 'content': reply_content})

        # 把 AI 的回答渲染到界面中
        st.chat_message("assistant").markdown(reply_content)
       