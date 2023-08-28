from typing import Tuple
from starlette.authentication import AuthCredentials, AuthenticationBackend, AuthenticationError
from starlette.requests import HTTPConnection
from .data import collection
from .models import UserRecord
from pymongo.collection import Collection

class TokenAuthentication(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection) -> Tuple[AuthCredentials, UserRecord] | None:
        if "Token" not in conn.headers:
            return
        token = conn.headers["Token"]
        def inner(users:Collection):
            userDocument = users.find_one({"token": token})
            if userDocument:
                return UserRecord(**userDocument)
            else:
                return None
        user:UserRecord|None = collection("users", inner)
        if user is None:
            raise AuthenticationError("Invalid credentials")

        return AuthCredentials(user.permissions), user