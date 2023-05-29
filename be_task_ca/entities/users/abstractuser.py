import uuid
import hashlib


class AbstractUser:
    def __init__(self, email: str, id: uuid.UUID = None, raw_password: str = None, hashed_password: str = None):
        self.id = id if id else uuid.uuid4()
        self.email = email
        if raw_password and hashed_password:
            raise ValueError("Cannot set both raw_password and hashed_password")
        if not raw_password and not hashed_password:
            raise ValueError("Must set either raw_password or hashed_password")
        self.hashed_password = hashed_password if hashed_password else hashlib.sha512(
            raw_password.encode("UTF-8")
        ).hexdigest()
