from aiogram import types
from transformers import pipeline
from uuid import uuid4

from loader import dp


@dp.message_handler(content_types=types.ContentType.VOICE)
async def get_voice(msg: types.Message):

    await msg.reply("<b>Qabul qildim. Iltimos, biroz kuting!</b>")
    file_name = str(uuid4()) + ".flac"
    with open(file_name, 'wb') as f:
        await msg.voice.download(f)

    pipe = pipeline("automatic-speech-recognition", "lucio/xls-r-uzbek-cv8")
    data = pipe(file_name)

    await msg.reply(f"<b>Text:\n\n</b><code>{data['text'].capitalize()}</code>")