import logging
from aiogram import types, Router, F
from aiogram.filters import Command
from core.database.models import User
from core.excel.excel_generator import create_excel
from settings import settings


logger = logging.getLogger(__name__)
router = Router(name='Admin commands router')


@router.message(Command(commands=['stats']))
async def excel_stats(message: types.Message):
    # cuz command is only for 'admin'
    user = await User.get(user_id=message.from_user.id)
    if user.status != 'admin':
        return

    file_in_memory = await create_excel(model=User)
    await message.answer_document(document=types.BufferedInputFile(file_in_memory.read(), filename=settings.excel_file))


# get file_id for broadcaster
@router.message(F.video | F.video_note | F.photo | F.audio | F.animation | F.sticker | F.document)
async def get_hash(message: types.Message):
    if (await User.get(user_id=message.from_user.id)).status != 'admin':
        return

    if message.video:
        hashsum = message.video.file_id
    elif message.video_note:
        hashsum = message.video_note.file_id
    elif message.photo:
        hashsum = message.photo[-1].file_id
    elif message.audio:
        hashsum = message.audio.file_id
    elif message.animation:
        hashsum = message.animation.file_id
    elif message.sticker:
        hashsum = message.sticker.file_id
    elif message.document:
        hashsum = message.document.file_id
    else:
        return

    await message.answer(f'<code>{hashsum}</code>')
