from typing import TypeVar
from fastapi import FastAPI, Request, Response
from fastapi.exceptions import HTTPException

def not_success(status_code:int, detail:str = None):
    raise HTTPException(status_code, detail or 'Bobo')

def not_found(detail:str = None):
    return not_success(404, detail)

T = TypeVar("T")
def value_or_not_found(value:T) -> T|None:
    return value or not_found()


def configure_cors(api:FastAPI) -> FastAPI:
    async def inner(request:Request, call_next):
        response:Response = Response() if request.method == "OPTIONS" else await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = '*'
        response.headers["Access-Control-Allow-Methods"] = 'GET, POST, OPTIONS'
        response.headers["Access-Control-Allow-Headers"] = '*'
        return response
    api.middleware("http")(inner)
    return api