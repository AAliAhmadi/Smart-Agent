# 🤖 Smart AI Agent (Gemma3 + Web Tools)

An intelligent Streamlit-based assistant that runs **Gemma3:4b** locally via Ollama and automatically switches between:

- 🌐 **Online mode:** Uses Wikipedia + DuckDuckGo search for live data.
- 📴 **Offline mode:** Uses Gemma3:4b alone (with a warning about outdated info).

---

## 🚀 Features

- 🧠 Local reasoning via **Gemma3:4b**
- 🌐 Web search via **Wikipedia** and **DuckDuckGo**
- 💬 Chat memory across turns
- 🧹 "Clear Chat" button
- ⚙️ Clean modular structure for maintainability

---

## 🧱 Project Structure

```
app/
├── main.py # Streamlit app
├── agent_logic.py # Main agent logic (ReAct + fallback)
├── prompts.py # Prompt templates
├── utils.py # Internet check helper
└── init.py
requirements.txt
README.md
```





## 🧩 Installation (Local)

### 1️⃣ Install Ollama
Install [Ollama](https://ollama.com/download) and pull Gemma:

```bash
ollama pull gemma3:4b


### 2️⃣ Clone the repository
```bash
git clone https://github.com/AAliAhmadi/smart-agent.git
cd smart-agent

### 3️⃣ Set up environment
```bash
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

### 4️⃣ Run locally
```bash
streamlit run app/main.py


## 🧠 Usage

Run the app and start chatting:

Ask factual or reasoning-based questions.

If internet is available, the agent searches online.

If not, it answers locally but notes that info might be outdated.

Use the 🗑️ Clear Chat History button to reset the conversation.



## Acknowledgement
🙏 This project was inspired by the lectures of Bharath Thippireddy.



## 📄 License

MIT License © 2025 AAli Ahmadi

✅ **Summary of Improvements**
- Cleaner modular structure (`main`, `logic`, `prompts`, `utils`)
- Visible chat history  
- “🗑️ Clear Chat History” button  
- Ready for both **local** (Gemma) and **cloud** (GPT/OpenAI) modes  
- Updated, professional README  

---

Would you like me to make a **Streamlit Cloud–compatible variant** (automatically detects if Ollama is missing, and uses GPT-4o instead)? It’ll run both locally *and* in the cloud with no edits.


