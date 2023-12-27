import sys

import time
import random
import requests
from loguru import logger
from bs4 import BeautifulSoup

from book_watch.paths import LOGS_PATH
from book_watch.paths import ASSETS_PATH
from book_watch.config import Config
from book_watch.config import read_config


@logger.catch()
def check_webpage(config: Config) -> None:
    """Check the webpage for the availability of a book.

    Args:
        config (Config): The configuration object from book_config.yaml.

    Returns:
        None
    """
    response = requests.get(config.book.url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if config.book.name in soup.text:
        if "Knihu momentálně nemáme skladem" not in soup.text:
            logger.info("Book is in stock!")
            send_notification_in_stock(config)
        else:
            logger.info("Book is unavailable.")
    else:
        send_notification_info(config)

        logger.debug(response)
        logger.debug(soup.text)
        logger.info("Page was not loaded.")


def send_notification_in_stock(config: Config) -> None:
    """Sends a notification when a book is in stock.

    Args:
        config (Config): The configuration object from book_config.yaml.

    Returns:
        None
    """
    requests.post(config.ntfy_url,
        data=f"Book: {config.book.name} is in stock !",
        headers={"Priority": "5", "Click": config.book.url})


def send_notification_info(config: Config) -> None:
    """Sends a notification when Knihobot is unavailable.

    Args:
        config (Config): The configuration object from book_config.yaml.

    Returns:
        None
    """
    requests.post(config.ntfy_url,
        data="Knihobot is unavailable :(",
        headers={"Priority": "1"})


if __name__ == "__main__":
    logger.remove(0)
    logger.add(sys.stderr, level='DEBUG')
    logger.add(LOGS_PATH / 'log_{time:YYYY-MM-DD}.log', level='DEBUG', enqueue=False)

    config_book = read_config(ASSETS_PATH / 'book_config.yaml')

    while True:
        check_webpage(config_book)
        time.sleep(random.randint(60, 120))