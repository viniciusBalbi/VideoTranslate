import gradio as gr
import whisper
import torch
import os
import numpy as np
from googletrans import Translator
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip
import tempfile
from pytube import YouTube
import asyncio

class VideoTranslator:
    def __init__(self):
        self.whisper_model = whisper.load_model("turbo")
        self.translator = Translator()

    def download_youtube_video(self, url):
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            temp_path = os.path.join(tempfile.gettempdir(), 'temp_video.mp4')
            stream.download(output_path=tempfile.gettempdir(), filename='temp_video.mp4')
            return temp_path
        except Exception as e:
            raise gr.Error(f"Error downloading YouTube video: {str(e)}")

    def transcribe_audio(self, video_path):
        try:
            result = self.whisper_model.transcribe(video_path)
            return result["text"], result["language"]
        except Exception as e:
            raise gr.Error(f"Transcription error: {str(e)}")

    async def translate_text(self, text, source_lang, target_lang):
        try:
            translation = await self.translator.translate(text, src=source_lang, dest=target_lang)
            return translation.text 
        except Exception as e:
            raise gr.Error(f"Translation error: {str(e)}")

    def generate_speech(self, text, language):
        try:
            if not isinstance(text, str):
                text = str(text)  

            tts = gTTS(text=text, lang=language)
        
            temp_path = os.path.join(tempfile.gettempdir(), 'temp_audio.mp3')
            tts.save(temp_path)  
        
            return temp_path
        except Exception as e:
            raise gr.Error(f"Speech generation error: {str(e)}")

    async def process_video(self, video_input, target_lang):
        try:
            if isinstance(video_input, str) and "youtube.com" in video_input:
                video_path = self.download_youtube_video(video_input)
            else:
                video_path = video_input
            
            transcription, detected_lang = self.transcribe_audio(video_path)
            
            translated_text = await self.translate_text(transcription, detected_lang, target_lang)
            
            translated_audio_path = self.generate_speech(translated_text, target_lang)
            
            temp_output_path = os.path.join(tempfile.gettempdir(), 'output_video.mp4')
            video = VideoFileClip(video_path)
            audio = AudioFileClip(translated_audio_path)
            
            if audio.duration > video.duration:
                audio = audio.subclip(0, video.duration)
            
            final_video = video.set_audio(audio)
            final_video.write_videofile(temp_output_path, codec="libx264", audio_codec="aac")
            
            return temp_output_path, transcription, translated_text
            
        except Exception as e:
            raise gr.Error(f"Processing error: {str(e)}")

def create_interface():
    translator = VideoTranslator()
    
    with gr.Blocks(title="Video Translation App") as interface:
        gr.Markdown("# Video Translation App")
        
        with gr.Row():
            with gr.Column():
                video_input = gr.Video(label="Upload Video")
                youtube_input = gr.Textbox(label="Or paste YouTube URL")
                
                target_lang = gr.Dropdown(
                    choices=["en", "es", "fr", "it", "de", "pt", "ja", "ko", "zh-cn"],
                    label="Target Language",
                    value=" "
                )
                
                process_btn = gr.Button("Process Video")
                
            with gr.Column():
                output_video = gr.Video(label="Translated Video")
                original_text = gr.Textbox(label="Original Transcription")
                translated_text = gr.Textbox(label="Translated Text")
        
        def process_wrapper(video, url, lang):
            input_source = url if url else video
            if not input_source:
                raise gr.Error("Please provide either a video file or YouTube URL")

            output_path, trans, translated = asyncio.run(translator.process_video(input_source, lang))
            return output_path, trans, translated
        
        process_btn.click(
            fn=process_wrapper,
            inputs=[video_input, youtube_input, target_lang],
            outputs=[output_video, original_text, translated_text]
        )
    
    return interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(share=True)
