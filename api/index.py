from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware
from common.http import configure_cors
from common.authentication import TokenAuthentication
from router_users import router as usersRouter
from router_files import router as files_router


api:FastAPI = configure_cors(FastAPI())

api.add_middleware(AuthenticationMiddleware, backend=TokenAuthentication())

api.include_router(usersRouter, prefix="/users")
api.include_router(files_router, prefix="/files")

@api.get('/')
def home():
    return 'active'