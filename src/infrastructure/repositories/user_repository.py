from src.domain.entities.user import User
from src.domain.interfaces.i_user_repository import UserRepository
from src.infrastructure.database import db_instance
from sqlalchemy.exc import IntegrityError

class UserRepositoryImpl(UserRepository):
    def __init__(self):
        self.db = db_instance.get_session()

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user: User) -> User:
        existing = self.get_user_by_email(user.email)
        if existing:
            return None

        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            return None
