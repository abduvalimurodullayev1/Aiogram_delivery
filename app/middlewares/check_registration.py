from aiogram.types import Update, User
from aiogram import BaseMiddleware, Bot, types

from typing import Callable, Dict, Any, Awaitable

from app.keyboards.inline import *
from app.utils.db_manager import db
from app.utils.states import OrderStateGroup, RegistrationStateGroup

EVENT_FROM_USER = 'event_from_user'


class CheckRegistrationMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        bot: Bot = data['bot']
        user: User = data.get(EVENT_FROM_USER)
        state = data['state']

        current_state = await state.get_state()

        user_data = await db.get_user(telegram_id=user.id)

        if not user_data and current_state in OrderStateGroup.__all_states__:
            await bot.send_message(chat_id=user.id, text='Iltimos avval registratsiyadan o`ting', reply_markup=types.ReplyKeyboardRemove())
            await state.set_state(RegistrationStateGroup.language)
            return await bot.send_message(chat_id=user.id, text='Tilni tanlang', reply_markup=inline_languages())

        data['user'] = user_data

        return await handler(event, data)


__all__ = [
    'CheckRegistrationMiddleware'
]
