from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_send_phone_number():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Send phone", request_contact=True)

    return reply_keyboard.as_markup()


def reply_start_order():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Eltib berish")
    reply_keyboard.button(text="Borib olish")
    reply_keyboard.button(text="Orqaga")

    reply_keyboard.adjust(2)

    return reply_keyboard.as_markup(resize_keyboard=True)


def reply_send_location():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Lokatsiya jo`natish", request_location=True)
    reply_keyboard.button(text="Orqaga")

    return reply_keyboard.as_markup(resize_keyboard=True)



def yes_or_no():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Ha")
    reply_keyboard.button(text="Yo'q")

    return reply_keyboard.as_markup(resize_keyboard=True)





def admin_panel_keyboard():
    reply = ReplyKeyboardBuilder()
    reply.button(text="Yangi mahsulot qo'shish")
    reply.button(text="Mahsulotlar")

    return reply.as_markup(resize_keyboard=True)