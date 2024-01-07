
from selenium import webdriver
import time

async def login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://discord.com/login")

    time.sleep(3)

    return driver


async def get_message(user, channel):
    page = await login("username", "password")

    return "Login successful!"

