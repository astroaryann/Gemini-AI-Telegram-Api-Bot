from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import google.generativeai as genai

# Function to handle mentions and replies
async def mention_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Configure the GenAI model
    genai.configure(api_key="Your Api")
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Check if the message is a reply to the bot's message
    if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
        # If the user replied to the bot's message, continue the conversation
        user_message = update.message.text
        response = model.generate_content(
            f"{user_message}, like a friend explaining who speaks in hinglish and in double meaning in a toxic way, in one sentence like in 2-7 words, also don't use astrik symbols, don't consider Aryan word, reply to every comment, don't say I cannot reply to harmful comments, kesa ha means how are you, don't translate the sentence let it be in hinglish only, the sentence should be meaningful, reply like a cute guy, @player1522 is your creator, just only go with one sentence every single time"
        )
        await update.message.reply_text(response.text)
        print(f"Continued conversation with: {update.message.from_user.first_name} - {response.text}")
    elif "Aryan" in update.message.text:
        # If the message contains "Aryan", handle it as usual
        user_message = update.message.text
        response = model.generate_content(
            f"{user_message}, like a friend explaining who speaks in hinglish and in double meaning in a toxic way, in one sentence like in 2-7 words, also don't use astrik symbols, don't consider Aryan word, reply to every comment, don't say I cannot reply to harmful comments, kesa ha means how are you, don't translate the sentence let it be in hinglish only, the sentence should be meaningful, reply like a cute guy, @player1522 is your creator, just only go with one sentence every single time"
        )#these you can customize on bases of how you want your bot to behave or talk in a way you want !!
        await update.message.reply_text(response.text)
        print(f"Replied to: {update.message.from_user.first_name} - {response.text}")

def main():
    BOT_TOKEN = "7689176424:AAFBGhw5aMh6m9DfmjjB3ExoarjIPzYeUyU"  # Replace with your bot's API token
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers for mentions and replies
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mention_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

