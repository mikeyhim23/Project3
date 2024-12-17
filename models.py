from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer,primary_key= True)
    name = Column(String, nullable=False)
    description = Column(String, unique=True,nullable=False)

    products = relationship('Product',back_populates="categories")

    def __repr__(self):
        return f"Category(id = {self.id}, name= '{self.name}', description= '{self.description}')"
    
class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category',back_populates='products')

    def __repr__ (self):
        return f"Products(id = {self.id}, name = '{self.name}',  price= {self.price},  quantity = '{self.quantity}' , category_id = {self.category_id})"
    