import tkinter as tk
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return 'Hello! How can I help you today?'
    elif 'your name' in user_input:
        return 'I am a simple AI Chatbot built using Python.'
    elif 'time' in user_input:
        return f'The current time is {datetime.now().strftime("%H:%M:%S")}'
    elif 'date' in user_input:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"
    elif 'bye' in user_input:
        return 'Goodbye! Have a great day.'
    else:
        return 'Sorry, I did not understand that. Please try again.'

def send_message():
    user_message = user_entry.get()
    if user_message.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_message + "\n")
    bot_reply = chatbot_response(user_message)
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_area.config(state=tk.DISABLED)

    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI Chatbot")
root.geometry("450x500")
root.resizable(False, False)

title = tk.Label(root, text="AI Chatbot", font=("Arial", 18, "bold"))
title.pack(pady=10)

chat_area = tk.Text(root, state=tk.DISABLED, width=52, height=20)
chat_area.pack(pady=10)

user_entry = tk.Entry(root, width=40, font=("Arial", 12))
user_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.pack(pady=5)

root.mainloop()
