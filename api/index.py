from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware
from common.http import configure_cors
from common.authentication import TokenAuthentication
from router_users import router as users_router
from router_files import router as files_router
from router_locations import router as locations_router

api:FastAPI = configure_cors(FastAPI())

api.add_middleware(AuthenticationMiddleware, backend=TokenAuthentication())

api.include_router(users_router, prefix="/users")
api.include_router(files_router, prefix="/files")
api.include_router(locations_router, prefix="/locations")

@api.get('/')
def home():
    return 'active'