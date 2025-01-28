from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

# Function to handle the /get command
async def get_cookie(update: Update, context: CallbackContext) -> None:
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
    await update.message.reply_document(document=open("cookie_script.txt", "rb"))

# Set up the bot
def main():
    # Replace 'YOUR_TOKEN' with your bot's token
    token = "8116033425:AAFP7TkcGv9RCLJFkgJI9Hi5pm4Mvxl7cXo"
    
    # Application setup
    application = Application.builder().token(token).build()

    # Add the /get command handler
    application.add_handler(CommandHandler("get", get_cookie))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()


    
 
