import openai

openai.api_key = "provide your key"

messages = []

while True:
    user_input = input("Enter a theme: ")
    message = f'Generate 5 titles of article for {user_input}.'
    
    # Generate 5 titles
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply1 = chat.choices[0].message.content
    print(f"ChatGPT: {reply1}")
    messages.append({"role":"assistant", "content": reply1})
    
    # Generate agenda for every title
    messages.append({"role":"user", "content":f"Make agenda for every article {reply1}."})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply2 = chat.choices[0].message.content
    print(f"ChatGPT: {reply2}")
    messages.append({"role":"assistant", "content": reply2})
    
    # Write agenda to file
    with open('generated_paragraph.html', 'w') as f:
        f.write(f"<h1>{reply2}\n</h1>\n\n\n")
    
    # Generate paragraph for every provided agenda
    with open('generated_paragraph.html', 'r') as f:
        for line in f:
            if line.startswith("-"):
                agenda_item = line.strip()
                messages.append({"role": "user", "content": f"Write a paragraph about {line}."})
                chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                reply3 = chat.choices[0].message.content
                print(f"ChatGPT: {reply3}")
                messages.append({"role": "assistant", "content": reply3})
                # Write paragraphs to file
                with open('generated_paragraph.html', 'a') as file:
                    file.write(f"<h2>{agenda_item}</h2>\n")
                    file.write(f"<h3>{reply3}</h3>\n\n\n")
                messages.pop() # Remove last message to avoid exceeding context length
    messages.clear() # Clear messages list after each iteration
    break
