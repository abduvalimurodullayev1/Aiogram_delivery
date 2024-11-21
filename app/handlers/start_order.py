from app.utils.functions import get_address, haversine
from app.utils.states import OrderStateGroup

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from app.handlers.commands import start_command
from app.keyboards.inline import inline_main_menu, generate_category_keyboard
from app.keyboards.reply import reply_start_order, reply_send_location
from app.utils.callback_data import MainMenuCallbackData, MainMenuAction
from app.utils.states import OrderStateGroup

router = Router()


@router.callback_query(MainMenuCallbackData.filter(F.action == MainMenuAction.ORDER))
async def start_order(update: [types.CallbackQuery, types.Message], state: FSMContext):
    if isinstance(update, types.CallbackQuery):
        callback_query = update
        await callback_query.message.answer(
            f"Buyurtmani birga joylashtiramizmi? 🤗 Buyurtma turini tanlang?",
            reply_markup=reply_start_order())

    if isinstance(update, types.Message):
        message = update
        await message.answer("Buyurtmani birga joylashtiramizmi? �� Buyurtma turini tanlang?",
                             reply_markup=reply_start_order())

    await state.set_state(OrderStateGroup.order_type)


@router.message(F.text == "Orqaga")
async def order_message(message: types.Message, state: FSMContext, user: dict | None):
    await message.answer("Buyurtmani birga joylashtiramizmi? 🤗", reply_markup=ReplyKeyboardRemove())
    await message.answer("Quyidagilardan birini tanlang", reply_markup=inline_main_menu())
    await state.clear()


@router.message(F.text == 'Borib olish', OrderStateGroup.order_type)
async def order_book_message(message: types.Message, state: FSMContext):
    await message.answer("�� Borib olish uchun geo-joylashuvni jo'nating, sizga yaqin bo'lgan filialni aniqlaymiz",
                         reply_markup=reply_send_location())
    await state.update_data({'type_order': 'take_away'})
    await state.set_state(OrderStateGroup.send_location)



@router.message(F.location, OrderStateGroup.send_location)
async def handle_location_message(message: types.Message, state: FSMContext):
    order_data = await state.get_data()
    order_type = order_data.get('type_order', None)
    import logging

    if order_type == 'delivery':
        distance = await haversine(
            message.location.longitude,
            message.location.latitude,
            69.243001, 
            41.328492  
        )
        logging.critical(distance)
        if distance >= 20:
            return await message.answer('Выбранная локация находится вне зоны доставки.')

    await state.update_data(
        {'coordinate': {'longitude': message.location.longitude, 'latitude': message.location.latitude}}
    )

    await message.answer(
        "Lokatsiya qabul qilindi\nKategoriyalardan birini tanlang:",
        reply_markup=generate_category_keyboard()
    )