from pydantic import BaseModel

class Code(BaseModel):
    code: str

class FileHandler(Code):
    path: str
    owner: str

class UploadFileRequest(BaseModel):
    content: str

class Product(BaseModel):
    name: str
    description: str
    unit_volume: float
    unit_weight: float

class ProductRecord(Code, Product):
    pass

class Location(BaseModel):
    name: str
    latitude: float
    longitude: float
    altitude: float
    admin: str
    managers: list[str]

class LocationRecord(Code, Location):
    pass

class UserRequest(BaseModel):
    name: str
    password: str

class UserRecord(BaseModel):
    code: str
    name: str
    permissions: list[str]
    roles: list[str]
    status: int

class UserWithPassword(UserRecord):
    token: str
    password_hash: str
    password_salt: str

class RoomType(BaseModel):
    location: str
    name: str
    photo: str
    features: list[str]

class RoomTypeRecord(Code, RoomType):
    pass