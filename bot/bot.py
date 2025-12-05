import logging
import requests
import dotenv
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes


dotenv.load_dotenv()

TELEGRAM_API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
BACKEND_SERVER_URL = os.environ.get("BACKEND_SERVER_URL")
BACKEND_HOST = os.environ.get("BACKEND_HOST")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def analyze_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = update.message.text
    chat_id = update.message.chat_id
    chat_type = update.message.chat.type

    logger.info(f"Message in chat: {chat_id}...")

    if not text:
        return

    try:
        response = requests.post(
            BACKEND_SERVER_URL,
            json={"text": text, "chat_id": chat_id},
            headers={"Host": BACKEND_HOST},
            timeout=15,
        )
        logger.info(f"Message sent to backend: {text[:50]}...")
        logger.info(f"Backend response: {response.json()}")

        if chat_type == "private":
            
            response_data = response.json()
            class_probs = [
                ("No threat", response_data["class_0_probability"]),
                ("Judicial threat", response_data["class_1_probability"]),
                ("Actual threat", response_data["class_2_probability"]),
            ]
            prob_strings = [f"{name}: {prob:.6}" for name, prob in class_probs]
            reply_text = f"Analysis for message (first 50 chars):\n{text[:50]}\n\nProbabilities:\n" + \
                "\n".join(prob_strings)

            await context.bot.send_message(chat_id=chat_id, text=reply_text)

    except Exception as e:
        logger.error(f"Failed to send message to backend: {e}")

def main():
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze_message))

    application.run_polling()
    logger.info("Bot started and listening for messages...")

if __name__ == "__main__":
    main()
