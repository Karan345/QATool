##kt : Built with help from gemini as a quick llm project

import ollama
import sys

# 1. Read the local file
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        file_content = f.read()
except FileNotFoundError:
    print("Error: 'data.txt' not found. Please create it first.")
    sys.exit()

print(f"Loaded 'data.txt' ({len(file_content)} characters).")
print("Ask a question about your document (type 'exit' to quit):")
print("-" * 50)

# 2. Start the chat loop
conversation_history = []

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit']:
        break

    # 3. Construct the prompt with the document context
    # We send the document content ONLY in the first message to save tokens/time
    if not conversation_history:
        messages = [
            {'role': 'system', 'content': 'You are a helpful assistant. Answer questions based on the provided text.'},
            {'role': 'user', 'content': f"Here is the text to analyze:\n\n{file_content}\n\nQuestion: {user_input}"}
        ]
    else:
        # Append new question to history
        messages = conversation_history + [{'role': 'user', 'content': user_input}]

    print("Gemma: ", end="", flush=True)

    # 4. Call the model
    try:
        response_stream = ollama.chat(model='gemma3:1b', messages=messages, stream=True)
        
        full_response = ""
        for chunk in response_stream:
            text = chunk['message']['content']
            print(text, end="", flush=True)
            full_response += text
        
        print() # Newline after response

        # Update history
        conversation_history.append({'role': 'user', 'content': user_input})
        conversation_history.append({'role': 'assistant', 'content': full_response})

    except Exception as e:
        print(f"\nError communicating with model: {e}")