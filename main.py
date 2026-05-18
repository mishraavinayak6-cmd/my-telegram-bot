import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import httpximport os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import httpx

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """Tu ek AI Study Assistant hai jo students ki help karta hai.
Tu Hindi aur English dono me samjha sakta hai.
Tu concepts simply explain karta hai, notes summarize karta hai,
MCQs banata hai, aur exam preparation me help karta hai.
Hamesha friendly aur helpful tone me jawab de."""

async def ask_groq(user_message: str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 1024
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data, timeout=30)
        result = response.json()
        return result["choices"][0]["message"]["content"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 *AI Study Assistant me aapka swagat hai!*\n\n"
        "Main aapki study me help kar sakta hoon:\n"
        "📚 Concepts explain\n"
        "📝 Notes summarize\n"
        "🧠 MCQs banana\n"
        "🎯 Exam preparation\n\n"
        "Bas apna question likho!",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Kya kya pooch sakte ho:*\n\n"
        "• Photosynthesis explain karo\n"
        "• Python loops samjhao Hindi me\n"
        "• UPSC ke notes short karo\n"
        "• Science ke 10 MCQ banao\n\n"
        "Seedha apna sawaal likho! 🚀",
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text("⏳ Soch raha hoon...")
    try:
        reply = await ask_groq(user_text)
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text("❌ Kuch problem aayi. Dobara try karo!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """Tu ek AI Study Assistant hai jo students ki help karta hai.
Tu Hindi aur English dono me samjha sakta hai.
Tu concepts simply explain karta hai, notes summarize karta hai,
MCQs banata hai, aur exam preparation me help karta hai.
Hamesha friendly aur helpful tone me jawab de."""

async def ask_groq(user_message: str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 1024
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data, timeout=30)
        result = response.json()
        return result["choices"][0]["message"]["content"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 *AI Study Assistant me aapka swagat hai!*\n\n"
        "Main aapki study me help kar sakta hoon:\n"
        "📚 Concepts explain\n"
        "📝 Notes summarize\n"
        "🧠 MCQs banana\n"
        "🎯 Exam preparation\n\n"
        "Bas apna question likho!",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Kya kya pooch sakte ho:*\n\n"
        "• Photosynthesis explain karo\n"
        "• Python loops samjhao Hindi me\n"
        "• UPSC ke notes short karo\n"
        "• Science ke 10 MCQ banao\n\n"
        "Seedha apna sawaal likho! 🚀",
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text("⏳ Soch raha hoon...")
    try:
        reply = await ask_groq(user_text)
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text("❌ Kuch problem aayi. Dobara try karo!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
