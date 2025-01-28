from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Function to handle the /get command
def get_cookie(update: Update, context: CallbackContext):
    # Code to create the file with the Python script
    code = '''import requests

session = requests.Session()
url = "https://www.youtube.com"
response = session.get(url)
print(session.cookies.get_dict())'''
    
    # Save the code to a file
    with open("cookie_script.txt", "w") as file:
        file.write(code)
    
    # Send the file to the user
    update.message.reply_document(document=open("cookie_script.txt", "rb"))

# Set up the bot
def main():
    # Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater("8116033425:AAFP7TkcGv9RCLJFkgJI9Hi5pm4Mvxl7cXo", use_context=True)
    dispatcher = updater.dispatcher

    # Add the /get command handler
    dispatcher.add_handler(CommandHandler("get", get_cookie))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
