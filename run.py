import gradio as gr
from fastapi import FastAPI
import uvicorn
from chatbot import iFace

app = FastAPI()

# Use Gradio's `Interface.fastapi_app` to mount the Gradio app within FastAPI
app = gr.mount_gradio_app(app, iFace, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
