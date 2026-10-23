import ollama
import streamlit
print(f"ollama当前可用的模型有：{ollama.list()}")
print(f"streamlitlist库版本是：{streamlit.__version__}")