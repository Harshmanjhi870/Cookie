from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

# Function to handle the /get command
async def get_cookie(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    
    # Send the file to the user (awaiting the send method)
    await update.message.reply_document(document=open("youtube_cookies.txt", "rb"))

# Set up the bot
def main():
    # Replace 'YOUR_TOKEN' with your bot's token
    application = Application.builder().token("YOUR_TOKEN").build()

    # Add the /get command handler
    application.add_handler(CommandHandler("get", get_cookie))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
