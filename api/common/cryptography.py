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

#I have no actual clue of how that works. Thanks to https://stackoverflow.com/users/391531/nmichaels
#Answered in https://stackoverflow.com/questions/8539441/private-public-encryption-in-python-with-standard-library

def gen_prime(n=10**8, bases=range(2, 20000)):
    p = 1
    while any(pow(base, p-1, p) != 1 for base in bases):
        p = random.SystemRandom().randrange(n)
    return p

def get_multiplicative_inverse(modulus, value):
    x, last = 0, 1
    a, b = modulus, value
    while b:
        a, q, b = b, a // b, a % b
        x, last = last - q * x, x
    result = (1 - last * modulus) // value
    return result + modulus if result < 0 else result

def keygen(n:int = 10**8, e:int = 65537):
    prime1 = gen_prime(n)
    prime2 = gen_prime(n)
    totient = (prime1 - 1) * (prime2 - 1)
    return prime1 * prime2, get_multiplicative_inverse(totient, e)