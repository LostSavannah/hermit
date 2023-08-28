from fastapi import FastAPI
from common.http import configure_cors
from products import router as productsRouter
from locations import router as locationsRouter
from users import router as usersRouter

api:FastAPI = configure_cors(FastAPI())

api.include_router(usersRouter, prefix="/users")
api.include_router(locationsRouter, prefix="/locations")
api.include_router(productsRouter, prefix="/products")

@api.get('/')
def home():
    return 'active'