import secrets #python generates cryptographically strong random values
from cryptography.fernet import Fernet
from pathlib import Path

KEY_FILE=Path(__file__).parent / "master.key"


if KEY_FILE.exists():
    MASTER_KEY = KEY_FILE.read_bytes()

else: 
    MASTER_KEY = Fernet.generate_key() #generate a master key
    KEY_FILE.write_bytes(MASTER_KEY)

#convert the master key from bytes to python string (str)
MASTER_KEY = MASTER_KEY.decode("utf-8")

def generate_data_key(): #generates a new key for each password
    DATA_KEY = secrets.token_urlsafe(32)
    return DATA_KEY 

