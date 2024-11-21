from tortoise.exceptions import DoesNotExist
from app.keyboards.reply import admin_panel_keyboard
from sqlalchemy.orm import Session
from app.utils.db import Menu
from app.utils.states import MenuStateGroup
from aiogram import types
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import F
from app.utils.states import *
admin = ['Abduvali_Murodullayev']
router = Router()
from aiogram.fsm.context import FSMContext
def is_admin(username):
    return username in admin




@router.message(F.text== "Admin panel", F.from_user.username == 'Abduvali_Murodullayev')
async def admin_panel(message: types.Message):
    await message.answer("Admin panelga hush kelibsiz",
                         reply_markup=admin_panel_keyboard())
    

@router.message(F.text == "Yangi mahsulot qo'shish", F.from_user.username == "Abduvali_Murodullayev")
async def add_product(message: types.Message, state: FSMContext):
    await message.answer("📌 Mahsulot nomini kiriting:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(MenuStateGroup.name)


@router.message(MenuStateGroup.name)
async def product_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("📸 Mahsulot uchun rasm URL-ni yuboring:")
    await state.set_state(MenuStateGroup.image)
    

@router.message(MenuStateGroup.image)
async def product_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.text)
    await message.answer("📝 Mahsulot tavsifini kiriting:")
    await state.set_state(MenuStateGroup.description)


@router.message(MenuStateGroup.description)
async def product_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("💰 Mahsulot narxini kiriting (so'mda):")
    await state.set_state(MenuStateGroup.price)


@router.message(MenuStateGroup.price)
async def product_price(message: types.Message, state: FSMContext, session: Session):
    try:
        price = int(message.text)  
    except ValueError:
        await message.answer("❌ Iltimos, narxni faqat son shaklida kiriting.")
        return

    data = await state.get_data()
    name = data["name"]
    image = data["image"]
    description = data["description"]

    new_menu_item = Menu(name=name, price=price, description=description, image=image)
    session.add(new_menu_item)
    session.commit()

    await message.answer(f"✅ Mahsulot muvaffaqiyatli qo'shildi:\n\n"
                         f"📌 Nomi: {name}\n"
                         f"📸 Rasm: {image}\n"
                         f"📝 Tavsif: {description}\n"
                         f"💰 Narxi: {price} so'm")
    await state.clear()




@router.message(F.text == "O'chirish", F.from_user.username == "Abduvali_Murodullayev")
async def ask_product_delete(message: types.Message, state: FSMContext):
    await message.reply("📌 Mahsulot nomini kiriting:")
    await state.set_state(DeleteProductStateGroup.confirm)

@router.message(DeleteProductStateGroup.confirm)
async def delete_product(message: types.Message, state: FSMContext, session: Session):
    product_name = message.text.strip()
    try:
        # Menu modelidan mahsulotni nomi bo‘yicha qidirish
        product = await Menu.get(name=product_name, session=session)
        await product.delete(session=session)
        await message.answer(f"✅ Mahsulot muvaffaqiyatli o'chirildi: {product_name}")
    except DoesNotExist:  # Tortoise ORM uchun xatolik
        await message.answer(f"❌ Mahsulot topilmadi: {product_name}")
    await state.clear()
