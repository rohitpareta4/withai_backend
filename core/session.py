from sqlalchemy.orm import sessionmaker
from core.database import engine

SessionLocal=sessionmaker(bind=engine)