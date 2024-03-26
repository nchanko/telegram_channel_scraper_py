import pandas as pd
from scraper import scrape_by_message, scrape_by_date
from save_data import save_to_csv
from dotenv import load_dotenv
import os
from datetime import datetime, timezone


"""#Main Function"""

def main():

  # Replace with your actual values
  load_dotenv()
  api_id = os.getenv('telegram_api_id')  
  api_hash = os.getenv('telegram_api_hash')
  #https://t.me/burmesevoanews, for channel username, only use the last part of the url.
  channel_username = 'burmesevoanews'
  limit = 20
  #sheetname ='SHEET_NAME'
  #sheet_address = 'SHHET_ADDRESS'

  #Shuld be year /month/ date format.
  start_date = datetime(2024, 1, 1, tzinfo=timezone.utc)
  end_date = datetime(2024, 3, 28, tzinfo=timezone.utc)

  #Choose method scrape by message or scrape by date. If scrape by  date , provide starting date and ending date.
  
  #messages_data = scrape_by_message(api_id,api_hash,channel_username,limit)
  messages_data = scrape_by_date(api_id, api_hash, channel_username, start_date, end_date)

  print("Creating dataframe.")
  df = pd.DataFrame(messages_data)
  # Display the DataFrame
  print(df.head())
  save_to_csv(df,f"{channel_username}.csv")

main()