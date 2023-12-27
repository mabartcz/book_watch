import sys

import requests
import random
import time
from bs4 import BeautifulSoup
from loguru import logger


# Function to check the webpage content
def check_webpage():
    url = "https://knihobot.cz/g/185848"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the specified text is present on the webpage
    if "Knihu momentálně nemáme skladem" not in soup.text:
        logger.info("Kniha je dostupna !")
        send_notification()
    else:
        logger.info("Kniha není dostupná.")

# Function to send an email
def send_notification():
    requests.post("https://ntfy.sh/book-svet-mest",
        data="Kniha Svet mest je dostupna !",
        headers={ "Priority": "5", "Click": "https://knihobot.cz/g/185848"})


if __name__ == "__main__":
    logger.remove(0)
    logger.add(sys.stderr, level='DEBUG')

    logger.add('log_{time:YYYY-MM-DD}.log', level='DEBUG', enqueue=False)

    while True:
        check_webpage()
        time.sleep(random.randint(60, 120))