# Job Telegram Bot

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

This is a Scrapy project designed to scrape job listings from various sites and send them to a Telegram channel. The project utilizes Scrapy for web scraping, pandas for data manipulation, and the requests library for sending messages to Telegram.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/AbyvargheseMandapathel/job_updates_bot.git
```

2. **Install the required Python packages:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
TELEGRAM_API=<your_telegram_api_key>
CHAT_ID=<your_telegram_chat_id>
START_URLS=
```

## Usage

To run the Scrapy spider and scrape job listings:

```bash
scrapy crawl jobs -o output.csv
```


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
