from aiogram import types
from transformers import pipeline

from loader import dp


@dp.message_handler(content_types=types.ContentType.VOICE)
async def get_voice(msg: types.Message):

    with open('sample.flac', 'wb') as f:
        await msg.voice.download(f)

    pipe = pipeline("automatic-speech-recognition", "lucio/xls-r-uzbek-cv8")
    pipe("sample.flac")

    await msg.reply('Voice saved')
    await msg.answer(f"Voice: {msg.voice.file_id}")