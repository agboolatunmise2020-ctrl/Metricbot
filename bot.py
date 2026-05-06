import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# This looks for 'BOT_TOKEN' in Render Environment Variables
# If not found, it will print an error in your Render logs
TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    print("ERROR: BOT_TOKEN not found in Environment Variables!")
else:
    print("Token received. Initializing bot...")

bot = telebot.TeleBot(TOKEN)

# URL for your landing page
LANDING_PAGE_URL = "https://mglion.goaffnk.com/t/NV8y/"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(f"User {message.chat.id} started the bot.")
    markup = InlineKeyboardMarkup()
    
    # Button 1: Educative (stays in bot)
    about_button = InlineKeyboardButton(
        text="📖 About MGLion", 
        callback_data="about_info"
    )
    
    # Button 2: The Website Redirect
    web_button = InlineKeyboardButton(
        text="🌐 Visit Website", 
        url=LANDING_PAGE_URL
    )

    # Placing them side-by-side
    markup.row(about_button, web_button)

    welcome_text = (
        "Welcome! Discover a premium sports and gaming experience tailored for you.\n\n"
        "Click below to learn more or visit our platform."
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Handler for the educative info button
@bot.callback_query_handler(func=lambda call: call.data == "about_info")
def show_about(call):
    educative_text = (
        "**What is MGLion?**\n\n"
        "MGLion is a trusted platform for global sports markets and interactive gaming.\n\n"
        "✅ Secure access to top-tier entertainment\n"
        "✅ 24/7 dedicated support\n"
        "✅ Real-time sports updates\n\n"
        "Click 'Visit Website' to explore further!"
    )
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, educative_text, parse_mode="Markdown")

if __name__ == "__main__":
    print("Bot is successfully running and polling...")
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Connection Error: {e}")
