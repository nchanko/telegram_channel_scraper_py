
from datetime import datetime, timezone
import nest_asyncio
import asyncio
from pyrogram import Client

def scrape_by_message(api_id, api_hash, channel_username, limit):
    # Allow nested asyncio calls in Google Colab
    nest_asyncio.apply()

    # Define an async function to get channel messages with a limit
    async def get_channel_messages():
        async with Client('my_account', api_id=api_id, api_hash=api_hash) as app:
            channel_info = await app.get_chat(channel_username)

            messages_list = []

            # Get messages from the channel with specified limit
            print("Getting chat histories by messages.")
            async for message in app.get_chat_history(channel_info.id, limit=limit):
                messages_list.append({
                    'date': message.date,
                    'message': message.text
                })
                # print(f"{message.date}: {message.text}")
            print("Scraping completed.")

        return messages_list

    # Run the async function using asyncio
    loop = asyncio.get_event_loop()
    messages_data = loop.run_until_complete(get_channel_messages())

    return messages_data

"""#Scrape by Date"""

def scrape_by_date(api_id, api_hash, channel_username, start_date, end_date):
    # Allow nested asyncio calls in Google Colab
    nest_asyncio.apply()

    # Convert start and end dates to UTC timezone
    start_date_utc = start_date.replace(tzinfo=timezone.utc)
    end_date_utc = end_date.replace(tzinfo=timezone.utc)

    # Define an async function to get channel messages within the specified period
    async def get_channel_messages_within_period():
        async with Client('my_account', api_id=api_id, api_hash=api_hash) as app:
            channel_info = await app.get_chat(channel_username)

            messages_list = []
            print("Getting data by date.")
            # Get messages from the channel
            async for message in app.get_chat_history(channel_info.id):
                # Convert message.date to UTC timezone
                message_date_utc = message.date.replace(tzinfo=timezone.utc)

                # Collect messages within the specified period
                if start_date_utc <= message_date_utc <= end_date_utc:
                    messages_list.append({
                        'date': message_date_utc,
                        'message': message.text
                    })

                # Break the loop if the message date is earlier than the start date
                if message_date_utc < start_date_utc:
                    break
            print("Scraping completed.")
            return messages_list

    # Run the async function using asyncio
    loop = asyncio.get_event_loop()
    messages_data = loop.run_until_complete(get_channel_messages_within_period())
    return messages_data