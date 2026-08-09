import whisper
from deep_translator import GoogleTranslator

#Load model once
print("Loading Whisper ASR model...")
model = whisper.load_model("large-v3-turbo")

SUPPORTED_TARGET_LANGUAGES = {
    "Original Spoken Language": "original",
    "English": "en",
    "Urdu": "ur",
    "Assamese": "as",
    "Bengali": "bn",
    "Bodo": "brx",      # Google Translate language code for Bodo
    "Dogri": "doi",     # Google Translate language code for Dogri
    "Gujarati": "gu",
    "Hindi": "hi",
    "Kannada": "kn",
    "Kashmiri": "ks",   # Google Translate language code for Kashmiri
    "Konkani": "gom",   # Goan Konkani
    "Maithili": "mai",  # Google Translate language code for Maithili
    "Malayalam": "ml",
    "Manipuri (Meitei)": "mni-Mtei",
    "Marathi": "mr",
    "Nepali": "ne",
    "Odia": "or",
    "Punjabi": "pa",
    "Sanskrit": "sa",
    "Santali": "sat",   # Google Translate language code for Santali
    "Sindhi": "sd",
    "Tamil": "ta",
    "Telugu": "te",
    "Arabic": "ar"

}

def transcribe_multilingual_audio(audio_path, target_language="Origianl Spoken Language"):
    """
    Transcribes audio, detects languages segment-by-segment, translates the output into the selected target language.
    """
    if not audio_path:
        return "No audio provided.",""

    if target_language == "English":
        print(f"Processing audio: {audio_path} | Using Whisper Direct Speech-to English Translation")
        result = model.transcribe(audio_path, task="translate")
    else:
        print(f"Processing audio: {audio_path} | Task: Transcribe({target_language})")
        result = model.transcribe(audio_path, task="transcribe")

    # Extract language detected and transcribed text
    overall_detected_language = result.get("language", "Unknown").upper()
    segments = result.get("segments",[])

    formatted_transcript = []

    for seg in segments:
        start_time = f"{int(seg['start'] // 60):02d}:{int(seg['start'] % 60):02d}"
        end_time = f"{int(seg['end'] // 60):02d}:{int(seg['end'] % 60):02d}"
        text = seg["text"].strip()

        # translate to chosen language if non-original and non-Whisper-native English
        if target_language not in ["Original Spoken Language", "English"]:
            target_code = SUPPORTED_TARGET_LANGUAGES.get(target_language, "en")
            try:
                text = GoogleTranslator(source='auto', target=target_code).translate(text)
            except Exception as e:
                print(f"Translation warning for segment: {e}")

        formatted_transcript.append(f"[{start_time} - {end_time}] {text}")

    final_text = "\n".join(formatted_transcript)
    return overall_detected_language, final_text
