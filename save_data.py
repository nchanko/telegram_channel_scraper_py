
"""#Save to Sheet."""
import pandas as pd
# def save_to_sheet(df,sheetname, sheet_address):

#   gc = gspread.authorize(creds)
#   wb = gc.open_by_url(sheet_address)
#   sheet = wb.worksheet(sheetname)
#   # get_all_values gives a list of rows.
#   print("loading gsheet data..")
#   data = sheet.get_all_values()

#   # Assuming df is your DataFrame with Timestamp objects
#   print("Preparing data to send to sheet. ")
#   df_to_append = pd.DataFrame({
#       'date': df['date'].astype(str),  # Convert Timestamp to string
#       'message': df['message']
#   })

#   # Append the new data to the existing data
#   print("Appending data to existing .")
#   updated_data = data + df_to_append.values.tolist()

#   # Update the Google Sheet with the combined data
#   sheet.update('A1', updated_data)
#   print("Process completed!")

def save_to_csv(df, filename):
    """Saves DataFrame df to a CSV file at path with filename."""
    # Ensure the path ends correctly

    # Save the DataFrame
    df.to_csv(f"{filename}", index=False)
