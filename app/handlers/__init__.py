from .commands import router as commands_router
from .about import router as about_router
from .send_location import router as send_location
from .start_order import router as start_order
from .registration import router as registration
from .branchs import router as branches
from .new import router as new
from .admin import router as admin

def setup_handlers(dp):
    dp.include_router(commands_router)
    dp.include_router(send_location)

    dp.include_router(start_order)

    dp.include_router(about_router)

    dp.include_router(registration)
    dp.include_router(branches)
    dp.include_router(new)
    dp.include_router(admin)
    
