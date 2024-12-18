import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.methods import DeleteWebhook
from config.config import TOKEN
from aiogram import Bot, Dispatcher
from handlers.start_handler import router
from handlers.download_picture_handler import router as picture_handler
from handlers.download_video_handler import router as video_handler
from handlers.admin_handler import router as admin_router
# from handlers.newsletter_handler import router as newsletter_router
# from handlers.newsletter_handler import init_db


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(picture_handler)
    dp.include_router(video_handler)
    dp.include_router(admin_router)
    # dp.include_router(newsletter_router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        # init_db()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
