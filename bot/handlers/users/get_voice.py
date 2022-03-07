from aiogram import types
from transformers import pipeline

from bot.loader import dp


@dp.message_handler(content_types=types.ContentType.VOICE)
async def get_voice(msg: types.Message):

    await msg.reply("<b>Qabul qildim. Iltimos, biroz kuting!</b>")
    with open('sample.flac', 'wb') as f:
        await msg.voice.download(f)

    pipe = pipeline("automatic-speech-recognition", "lucio/xls-r-uzbek-cv8")
    data = pipe("sample.flac")

    await msg.reply(f"<b>Text:\n\n</b><code>{data['text'].capitalize()}</code>")