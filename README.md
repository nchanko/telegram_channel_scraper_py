# Telegram Channel Scraper v1.1

## Overview
This script, developed by Nyein Chan Ko Ko, is designed to scrape messages from Telegram channels. It's been modularized and transferred from Google Colab for ease of use.

## Features
- **Scrape by Date:** Provide `api_id`, `api_hash`, channel username, start date, and end date.
- **Scrape by Message Counts:** Provide `api_id`, `api_hash`, channel_username, and a limit on the number of messages.

## Getting Started
1. Obtain your `api_id` and `api_hash` from [Telegram's API](https://core.telegram.org/api/obtaining_api_id).
2. Run `main.py` and enter your channel name, `api_id`, and `api_hash` when prompted.
3. Input your phone number registered with Telegram. You will receive a token on Telegram, which you need to enter into the script.
4. If required, input your Telegram password.
5. The script will commence scraping based on the provided parameters.

## Notes
- Ensure your phone number is linked to a Telegram account.
- You might need to implement additional code to handle timeouts during scraping.
