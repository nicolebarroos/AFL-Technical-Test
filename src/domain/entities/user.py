from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = self.hash_password(password)
        self.created_at = datetime.utcnow()

    def hash_password(self, password):
        return pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
