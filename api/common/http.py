from typing import TypeVar
from fastapi import FastAPI, Request, Response
from fastapi.exceptions import HTTPException
from .data import collection
from .models import UserWithPassword
from pymongo.collection import Collection

def not_success(status_code:int, detail:str = None):
    raise HTTPException(status_code, detail or 'Bobo')

def not_found(detail:str = None):
    return not_success(404, detail)

def bad_request(detail:str = None):
    return not_success(400, detail)

T = TypeVar("T")
def value_or_not_found(value:T) -> T|None:
    return value or not_found()

def value_or_bad_request(value:T) -> T|None:
    return value or bad_request()


def validate_user(api:FastAPI) -> FastAPI:
    async def inner(request:Request, call_next):
        def get_user(collection:Collection):
            token:str = request.headers.get("Token") or ""
            document = collection.find_one({"token": token})
            return UserWithPassword(**document) if document else None 
        print(collection("users", get_user))
        response:Response = await call_next(request)
        return response
    api.middleware("http")(inner)
    return api

def configure_cors(api:FastAPI) -> FastAPI:
    async def inner(request:Request, call_next):
        response:Response = Response() if request.method == "OPTIONS" else await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = '*'
        response.headers["Access-Control-Allow-Methods"] = 'GET, POST, OPTIONS'
        response.headers["Access-Control-Allow-Headers"] = '*'
        return response
    api.middleware("http")(inner)
    return api