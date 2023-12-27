# Book Watch

Keep a close eye on your favorite book with this simple Python script designed to monitor the availability of specific book on Knihobot.cz. Receive notifications effortlessly thanks to [ntfy.sh](https://ntfy.sh/).

## Table of Contents

* [Features](#features)
* [How to Use](#how-to-use)
  * [Configuration](#configuration)
  * [Deployment](#deployment)
* [License](#license)
* [Risks](#use-at-your-own-risk)
* [Made with love](#made-with-love)

## Features

* Monitor the availability of your chosen book on Knihobot.cz.
* Receive notifications seamlessly through [ntfy.sh](https://ntfy.sh/).

## How to Use

### Configuration

To tailor the script to your preferences, utilize the `book_config` file. Specify the books you wish to track and customize other settings as needed.

### Deployment

#### Docker

1. Build the Docker image:

   ```
   docker build -t book-watch .
   ```
2. Run the Docker container:

   ```
   docker run -d --name book-watch-container book-watch
   ```

   Adjust the container name (`book-watch-container`) as desired.

## License

This project is licensed under the Apache License 2.0.

## Use at Your Own Risk

Please be cautious when using this script. The default time check interval is 60-120 seconds. Avoid lowering intervals to prevent spamming Knihobot.cz.

## Made with love

Crafted for book lovers ❤️
