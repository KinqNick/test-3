from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from src.database.connection import Session

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, quantity={self.quantity})>"

Base.metadata.create_all(Session.bind)