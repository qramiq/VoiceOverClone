import os
import sys
import platform

# Check for Python 3.11 specifically
if not (sys.version_info.major == 3 and sys.version_info.minor == 11):
    print("ERROR: This application requires Python 3.11 specifically.")
    print(f"Current Python version: {platform.python_version()}")
    print("Please install Python 3.11 from https://www.python.org/downloads/release/python-3118/")
    sys.exit(1)

import torch
import gradio as gr
import torchaudio
from chatterbox.tts import ChatterboxTTS

# Initialize the model
def initialize_model(device="cuda" if torch.cuda.is_available() else "cpu"):
    model = ChatterboxTTS.from_pretrained(device=device)
    return model

# Generate speech from text
def generate_speech(text, audio_prompt_path=None, exaggeration=0.5, temperature=0.7, cfg_weight=0.5, seed=None):
    model = initialize_model()
    
    if seed is not None:
        seed = int(seed)
    
    if audio_prompt_path:
        wav = model.generate(
            text, 
            audio_prompt_path=audio_prompt_path,
            exaggeration=exaggeration,
            temperature=temperature,
            cfg_weight=cfg_weight,
            seed=seed
        )
    else:
        wav = model.generate(
            text,
            exaggeration=exaggeration,
            temperature=temperature,
            cfg_weight=cfg_weight,
            seed=seed
        )
    
    output_path = "output.wav"
    torchaudio.save(output_path, wav, model.sr)
    return output_path

# Create the Gradio interface
def create_ui():
    with gr.Blocks(title="Chatterbox Voice Cloning") as app:
        gr.Markdown("# Chatterbox Voice Cloning")
        gr.Markdown("### High-fidelity voice cloning for streamer chat TTS and more")
        
        with gr.Tab("Text-to-Speech"):
            with gr.Row():
                with gr.Column():
                    text_input = gr.Textbox(
                        label="Text to speak",
                        placeholder="Enter the text you want to convert to speech...",
                        lines=5
                    )
                    audio_prompt = gr.Audio(
                        label="Voice Reference (Optional)",
                        type="filepath"
                    )
                    
                    with gr.Accordion("Advanced Settings", open=False):
                        exaggeration = gr.Slider(
                            label="Exaggeration",
                            minimum=0.0,
                            maximum=1.0,
                            value=0.5,
                            step=0.05,
                            info="Controls emotional intensity (higher = more expressive)"
                        )
                        temperature = gr.Slider(
                            label="Temperature",
                            minimum=0.1,
                            maximum=1.0,
                            value=0.7,
                            step=0.05,
                            info="Controls randomness (higher = more variation)"
                        )
                        cfg_weight = gr.Slider(
                            label="CFG Weight",
                            minimum=0.0,
                            maximum=1.0,
                            value=0.5,
                            step=0.05,
                            info="Controls adherence to text (higher = more precise)"
                        )
                        seed = gr.Number(
                            label="Seed",
                            value=None,
                            precision=0,
                            info="Set for reproducible results (leave empty for random)"
                        )
                    
                    generate_btn = gr.Button("Generate Speech", variant="primary")
                
                with gr.Column():
                    output_audio = gr.Audio(label="Generated Speech")
                    
            generate_btn.click(
                fn=generate_speech,
                inputs=[text_input, audio_prompt, exaggeration, temperature, cfg_weight, seed],
                outputs=output_audio
            )
            
        with gr.Tab("Usage Tips"):
            gr.Markdown("""
            ## Tips for Best Results
            
            ### General Use (TTS and Voice Agents)
            - The default settings (exaggeration=0.5, cfg_weight=0.5) work well for most prompts
            - If the reference speaker has a fast speaking style, lowering cfg_weight to around 0.3 can improve pacing
            
            ### Expressive or Dramatic Speech
            - Try lower cfg_weight values (e.g. ~0.3) and increase exaggeration to around 0.7 or higher
            - Higher exaggeration tends to speed up speech; reducing cfg_weight helps compensate with slower, more deliberate pacing
            
            ### For Streamer Chat TTS
            - For consistent voice quality, use the same reference audio for all generations
            - Keep messages relatively short for best results
            - Adjust exaggeration based on the desired emotional intensity
            """)
    
    return app

if __name__ == "__main__":
    import torch
    app = create_ui()
    app.launch(share=True)
