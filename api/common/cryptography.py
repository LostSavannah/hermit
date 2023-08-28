import random
import uuid
import hashlib

def get_pool(a:int, b:int, exclude:list[int] = None) -> str:
    return ''.join([chr(i) for i in range(a, b) if i not in (exclude or [])])

def generate_code(len:int = 8, pool:str = "1234567890") -> str:
    return ''.join([random.choice(pool) for i in range(len)])

def get_hash(data:str) -> str:
    return hashlib.md5(data.encode()).hexdigest()

def create_salt() -> str:
    return generate_code(8, get_pool(65, 126))

def generate_password_hash_and_salt(raw_password:str) -> tuple[str, str]:
    salt = create_salt()
    password_hash = hash_raw_password_plus_salt(raw_password, salt)
    return password_hash, salt

def hash_raw_password_plus_salt(raw_password, salt) -> str:
    return get_hash(raw_password + salt)

def generate_uuid() -> str:
    return str(uuid.uuid4())

def generate_token() -> str:
    return generate_uuid()