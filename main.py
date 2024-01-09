# from assistant import generate_text
from discord import get_message, send_message
from web_ui import launch
from actor import predict_from_directory

async def on_submit(directory, channel, actor_image):
    if directory is not None:
        names = predict_from_directory(directory)

        return names

    return "Please input a directory"

if __name__ == "__main__":
    launch(on_submit)