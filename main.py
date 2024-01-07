from assistant import generate_text
from discord import get_message
from web_ui import launch

async def on_submit(username, channel):
    message = await get_message(username, channel)
    generated_message = generate_text(message)
    return generated_message

if __name__ == "__main__":
    launch(on_submit)