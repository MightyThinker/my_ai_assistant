
# 🤖 AI Voice Assistant (Offline + Online Hybrid)

This is a voice-controlled AI assistant built using **Python**, that can run with both cloud (OpenAI) and local (Ollama) LLMs. It listens to your voice, processes your commands, and responds with voice, switching automatically between online and offline models depending on availability.

---

## ✅ Features

- 🎙️ Accepts voice input via microphone
- 🧠 Processes input using LLM (OpenAI or Ollama)
- 🔁 Automatically switches between online/offline models
- 🗣️ Speaks responses using pyttsx3
- 📡 Uses .env for API keys and settings
- 📜 Logs all activity using a centralized logger

---

## 🧰 Hardware & Software Requirements

### 🖥️ System Requirements
- OS: Windows 10/11, macOS, or Linux
- RAM: 8 GB minimum (16 GB recommended for local models)
- Microphone and audio output device (headset/speakers)

### 🧪 Software Requirements
- Python 3.10+
- pip
- Internet connection (for OpenAI mode)
- Ollama (for local model)

---

## ⚙️ Setup Instructions

### 1. 🐍 Install Python
- Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Ensure "Add Python to PATH" is checked during installation.
- Verify:
  ```bash
  python --version
  ```

### 2. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. 🔐 Configure `.env`
Create a `.env` file at the root with:
```env
OPENAI_API_KEY=your_openai_key
LLM_MODE=auto              # auto | openai | local
OLLAMA_MODEL_NAME=mistral  # e.g., mistral, gemma
OLLAMA_BASE_URL=http://localhost:11434
```

---

### 4. ☁️ Setup OpenAI
- Get your API key from: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
- Paste it in `.env` under `OPENAI_API_KEY`

---

### 5. 🧠 Setup Ollama (for local LLM)

#### ✅ Windows
- Download: [https://ollama.com/download/windows](https://ollama.com/download/windows)
- Run `OllamaSetup.exe` and follow instructions.

#### ✅ macOS (Homebrew)
```bash
brew install ollama
```

#### ✅ Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### 📦 Pull a Model
```bash
ollama pull mistral
```

#### ▶️ Start Ollama
```bash
ollama serve
```

---

## 🚀 How to Run

```bash
python main.py
```

🎤 Speak your question.  
🛑 Say `exit`, `quit`, or `stop` to close the assistant.

---

## 📁 Project Structure

```
my_ai_assistant/
├── main.py                         # Main app loop
├── requirements.txt
├── .env                            # Configuration
├── logger_config.py                # Logger setup
├── my_io/
│   ├── speech_to_text.py
│   └── text_to_speech.py
├── my_brain/
│   ├── basic_brain.py
│   ├── llm_wrapper.py
│   ├── ai_openai.py
│   └── ai_ollama.py
```

---

## 🔁 LLM Switching Logic

- If `LLM_MODE=auto`:
  - Uses **OpenAI** if internet is available
  - Falls back to **Ollama** if offline or OpenAI fails
- You can manually force `LLM_MODE=local` or `LLM_MODE=openai` in `.env` to use a specific model.

---

## 📝 Logs

All logs (info, errors, speech recognition issues, etc.) are saved using a shared `logger` configuration.

---

## 👤 Author

**Pratyush Kumar**  
🔗 [LinkedIn](https://www.linkedin.com/in/mighty-thinker)  
💻 [GitHub](https://github.com/MightyThinker)

---

## 📃 License

MIT License – Free for personal and commercial use.
