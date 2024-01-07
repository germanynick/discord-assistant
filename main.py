## Create Desktop app with 2 simple input (username, channel) and 1 button (submit)
## When click submit, it will open a new window with the discord chat of the channel

import gradio as gr
import webbrowser
import time
from selenium import webdriver
from transformers import pipeline

pipe = pipeline("text-classification")


def open_discord_chat(username, channel, message):
    if message != "":
        return pipe(message)[0]['label']

    if username == "" or channel == "":
        return "Please enter your username and channel name"
    else:

        # Using selenium to open discord chat
        
        driver = webdriver.Chrome()
        driver.get(f"https://discord.com/channels/{channel}")

        # wait for the page to load
        time.sleep(5)

        return "Discord chat opened successfully"

inputs = [
    gr.Textbox(label="Username"),
    gr.Textbox(label="Channel"),
    gr.Textbox(label="Message")
]

output = gr.Textbox()

submit_button = gr.Interface(fn=open_discord_chat, inputs=inputs, outputs=output, title="Discord Chat")
submit_button.launch()

