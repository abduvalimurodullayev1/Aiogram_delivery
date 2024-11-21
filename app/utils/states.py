from aiogram.fsm.state import StatesGroup, State


class RegistrationStateGroup(StatesGroup):
    language = State()
    phone = State()
    name = State()


class OrderStateGroup(StatesGroup):
    order_type = State()
    send_location = State()
    confirm_location = State()
    category = State()
    


class MenuStateGroup(StatesGroup):
    name = State()
    image = State()
    description = State()
    price = State()
    
    
    

class DeleteProductStateGroup(StatesGroup):
    confirm = State()