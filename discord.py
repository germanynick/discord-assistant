
from selenium import webdriver
import time

async def login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://discord.com/login")

    time.sleep(3)

    return driver


async def get_message(user, channel):
    return "Last message: Hello!"


async def send_message(user, channel, message):
    #TODO: Implement this
    return "Message sent!"