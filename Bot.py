from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

# Function to handle the /get command
def get_cookie(update: Update, context: CallbackContext):
    # Create a session to make the request
    session = requests.Session()
    url = "https://www.youtube.com"
    
    # Get the response from YouTube
    response = session.get(url)
    
    # Extract the cookies from the session
    cookies = session.cookies.get_dict()
    
    # Prepare the cookies to send as a text file
    cookie_data = "\n".join([f"{key}: {value}" for key, value in cookies.items()])
    
    # Save the cookies to a file
    with open("youtube_cookies.txt", "w") as file:
        file.write(cookie_data)
    
    # Send the file to the user
    update.message.reply_document(document=open("youtube_cookies.txt", "rb"))

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


    
 
