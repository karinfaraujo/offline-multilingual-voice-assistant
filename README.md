# 🎙️ Offline Multilingual Voice Assistant

<p align="center">
  <img src="assets/demo.gif" width="800" alt="Offline Voice Assistant Demo"/>
</p>

<p align="center">
  <strong>Local-first • Privacy-friendly • Fully Offline Voice AI</strong>
</p>

---

## 🌍 Overview

**Offline Multilingual Voice Assistant** is a fully local, voice-based AI system that enables users to interact with a language model using **speech only**, without relying on any cloud APIs.

The assistant records user speech, transcribes it, generates a response using a **local Large Language Model**, and speaks the answer back — all **100% offline**, running entirely on the user's machine.

---

## ✨ Features

- 🎤 **Speech-to-Text (Offline)** using Faster-Whisper  
- 🧠 **Local Large Language Model** via Ollama  
- 🔊 **Text-to-Speech (Offline)** with Coqui TTS  
- 🌍 Multilingual-ready pipeline  
- 🔐 Privacy-first (no data leaves your machine)  
- 🧩 Modular, clean, and extensible architecture  

---

## 🏗️ System Architecture

```text
🎙️ User Voice
      ↓
🎤 Audio Recorder
      ↓
🧠 Speech-to-Text (Whisper)
      ↓
💬 Local LLM (Ollama)
      ↓
🔊 Text-to-Speech
      ↓
🗣️ Spoken Response

## 🧰 Tech Stack
| Layer            | Technology                |
| ---------------- | ------------------------- |
| Language         | Python 3.10               |
| Speech-to-Text   | Faster-Whisper            |
| Language Model   | Ollama (LLaMA 3.x)        |
| Text-to-Speech   | Coqui TTS                 |
| Audio Processing | SoundDevice, NumPy, SciPy |

## ▶️ Getting Started

1️⃣ Clone the repository
git clone https://github.com/your-username/offline-multilingual-voice-assistant.git
cd offline-multilingual-voice-assistant

2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install Ollama and a local model

Download Ollama from:
https://ollama.com

Pull a lightweight, CPU-friendly model:

ollama pull llama3.2:1b

5️⃣ Run the assistant
python app/main.py

Speak into your microphone and wait for the spoken response.

## 🔐 Why Offline?

- Most voice assistants rely on cloud APIs, which introduce:

- High latency

- Privacy concerns

- Usage limits

- API costs

This project explores a local-first AI approach, making it ideal for environments where privacy, control, and offline availability are essential.

## ♿ Accessibility & Use Cases

- Voice-based interfaces for visually impaired users

- Assistants in offline or restricted environments

- Foundations for avatars and sign-language systems

- Edge AI and smart device applications

- Educational demonstrations of AI pipelines

## 🔮 Future Improvements

-Streaming responses to reduce perceived latency

-Automatic language detection

-Wake-word activation

-GUI or web-based interface

-Conversation memory and context

## 👩‍💻 Author

Developed by Karin Araujo
Focused on data, AI, and applied machine learning projects.
