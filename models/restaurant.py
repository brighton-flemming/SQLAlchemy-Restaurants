from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'


    id = Column(Integer, primary_key=True)
    name = Column(String)

    reviews = relationship("Reviews", back_populates="restaurant")

    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name
    
    def get_customers(self):
        session = Session()
        customers = [review.customer for review in session.query(Reviews).filter_by(restaurant=self).all()]
        session.close()
        return list(set(customers))
    
    def get_reviews(self):
        session  = Session()
        reviews = session.query(Reviews).filter_by(restaurant=self).all()
        session.close()
        return reviews
    
    def average_star_rating(self):
        session = Session()
        reviews = session.query(Reviews).filter_by(restaurant=self).all()
        session.close()

        if not reviews:
            return 0
        
        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / len(reviews)
        return average_rating
        


class Reviews(Base):
    __tablename__ = 'reviews'
    

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
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