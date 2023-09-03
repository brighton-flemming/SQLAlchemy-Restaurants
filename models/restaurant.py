from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    reviews = relationship("Reviews", back_populates="restaurant")

    def __init__(self, name):
        self.name = name  

    def average_star_rating(self, session):
        reviews = session.query(Review).filter_by(restaurant=self).all()

        if not reviews:
            return None

        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / len(reviews)
        return average_rating
    
    def get_reviews(self, session):
        return session.query(Review).filter_by(restaurant = self).all()
    
    def get_customers(self, session):
        reviews = session.query(Review).filter_by(restaurant = self).all()
        customers = set([review.customer for review in reviews])
        return list(customers)
    

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Integer)

    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

engine = create_engine('sqlite:///reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


