# from assistant import generate_text
from discord import send_message
from web_ui import launch
from actor import predict_from_directory

def on_submit(directory, channel, actor_image):
    if directory is not None:
        names = predict_from_directory(directory)
        send_message(names)
        return names

    return "Please input a directory"

if __name__ == "__main__":
    launch(on_submit)