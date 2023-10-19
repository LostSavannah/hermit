from fastapi import APIRouter, Request
from common.http import not_success, value_or_bad_request
from common.data import collection
from common.models import LocationRecord, Location, UserRecord
from common.cryptography import generate_password_hash_and_salt, generate_token, generate_uuid, hash_raw_password_plus_salt
from pymongo.collection import Collection

router = APIRouter(tags=["Locations"])

@router.get("/")
def get_items():
    def get(collection:Collection):
        return [LocationRecord(**i) for i in collection.find()]
    return collection("locations", get)

@router.get("/mine")
def get_my_locations(request:Request):
    def get(collection:Collection):
        owner:UserRecord = value_or_bad_request(request.user)
        locations = [LocationRecord(**i) for i in collection.find()]
        return [l for l in locations if l.admin == owner.code]
    return collection("locations", get)

@router.post("/")
def create(location:Location):
    def create(collection:Collection):
        locationRecord = LocationRecord(
            **dict(location),
            code=generate_uuid()
        )
        collection.insert_one({**dict(locationRecord)})
        return locationRecord
    return collection("locations", create)