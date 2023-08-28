import os
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from common.http import value_or_not_found
from common.data import collection
from common.models import FileHandler
from pymongo.collection import Collection
from uuid import uuid4

files_root = os.environ.get("HERMIT_FILES_ROOT")

router = APIRouter(tags=["files"])

@router.get("/{code}")
async def get_file_by_code(code:str):
    def inner(files:Collection):
        fileDocument = value_or_not_found(files.find_one({"code": code}))
        return FileHandler(**fileDocument)
    fileName:str = os.sep.join([files_root, collection("files", inner)])
    return FileResponse(fileName)

@router.post("/")
async def post_file(request:Request):
    b:bytes = await request.body()
    def inner(files:Collection):
        code = str(uuid4())
        path = str(uuid4())
        owner = request.user.code
        fileHandler:FileHandler = FileHandler(code=code, path=path, owner="")
        with open(os.sep.join([files_root, path]), 'wb') as fo:
            fo.write(b)
        return fileHandler
    return collection("files", inner)