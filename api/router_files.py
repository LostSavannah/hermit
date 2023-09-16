import os
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from common.http import value_or_bad_request, value_or_not_found, bad_request
from common.data import collection
from common.models import FileHandler, UserRecord, UploadFileRequest
from pymongo.collection import Collection
from uuid import uuid4

files_root = os.environ.get("HERMIT_FILES_ROOT")
print(files_root)

router = APIRouter(tags=["files"])

@router.get("/{code}")
async def get_file_by_code(code:str):
    def inner(files:Collection):
        fileDocument = value_or_not_found(files.find_one({"code": code}))
        return FileHandler(**fileDocument).path
    fileName:str = os.sep.join([files_root, collection("files", inner)])
    return FileResponse(fileName)

@router.patch("/{code}")
async def patch_file(code:str, upload_file_request:UploadFileRequest, request:Request):
    def inner(files:Collection):
        code = str(uuid4())
        path = str(uuid4())
        owner:UserRecord = value_or_bad_request(request.user)
        fileHandler:FileHandler = value_or_not_found(files.find_one({"code": code}))
        if fileHandler.owner != owner.code:
            return bad_request()
        with open(os.sep.join([files_root, path]), 'w') as fo:
            fo.write(upload_file_request.content)
        return fileHandler
    return collection("files", inner)

@router.post("/")
async def post_file(upload_file_request:UploadFileRequest, request:Request):
    def inner(files:Collection):
        code = str(uuid4())
        path = str(uuid4())
        owner:UserRecord = value_or_bad_request(request.user)
        fileHandler:FileHandler = FileHandler(code=code, path=path, owner=owner.code)
        with open(os.sep.join([files_root, path]), 'w') as fo:
            fo.write(upload_file_request.content)
        files.insert_one({**dict(fileHandler)})
        return fileHandler
    return collection("files", inner)

@router.delete("/{code}")
async def delete_file(code:str, request:Request):
    def inner(files:Collection):
        owner:UserRecord = value_or_bad_request(request.user)
        fileDocument = value_or_not_found(files.find_one({"code": code}))
        fileHandler:FileHandler = FileHandler(**fileDocument)
        if owner.code != fileHandler.owner:
            return bad_request()
        filename:str = os.sep.join([files_root, fileHandler.path])
        os.unlink(filename)
        files.delete_one({"code": code})
        return fileHandler
    return collection("files", inner)


