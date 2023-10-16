from aiogram import Router
from aiogram.types import Message

router = Router()

# Этот хендлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Извините,\nтаким коммандам: "{message.text}"\nменя пока не обучали🤷🏻‍♂️')