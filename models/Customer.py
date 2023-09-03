from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    family_name = Column(String)



    reviews = relationship("Review", back_populates="customer")

    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name
        self.reviews = []

    def add_review(self, restaurant_name, rating):
        review = Review(customer=self, restaurant_name=restaurant_name, rating=rating)


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_name = Column(String)
    rating = Column(Integer)


    customer = relationship("Customer", back_populates="reviews")

    def __init__(self, customer, restaurant_name, rating):
        self.customer = customer
        self.restaurant_name = restaurant_name
        self.rating = rating

engine = create_engine('sqlite:///reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
