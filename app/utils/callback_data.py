from enum import Enum
from aiogram.filters.callback_data import CallbackData


class MainMenuAction(str, Enum):
    ORDER = 'order'
    ABOUT = 'about'
    MY_ORDERS = 'my_orders'
    BRANCHES = 'branches'
    SETTINGS = 'settings'


class MainMenuCallbackData(CallbackData, prefix='main_menu'):
    action: MainMenuAction

class BranchesAction(str, Enum):
    SHOW = 'show'        
    SELECT = 'select'
    NEXT = 'next'
    BACK = 'back'


class BranchesCallbackData(CallbackData, prefix='branches'):
    action: BranchesAction
    branch_id: int | None = None  
    page: int | None = None





def cb_main_menu_callback_data(action):
    return MainMenuCallbackData(action=action.value).pack()


class BackToMainMenuAction(str, Enum):
    BACK = 'back'


class BackToMainMenuCallbackData(CallbackData, prefix='back_main_menu'):
    action: BackToMainMenuAction


def cb_back_to_main_menu_callback_data():
    return BackToMainMenuCallbackData(action=BackToMainMenuAction.BACK.value).pack()


class SelectLanguage(str, Enum):
    UZ = 'uz'
    RU = 'ru'
    EN = 'en'


class SelectLanguageCallbackData(CallbackData, prefix='select_language'):
    language: SelectLanguage


def cb_select_language_callback_data(lang):
    return SelectLanguageCallbackData(language=lang.value).pack()

class CategoryAction(str, Enum):
    NEWS = '🆕YANGILIKLAR'    
    DUETLAR = 'duetlar'
    BURGER = 'burger'
    PIZZA = 'pizza'
    SENDVICH = 'sendvich'
    KATTA_PITSA = 'katta_pitsa'
    YAXNA_KOFE = 'yaxna_kofe'
    SHIRINLIKLAR = 'shirinliklar'
    LAVASHLAR = 'lavashlar'
    DONARLAR = 'donarlar'
    SOUSLAR = 'souslar'
    SALATLAR = 'salatlar'
    SNEKLAR = 'sneklar'
    MAIN_MENU = 'asosiy_menu'


class CategoryCallbackData(CallbackData, prefix='category'):
    action: CategoryAction


def cb_category_callback_data(action):
    return CategoryCallbackData(action=action.value).pack()


class YesORNoAction(str, Enum):
    YES = 'yes'
    NO = 'no'


class YesORNoCallbackData(CallbackData, prefix='yes_or_no'):        
    action: YesORNoAction   