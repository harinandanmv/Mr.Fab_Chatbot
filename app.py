import os
import gradio
from groq import Groq

client = Groq(api_key=os.getenv("API_KEY"))

messages_prmt = [
    {
        "role": "system",
        "content": "You are a skilled sports analyst with a successful track record in football related news. Your role is to assist people by providing guidance on various football records, matches, player data etc."
    }
]

def customLLMBot(user_input, history):
    global messages_prmt
    messages_prmt.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})
    return LLM_reply

iface = gradio.ChatInterface(
    customLLMBot,
    chatbot=gradio.Chatbot(height=500),
    textbox=gradio.Textbox(placeholder="Ask me a question related to football"),
    title="Mr.Fab ChatBot",
    description="Hi! I’m Mr. Fab 🤖⚽ — your go-to chatbot for football rules, player stats, and match insights!",
    theme="soft",
    examples=["Hiii", "What is football", "What is offside"],
    submit_btn=True
)

iface.launch()
