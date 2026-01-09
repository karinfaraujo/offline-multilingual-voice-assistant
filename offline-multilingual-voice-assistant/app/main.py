from audio_recorder import record_audio
from speech_to_text import transcribe_audio
from llm import ask_llm
from text_to_speech import speak

def main():
    print("🎤 Recording...")
    audio_path = record_audio()

    print("🧠 Transcribing...")
    text = transcribe_audio(audio_path)
    print(f"User said: {text}")

    print("💬 Thinking...")
    answer = ask_llm(text)
    print(f"Assistant: {answer}")

    print("🔊 Speaking...")
    speak(answer)

if __name__ == "__main__":
    main()
