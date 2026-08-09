import gradio as gr
from asr_engine import transcribe_multilingual_audio, SUPPORTED_TARGET_LANGUAGES

def process_audio_ui(audio_file, target_lang):
    if audio_file is None:
        return "N/A","Please upload or record an audio file."

    detected_lang, transcript = transcribe_multilingual_audio(audio_file, target_lang)
    return detected_lang, transcript

# Create Gradio Dashboard
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Multilingual ASR System
        Upload an audio file or record your voice to automatically detect the language and transcribe speech into text.
        """
    )

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(sources=["upload","microphone"], type="filepath", label="Upload/Record Audio")

            lang_dropdown = gr.Dropdown(
                choices=list(SUPPORTED_TARGET_LANGUAGES.keys()),
                value="Original Spoken Language",
                label="Target Output Language"
            )

            submit_btn = gr.Button("Transcribe & Translate", variant="primary")

        with gr.Column():
            lang_output = gr.Textbox(label="Primary Detected language")
            text_output = gr.Textbox(label="Timestamped Transcript / Translation",lines=12)

    submit_btn.click(
        fn=process_audio_ui,
        inputs=[audio_input, lang_dropdown],
        outputs=[lang_output,text_output]
    )

if __name__ == "__main__":
    demo.launch(share=True, theme=gr.themes.Soft())