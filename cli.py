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
        print(f'Category with ID {category_id} doesn/t exist.')
        return
    category.name = input(f'Enter new name for Category (current: {category.name}):') or category.name
    category.description = input(f'Enter new description for Category (current: {category.description}):') or category.description

    session.commit()
    print(f'Category ID {category_id} updated successfully')


def delete_category():
    category_id = int(input('Enter Category ID to update: '))
    category = session.get(Category,category_id)
    if not category:
        print(f'Category with ID {category_id} doesn/t exist.')
        return
    session.delete(category)
    session.commit()
    print (f'Category ID {category_id} deleted successfully.')


def create_product():
    name = input('Enter product name:')
    price = int(input('Enter product price:'))
    quantity = input('Enter product quantity:')
    category_id = int(input('Enter Category ID:'))
    category = session.get(Category, category_id)
    if not category:
        print(f'Category with ID {category_id} doesn/t exist')
        return
    product = Products(name=name, print=price, quantity=quantity, category_id=category_id)
    session.add(product)
    session.commit()
    print(f'Product "{name}" created with ID {product.id} and assigned to Category_ID {category_id}')

def update_product():
    product_id = int(input('Enter Product ID to update:'))
    product = session.get(Products, product_id)

    if not product:
        print(f'Product with Id {product_id} does not exist')
        return
    product.name = input('Enter new name for product (current: {product.name}):') or product.name
    product.price = input('Enter new price for product (current: {product.price}):') or product.price
    product.quantity = input('Enter new quantity for product (current: {product.quantity}):') or product.quantity
    new_category_id = input(f'Enter new Category ID for product (current: {product.category_id}):') or product.category_id
    if new_category_id:
        new_category = session.get(Category, int(new_category_id))
        if not new_category:
            print (f'Category with ID {new_category_id} doesn/t exist. Skipping Ctegory update')
        
        else:
            product.category_id = new_category_id
    session.commit()
    print(f'Product ID {product_id} updated correctly')