from app.utils.functions import *

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from app.keyboards.inline import *
from app.keyboards.inline import inline_main_menu
from app.keyboards.reply import reply_start_order, reply_send_location
from utils.callback_data import BranchesCallbackData, MainMenuAction, MainMenuCallbackData
from app.utils.states import OrderStateGroup

router = Router()



@router.callback_query(CategoryCallbackData.filter(F.action == CategoryAction.NEWS))
async def show_news(callback_query: types.CallbackQuery, callback_data: CategoryCallbackData):
    photo_url = "https://static.dw.com/image/69243161_605.jpg"
    # Correct function call and pass required arguments
    await callback_query.message.answer_photo(
        photo_url,
        caption="🚀 Yangiliklar",
        reply_markup=await show_news_inline(callback_query.message, callback_query.bot.get('session'))  
    )