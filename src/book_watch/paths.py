import pathlib

# Directories and files
SOURCES_PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve()
ROOT_PATH = SOURCES_PATH.parent.resolve()
ASSETS_PATH = SOURCES_PATH / 'assets'
LOGS_PATH = ROOT_PATH / 'logs'


if __name__ == '__main__':
    print(f'ROOT_PATH:\t\t{ROOT_PATH}')
    print(f'SOURCES_PATH:\t{SOURCES_PATH}')
    print(f'ASSETS_PATH:\t{ASSETS_PATH}')
    print(f'LOGS_PATH:\t\t{LOGS_PATH}')
