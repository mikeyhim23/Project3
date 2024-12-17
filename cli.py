import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Category,Products


DATABASE_URL = 'sqlite:///products.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print('Initializing database')


def create_category():
    name = input('Enter the Category name:')
    description = input('Type the description of the category:')
    category = Category(name=name, description=description)
    session.add(category)
    session.commit()
    print (f'Category "{name}" created with ID {category.id}' )