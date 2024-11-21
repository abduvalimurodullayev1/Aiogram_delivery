from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from app.keyboards.inline import generate_category_keyboard
from app.keyboards.reply import yes_or_no  # Lokatsiyani tasdiqlash tugmalari
from app.handlers.start_order import start_order
from app.utils.functions import haversine
from app.keyboards.reply import *
from app.utils.states import OrderStateGroup
import logging
router = Router()

@router.message(F.text == "Orqaga", OrderStateGroup.send_location)
async def order_message(message: types.Message, state: FSMContext):
    await start_order(update=message, state=state)

@router.message(F.text == "Eltib berish")
async def handle_eltib_berish(message: types.Message, state: FSMContext):
    logging.info("Eltib berish tugmasi bosildi.") 
    await state.set_state(OrderStateGroup.send_location)  # Holatni o'rnatish
    await message.answer("Lokatsiyani jo'nating", reply_markup=reply_send_location())  # Lokatsiya tugmasi

@router.message(F.location, OrderStateGroup.send_location)
async def order_book_message(message: types.Message, state: FSMContext):
    """
    Lokatsiyani qabul qilish va masofani tekshirish.
    """
    order_data = await state.get_data()
    order_type = order_data.get("type_order", None)

    if order_type == "delivery":
        distance = await haversine(
            message.location.longitude, message.location.latitude, 
            69.243001, 41.328492
        )
        if distance >= 20:
            return await message.answer("Выбранная локация находится вне зоны доставки.")

    # Lokatsiyani saqlash
    await state.update_data(
        coordinate={"longitude": message.location.longitude, "latitude": message.location.latitude}
    )

    # Lokatsiyani tasdiqlash
    await message.answer("Joylashuvni tasdiqlaysizmi?", reply_markup=yes_or_no())
    await state.set_state(OrderStateGroup.confirm_location)  # Tasdiqlash holatiga o'tish


@router.message(F.text.in_(["Ha", "Yo'q"]), OrderStateGroup.confirm_location)
async def confirm_location(message: types.Message, state: FSMContext):
    """
    Lokatsiyani tasdiqlash yoki rad etish.
    """
    if message.text == "Ha":
        await message.answer("Kategoriyalardan birini tanlang", reply_markup=generate_category_keyboard())
        await state.set_state(OrderStateGroup.category) 
    elif message.text == "Yo'q":
        await state.set_state(OrderStateGroup.send_location)  # Lokatsiya yuborish holatiga qaytish
        await message.answer("Iltimos, qayta lokatsiya yuboring.")
