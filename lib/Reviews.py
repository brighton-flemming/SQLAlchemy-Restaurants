from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    restaurant_name = Column(String)
    rating = Column(Integer)

    def __init__(self, customer_name, restaurant_name, rating):
        self.customer_name = customer_name
        self.restaurant_name = restaurant_name
        self.rating = rating


engine = create_engine('sqlite:///reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
