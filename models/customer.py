from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    family_name = Column(String)

    reviews = relationship("Review", back_populates="customer")

    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def add_review(self, restaurant_name, rating):
        review = Review(customer=self, restaurant_name=restaurant_name, rating=rating)
        self.reviews.append(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, session, first_name):
        return session.query(Customer).filter_by(first_name=first_name).first()

    @classmethod
    def find_by_family_name(cls, session, family_name):
        return session.query(Customer).filter_by(family_name=family_name).first()

    def restaurants(self):
        reviewed_restaurants = set(review.restaurant_name for review in self.reviews)
        return list(reviewed_restaurants)

    def get_given_name(self):
        return self.first_name

    def get_family_name(self):
        return self.family_name

    def get_full_name(self):
        return f"{self.get_given_name()} {self.get_family_name()}"

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
