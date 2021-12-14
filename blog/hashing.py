from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    """ Hashes user password """
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    """ Compare hashed with plain password """
    def verify(hashed_p, plain_p):
        return pwd_cxt.verify(plain_p, hashed_p)
