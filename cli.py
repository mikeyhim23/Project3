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

def update_category():
    category_id = int(input('Enter Category ID to update: '))
    category = session.get(Category,category_id)
    if not category:
        print(f'Category with ID {category_id}')
        return
    category.name = input(f'Enter new name for Category (current: {category.name}):') or category.name
    category.description = input(f'Enter new description for Category (current: {category.description}):') or category.description

    session.commit()
    print(f'Category ID {category_id} updated successfully')