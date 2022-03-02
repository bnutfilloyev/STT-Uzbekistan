from aiogram import types
from transformers import pipeline

from loader import dp


@dp.message_handler(content_types=types.ContentType.VOICE)
async def get_voice(msg: types.Message):

    await msg.reply("Qabul qildim. Iltimos, kuting!.")
    with open('sample.flac', 'wb') as f:
        await msg.voice.download(f)

    pipe = pipeline("automatic-speech-recognition", "lucio/xls-r-uzbek-cv8")
    data = pipe("sample.flac")
    await msg.delete()
    await msg.answer(f"<b>Text:\n\n</b><code>{data['text'].capitalize()}</code>")