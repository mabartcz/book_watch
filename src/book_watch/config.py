import pathlib

import yaml
from pydantic import BaseModel
from book_watch.paths import ASSETS_PATH


class Book(BaseModel):
    name: str
    url: str

class Config(BaseModel):
    book: Book
    ntfy_url: str


def read_config(file_path: pathlib.Path) -> Config:
    """Reads the `*_config.yaml` file and returns a Config object.

    Parameters:
        file_path (str): The path to the `*_config.yaml` file.

    Returns:
        Config: The parsed configuration.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        config_data = yaml.safe_load(file)
    return Config(**config_data)


if __name__ == '__main__':
    config = read_config(ASSETS_PATH / 'book_config.yaml')
    print(config.ntfy_url)
    print(config.book.name)
    print(config.book.url)


