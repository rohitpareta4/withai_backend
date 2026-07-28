from pwdlib import PasswordHash

password_hash=PasswordHash.recommended()

def hashpass(password:str) -> str:
    return password_hash.hash(password)


def verify_pass(plainpass:str,hashpass:str) -> bool:
    return password_hash.verify(plainpass,hashpass)