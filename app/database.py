from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from urllib.parse import quote_plus

USERNAME = "root"
PASSWORD = quote_plus("Shilpa@2004")
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "food_delivery"

DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()