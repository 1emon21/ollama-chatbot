import ollama


#获得ollamaclient的客户端对象
client =ollama.Client(host="http://localhost:11434")

#list列出哪些可用的模型
print(client.list())
#show显示指定模型的详细信息
print(client.show('deepseek-r1:7b'))
#ps显示当前正在运行的模型
print(client.ps())
#chat与模型进行对话
while True:
    str=input("请输入您的需求\n")
    response=client.chat(model='deepseek-r1:7b',messages=[{
        'role':'user','content':str
    }])
    print(response['message']['content'])