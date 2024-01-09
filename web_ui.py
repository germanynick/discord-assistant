## Create Desktop app with 2 simple input (username, channel) and 1 button (submit)
## When click submit, it will open a new window with the discord chat of the channel

import gradio as gr
import webbrowser

def launch(on_submit):
    inputs = [
        gr.Textbox(label="Username"),
        gr.Textbox(label="Channel"),
        gr.Image(label="Actor Image")
    ]

    output = [gr.Textbox(), gr.Image()]

    interface = gr.Interface(fn=on_submit, inputs=inputs, outputs=output, title="Discord Chat")
    
    interface.launch(share=True, debug=True)

    return interface
