from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Assalom Alaykum, {message.from_user.full_name}!\n\n</b>"
                         f"Botdan foydalanish uchun voice yuboring")
