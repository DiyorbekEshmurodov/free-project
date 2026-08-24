# Agar ushbu fayl alohida python run_bot.py qilib yurgizilsa, Django'ni yuklaydi
import asyncio
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


from aiogram import Bot, Dispatcher
from django.conf import settings
from bot.bot_main import main_router


async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    # Webhook va eski xabarlarni tozalaymiz
    await bot.delete_webhook(drop_pending_updates=True)

    # Routerni ulaymiz
    dp.include_router(main_router)

    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
