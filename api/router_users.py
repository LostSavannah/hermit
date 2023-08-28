from fastapi import APIRouter
from common.http import not_success
from common.data import collection
from common.models import UserRecord, UserWithPassword, UserRequest
from common.cryptography import generate_password_hash_and_salt, generate_token, generate_uuid, hash_raw_password_plus_salt
from pymongo.collection import Collection

router = APIRouter(tags=["Users"])

@router.get("/")
def get_items():
    def get(collection:Collection):
        return [UserRecord(**i) for i in collection.find()]
    return collection("users", get)

@router.post("/")
def create_user(user:UserRequest):
    def create(collection:Collection):
        matches = collection.count_documents({"name": user.name})
        if matches:
            not_success(400, f"username {user.name} already in use")
        hash, salt = generate_password_hash_and_salt(user.password)
        userRecord = UserRecord(
            code=generate_uuid(), 
            name=user.name, 
            permissions=[], 
            roles=[], 
            status=1
        )
        userToInsert = UserWithPassword(
            **dict(userRecord),
            password_hash=hash, 
            password_salt=salt, 
            token=generate_token()
        )
        collection.insert_one({**dict(userToInsert)})
        return userRecord
    return collection("users", create)

@router.post("/login")
def login(user:UserRequest):
    def funct(collection:Collection):
        document = collection.find_one({"name": user.name})
        if (document):
            result = UserWithPassword(**dict(document))
            hash = hash_raw_password_plus_salt(user.password, result.password_salt)
            if hash == result.password_hash:
                token = generate_token()
                result.token = token
                collection.update_one({"code": result.code}, {"$set" : {**dict(result)}})
                return {
                    "token": token,
                    "name": result.name
                }
        return not_success(400, "Invalid credentials")
    return collection("users", funct)