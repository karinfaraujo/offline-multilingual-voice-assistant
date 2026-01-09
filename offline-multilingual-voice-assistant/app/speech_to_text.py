from faster_whisper import WhisperModel

MODEL_SIZE = "small"

def transcribe_audio(audio_path, language="en"):
    model = WhisperModel(MODEL_SIZE, device="cpu")
    segments, _ = model.transcribe(audio_path, language=language)

    text = " ".join([segment.text for segment in segments])
    return text
