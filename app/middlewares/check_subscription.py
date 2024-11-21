from aiogram.types import  InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.utils.callback_data import cb_back_to_main_menu_callback_data, cb_main_menu_callback_data, \
    cb_select_language_callback_data, cb_category_callback_data
from app.utils.callback_data import *

# Asosiy menyuga qaytish tugmasi
def inline_back_to_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Asosiy menu', callback_data=cb_back_to_main_menu_callback_data())
    return inline_keyboard.as_markup()

# Asosiy menyu
def inline_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='🏠️️ Buyurtma berish', callback_data=cb_main_menu_callback_data(action=MainMenuAction.ORDER))
    inline_keyboard.button(text='Biz haqimizda', callback_data=cb_main_menu_callback_data(action=MainMenuAction.ABOUT))
    inline_keyboard.button(text='Buyurtmalarim', callback_data=cb_main_menu_callback_data(action=MainMenuAction.MY_ORDERS))
    inline_keyboard.button(text='Filiallar', callback_data=cb_main_menu_callback_data(action=MainMenuAction.BRANCHES))
    inline_keyboard.button(text='Sozlamalar', callback_data=cb_main_menu_callback_data(action=MainMenuAction.SETTINGS))

    inline_keyboard.adjust(2)

    return inline_keyboard.as_markup()

# Foydalanuvchini obuna bo'lishga chaqirish uchun tugma
def inline_subscribe():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Obuna bo\'lish', url='https://t.me/Chatgpt_developer')

    return inline_keyboard.as_markup()

# Tilni tanlash tugmasi
def inline_languages():
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='O\'zbekcha', callback_data=cb_select_language_callback_data(lang=SelectLanguage.UZ))
    inline_keyboard.button(text='Ruscha', callback_data=cb_select_language_callback_data(lang=SelectLanguage.RU))
    inline_keyboard.button(text='Inglizcha', callback_data=cb_select_language_callback_data(lang=SelectLanguage.EN))

    inline_keyboard.adjust(1)

    return inline_keyboard.as_markup()

# Filiallar bo'yicha navigatsiya
def branches_build(page: int = 0, page_size: int = 4):
    inline_keyboard = InlineKeyboardBuilder()
    branch_names = [
        'Algoritm', 'Andalus', 'Andijon1', 'Andijon2', 'Aviasozlar bozori', 'Bahodir', 'Beruniy', 'Bodomzor', 
        'Bodomzor2', "Bo'ka", "Chig'atoy", "Chilonzor", "Chilonzor savdo markazi", "Chilonzor19", "Chinoz", 
        "Cho'pon ota", "Chorbog'", "Chorsu", "Chirchiq", "Compass mail", "Depo Mail", "Do'mbirobod", "Erkin", 
        "Farg'ona 1", "Farg'ona 2", "Farhod bozori", "Feruza", "G'azalkent", "Golden Life Mail", "Gulzor", 
        "Ibn Sino", "Ipodrom bozori", "Ko'ksaroy", "Lisunova", "Lisunova2 Drive", "LunaChariskiy markazi", 
        "Magic City", "Majnuntol", "Maksim Gorkiy", "Marg'ilon", "Markaz-5", "Minor", "Namangan1", "Namangan2", 
        "Namangan3", "Nukus", "Nazarbek", "Nukus", "Nukus2", "Nurafshon", "OLOOSS Test", "Olmailiq1", "Olmaliq2", 
        "Oqtepa Maydoni", "Oxunboboyev", "Parkent", "Piskent", "Qatortol", "Qo'qon 1", "Qo'qon2", "Qoraqamish", 
        "Qorasuv1", "Qorasuv2", "Qo'yliq1", "Qo'yliq2", "Qushbegi", "Qutbiniso", "Rakat", "Risoviy Bozor", 
        "Riviera", "Samarqan3", "Samarqand Bulvar", "Samarqand Familiy Park", "Sergeli2", "Sergeli8", 
        "Shifokorlar shaharchasi", "Shuhrat", "ToshMi", "TTZ", "Urganch", "Vatan", "Vodnik", "Westminster", 
        "Xadr", "Xalqlar Do'stligi", "Yangibozor", "Yangihayot 5-bekat", "Yangiyo'l1", "Yangiyo'l2", "Yangiyo'l3", 
        "Yunusobod", "Yunusobod 5-mavze", "Zangiota"
    ]

    start = page * page_size
    end = start + page_size
    current_page_branches = branch_names[start:end]

    for branch in current_page_branches:
        inline_keyboard.button(text=branch, callback_data=f"branch:{branch}")

    if page > 0:
        inline_keyboard.button(
            text="Orqaga",
            callback_data=BranchesCallbackData(action=BranchesAction.BACK, page=page - 1).pack()
        )

    if end < len(branch_names):
        inline_keyboard.button(
            text="Keyingi",
            callback_data=BranchesCallbackData(action=BranchesAction.NEXT, page=page + 1).pack()
        )

    return inline_keyboard.as_markup()

# Kategoriyalar bo'yicha navigatsiya
def generate_category_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="🆕YANGILIKLAR", callback_data=cb_category_callback_data(CategoryAction.NEWS)),
        InlineKeyboardButton(text="Duetlar", callback_data="duetlar"),
    )

    builder.row(
        InlineKeyboardButton(text="🍖 Barakali setlar", callback_data="barakali_setlar"),
        InlineKeyboardButton(text="🌯 Lavashlar", callback_data=cb_category_callback_data(CategoryAction.LAVASHLAR)),
    )

    builder.row(
        InlineKeyboardButton(text="🍔 Burger va Hot-doglar", callback_data=cb_category_callback_data(CategoryAction.BURGER)),
        InlineKeyboardButton(text="🥙 Donarlar", callback_data=cb_category_callback_data(CategoryAction.DONARLAR)),
    )

    builder.row(
        InlineKeyboardButton(text="🥪 Sendvich", callback_data=cb_category_callback_data(CategoryAction.SENDVICH)),
        InlineKeyboardButton(text="🍟 Sneklar", callback_data=cb_category_callback_data(CategoryAction.SNEKLAR)),
    )

    builder.row(
        InlineKeyboardButton(text="🍕 Katta pitsalar", callback_data=cb_category_callback_data(CategoryAction.KATTA_PITSA)),
        InlineKeyboardButton(text="🥗 Salatlar", callback_data=cb_category_callback_data(CategoryAction.SALATLAR)),
    )

    builder.row(
        InlineKeyboardButton(text="☕ Yaxna kofe", callback_data=cb_category_callback_data(CategoryAction.YAXNA_KOFE)),
        InlineKeyboardButton(text="🍰 Shirinliklar", callback_data=cb_category_callback_data(CategoryAction.SHIRINLIKLAR)),
    )

    builder.row(
        InlineKeyboardButton(text="🍅 Souslar", callback_data=cb_category_callback_data(CategoryAction.SOUSLAR)),
        InlineKeyboardButton(text="🍹 Ichimliklar", callback_data=cb_category_callback_data(CategoryAction.ICHIMLIKLAR)),
    )

    builder.row(
        InlineKeyboardButton(text="🔙 Orqaga", callback_data=cb_back_to_main_menu_callback_data()),
    )

    return builder.as_markup()
