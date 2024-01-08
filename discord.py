
from selenium import webdriver
import time

async def login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://discord.com/login")

    time.sleep(3)

    driver.close()


async def get_message(user, channel):
    await login(user, "password")
    return f'Hello {user}!, on channel {channel}'


async def send_message(user, channel, message):
    #TODO: Implement this
    return "Message sent!"