from aiogram.types import ChatType, Message, CallbackQuery

from app.misc import dp
from app.models import Chats


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['start'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """Просто отправьте мне имя артиста и/или название композиции, и я найду эту композицию!!

🔰 Подпишись на канал: @SJa_bots
👨‍💻 По всем вопросам: @SJ_Lynx
"""
    await message.reply(text,
                        disable_web_page_preview=True, parse_mode="Html")


@dp.callback_query_handler(text_startswith=['delete'])
async def _delete_message(query: CallbackQuery):
    await query.message.delete()
