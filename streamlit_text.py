import time

import streamlit as st
#标题
st.title("Streamlit教程")

#段落
st.write("hello")

#分割线
st.divider()

#聊天输入框
name=st.chat_input('请输入您的名字：')
if name:
	st.write(f"你好{name}")
#消息容器
st.chat_message('user').markdown('hello')

#等待提示框
with st.spinner("思考中..."):
	time.sleep(5)
	st.write("思考完成")