# 🤖⚽ Mr. Fab Football Chatbot

## 🧩 Overview  
The **Mr. Fab Football Chatbot** is an intelligent and user-friendly web application designed to answer a wide range of football-related queries. Powered by **Groq's LLaMA 3 model** and built with **Python** and **Gradio**, this chatbot provides real-time, context-aware responses about players, matches, rules, and football records.

---

## ✨ Features  
- 💬 Ask about **football rules**, **match history**, or **player stats**  
- 🧠 Maintains **chat history** for contextual conversation  
- ⚙️ Uses **Groq’s blazing-fast LLaMA 3 API**  
- 🎨 Built with **Gradio** for a smooth, interactive chat interface  

---

## 🛠️ Tech Stack  
- 🐍 **Python** – Core programming language  
- 🧪 **Gradio** – Web UI framework for rapid prototyping  
- ⚡ **Groq API** – LLM backend using LLaMA 3  
- 🔒 **Environment Variables** – For secure API key handling  

---

## 🔌 API Integration – Groq  
The chatbot connects with [Groq's API](https://console.groq.com/) to fetch intelligent responses.

### 🔑 Steps to get your API Key:
1. Sign up at [Groq Console](https://console.groq.com/)
2. Create a new API key
3. Add it to your environment:
   ```bash
   export API_KEY=your_groq_api_key   # Linux/macOS  
   set API_KEY=your_groq_api_key      # Windows
````

---

## 📁 Project Structure

* mr-fab-chatbot/

  * 📄 `app.py` — Main script with chat logic
  * 📄 `requirements.txt` — Python packages required
  * 📄 `.gitignore` — Git ignored files
  * 📄 `README.md` — This file

---

## 🚀 How to Run the Project Locally

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/mr-fab-chatbot.git
cd mr-fab-chatbot
```

### 📦 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 Step 3: Set Your API Key

```bash
export API_KEY=your_groq_api_key   # or use .env method
```

### ▶️ Step 4: Launch the App

```bash
python app.py
```

You will see a local URL (e.g., [http://localhost:7860](http://localhost:7860)) — open it in your browser to start chatting with Mr. Fab!

---

## 🧠 Example Questions

* "What is the offside rule in football?"
* "Tell me about Lionel Messi’s career stats."

---

## 🙏 Acknowledgements

* 🚀 [Groq](https://groq.com/) for powering high-performance LLMs
* 🧪 [Gradio](https://gradio.app/) for providing easy UI building blocks
* 📚 Football data publicly available for educational use

---

## 📌 Note

This chatbot is educational and experimental. Do not use it for betting or critical decisions without verifying data from official sources.
