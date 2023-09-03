from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.customer import Customer



Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id')) 
    restaurant_name = Column(String, ForeignKey('restaurant.id'))
    rating = Column(Integer)

    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews") 

    def __init__(self, customer, restaurant_name, rating):
        self.customer = customer
        self.restaurant_name = restaurant_name
        self.rating = rating

    def full_review(self):
        return f"REview for {self.restaurant_name} by {self.customer.get_full_name()}: {self.rating} stars."


    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant
    

    


engine = create_engine('sqlite:///reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
customer = session.query(Customer).filter_by(id=1).first()
new_review = Review(customer=customer, restaurant_name='Pizza Place', rating=5)
formatted_review = new_review.full_review()
print(formatted_review)
session.add(new_review)
session.commit()

all_reviews = session.query(Review).all()

for review in all_reviews:
    print(f"Customer ID: {review.customer_id}, Restaurant: {review.restaurant_name}, Rating: {review.rating}")

session.close()
