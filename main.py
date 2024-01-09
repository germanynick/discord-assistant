# from assistant import generate_text
from discord import get_message, send_message
from web_ui import launch
from actor import predict

async def on_submit(username, channel, actor_image):
    if (actor_image is not None):
        return predict(actor_image)
        
    return username
    # message = await get_message(username, channel)
    # generated_message = generate_text(message)

    # send_message(username, channel, generated_message)
    
    # return generated_message

if __name__ == "__main__":
    launch(on_submit)