import gradio as gr
from fastapi import FastAPI

from chatbot import iFace

app = FastAPI()

@app.get('/')
def home():
    return 'Gradio UI is running at /bot', 200


app = gr.mount_gradio_app(app, iFace, '/bot')