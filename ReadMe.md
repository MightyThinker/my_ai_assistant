# 🤖 AI Voice Assistant (Local, Offline)

This is a step-by-step build of a personal voice assistant using **Python**, with plans to integrate **AI**, **automation**, and eventually hybrid usage with **Java**.

### ✅ Features (Step 1)
- 🎙️ Accepts voice input (speech recognition)
- 🧠 Processes the command (mock brain for now)
- 🗣️ Responds using voice (text-to-speech)

### 📁 Folder Structure
my_ai_assistant/<br/>
├── .gitignore<br/>
├── README.md<br/>
├── main.py<br/>
├── requirements.txt<br/>
├── io/<br/>
│ ├── speech_to_text.py<br/>
│ └── text_to_speech.py<br/>
├── brain/<br/>
│ └── basic_brain.py<br/>


### 🔧 How to Run

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
2. Run the assistant
    ```bash
    python main.py
3. Say anything, like:
    ```bash
    "Hello assistant"
    To stop, say: exit or quit