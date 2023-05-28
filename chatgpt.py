import sys
import json
import requests
import openai

# Set OpenAI API key and organization
openai.api_key = sys.argv[1]
openai.organization = sys.argv[2]
print(openai.Model.list())

url = 'https://api.openai.com/v1/chat/completions'
# chatbot
print("Welcome to the chatgpt!")
prompt = ""
while True:
    prompt += input("You: ") + '\n'
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }
    
    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json"
    }
    
    r = requests.post(url, json=payload, headers=headers)
    
    try:
        res_json = json.loads(r.content.decode('utf-8'))
        res = res_json['choices'][0]['text']

        prompt += res+'\n'
        print("\n\nChatgpt: ")
        print(res)
        print("\n")
    except:
        print("error requests:", r.content.decode('utf-8'))
        break
    
