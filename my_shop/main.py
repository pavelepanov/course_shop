from aiogram import Bot, Dispatcher
import asyncio
import logging

from core.handlers.basic import get_start
from config import TOKEN


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)

    dp = Dispatcher()
    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
