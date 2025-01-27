from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    _instance = None
    _engine = None
    _SessionLocal = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._setup()
        return cls._instance

    @classmethod
    def _setup(cls):
        DATABASE_URL = os.getenv("DATABASE_URL")
        cls._engine = create_engine(DATABASE_URL)
        cls._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._engine)

    def get_session(self):
        return self._SessionLocal()

Base = declarative_base()
db_instance = Database()
