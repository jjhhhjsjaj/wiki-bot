import logging
import wikipediaapi
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
import asyncio

TOKEN = "7481429350:AAGf0ZIHez8C3tysUE-KQ0Rga8BLdRwRzR0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Wikipedia API sozlamalari (user_agent qo'shildi)
wiki_wiki = wikipediaapi.Wikipedia(user_agent="WikipediaUzBot/1.0 (example@gmail.com)", language="uz")

logging.basicConfig(level=logging.INFO)

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("Salom! Men Wikipedia botman. Menga so‘z yuboring va men ma’lumot topib beraman.")

@dp.message()
async def wiki_search(message: Message):
    query = message.text
    page = wiki_wiki.page(query)

    if page.exists():
        await message.answer(page.summary[:1000] + "\n\nBatafsil: " + page.fullurl)
    else:
        await message.answer("Kechirasiz, bu mavzu bo‘yicha Wikipedia'da ma'lumot topilmadi.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())