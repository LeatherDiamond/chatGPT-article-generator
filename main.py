import openai
import os
import json
from base64 import b64decode
from dotenv import load_dotenv

load_dotenv()

user_choice = input("Choose an option:\n1. Text Generation\n2. Image Generation\nEnter 1 or 2: ")

if user_choice == "1":
    openai.api_key = os.getenv("API_KEY")

    messages = []

    while True:
        user_input = input("Enter the topic: ")
        message = f'Generate 5 titles of article for {user_input}.'
        
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply1 = chat.choices[0].message.content
        print(f"ChatGPT: {reply1}")
        messages.append({"role":"assistant", "content": reply1})
        
        messages.append({"role":"user", "content":f"Make agenda for every article {reply1}."})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply2 = chat.choices[0].message.content
        print(f"ChatGPT: {reply2}")
        messages.append({"role":"assistant", "content": reply2})
        
        with open('generated_paragraph.html', 'w') as f:
            f.write(f"<h1>{reply2}\n</h1>\n\n\n")
        
        with open('generated_paragraph.html', 'r') as f:
            for line in f:
                if line.startswith("-"):
                    agenda_item = line.strip()
                    messages.append({"role": "user", "content": f"Write a paragraph about {line}."})
                    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                    reply3 = chat.choices[0].message.content
                    print(f"ChatGPT: {reply3}")
                    messages.append({"role": "assistant", "content": reply3})
                 
                    with open('generated_paragraph.html', 'a') as file:
                        file.write(f"<h2>{agenda_item}</h2>\n")
                        file.write(f"<h3>{reply3}</h3>\n\n\n")
                    messages.pop()
        messages.clear()
        break

elif user_choice == "2":
    prompt = input('Enter picture decription: ')
    openai.api_key = os.getenv('API_KEY')

    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='1024x1024',
    response_format='b64_json'
)

    with open('data.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    image_data = b64decode(response['data'][0]['b64_json'])
    file_name = '_'.join(prompt.split(' '))

    with open(f'{file_name}.png', 'wb') as file:
        file.write(image_data)
else:
    print("Invalid choice. Please enter 1 or 2.")
