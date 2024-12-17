import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Category,Products


DATABASE_URL = 'sqlite:///products.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

