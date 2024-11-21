from app.utils.functions import *

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from app.keyboards.inline import *
from app.keyboards.inline import inline_main_menu
from app.keyboards.reply import reply_start_order, reply_send_location
from app.utils.callback_data import BranchesCallbackData, MainMenuAction, MainMenuCallbackData
from app.utils.states import OrderStateGroup

router = Router()
branch_locations = {
    'Algoritm': (41.311081, 69.240562),
    'Andalus': (41.327545, 69.281204),
    'Andijon1': (40.789856, 72.339271),
}



@router.callback_query(BranchesCallbackData.filter(F.action == BranchesAction.NEXT))
async def show_next_branches(callback_query: types.CallbackQuery, callback_data: BranchesCallbackData):
    page = callback_data.page or 0
    keyboard = branches_build(page=page)
    await callback_query.message.edit_text("Filiallardan birini tanlang:", reply_markup=keyboard)



@router.callback_query(MainMenuCallbackData.filter(F.action == MainMenuAction.BRANCHES))
async def show_branches_menu(callback_query: types.CallbackQuery):
    keyboard = branches_build(page=0)
    await callback_query.message.edit_text("Filiallardan birini tanlang:", reply_markup=keyboard)

    

@router.callback_query(BranchesCallbackData.filter(F.action == BranchesAction.BACK))
async def show_previous_branches(callback_query: types.CallbackQuery, callback_data: BranchesCallbackData):
    page = callback_data.page or 0
    keyboard = branches_build(page=page)
    await callback_query.message.edit_text("Filiallardan birini tanlang:", reply_markup=keyboard)

async def find_nearest_branch(user_lat, user_lon):
    nearest_branch = None
    min_distance = float('inf')
    
    for branch_name, (branch_lat, branch_lon) in branch_locations.items():
        distance = await haversine(user_lon, user_lat, branch_lon, branch_lat)
        if distance < min_distance:
            min_distance = distance
            nearest_branch = branch_name
    
    return nearest_branch, min_distance



@router.message(F.location)
async def handle_location(message: types.Message):
    user_lat = message.location.latitude
    user_lon = message.location.longitude
    
    nearest_branch, distance = await find_nearest_branch(user_lat, user_lon)
    
    await message.reply(
        f"Eng yaqin filial: {nearest_branch}\nMasofa: {distance:.2f} km"
    )
