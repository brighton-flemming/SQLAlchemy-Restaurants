from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()
engine = create_engine('sqlite:///reviews.db')
Session = sessionmaker(bind=engine)
session = Session()


class Customer(Base):
    __tablename__ = 'customers'

 
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    family_name = Column(String)

    reviews = relationship("Review", back_populates="customer", primaryjoin='Customer.id == Review.customer_id')

    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name


    def get_given_name(self):
         return self.first_name

    def get_family_name(self):
         return self.family_name

    def get_full_name(self):
         return f"{self.get_given_name()} {self.get_family_name()}"

   

    # def add_review(self, session, restaurant_name, rating):
        
    #     review = Review(customer=self, restaurant_name=restaurant_name, rating=rating)
    #     session.add(review)

    def add_review(self, session: sessionmaker, restaurant_name: str, rating: int):
        restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()

        if restaurant:
            review = Review(customer_id=self.id, restaurant_id=restaurant.id, rating=rating)
            session.add(review)
            session.commit()
        else:
            print(f"Restaurant '{restaurant_name}' not found.")

    def delete_reviews(self, session, restaurant_name):
        session.query(Review).filter_by(customer=self, restaurant_name = restaurant_name).delete()


    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, session, first_name):
        return session.query(Customer).filter_by(first_name=first_name).first()

    @classmethod
    def find_by_family_name(cls, session, family_name):
        return session.query(Customer).filter_by(family_name=family_name).first()

    def get_restaurants(self):
        reviewed_restaurants = set(review.restaurant_name for review in self.reviews)
        return list(reviewed_restaurants)

    
    def get_favourite_restaurant(self, session):
        max_rating = func.max(Review.rating).label('max_rating')
        subquery = (
            session.query(Review.restaurant_id, max_rating)
            .filter(Review.customer_id == self.id)
            .group_by(Review.restaurant_id)
        ).subquery()

        query = (
            session.query(subquery.c.restaurant_id)
            .filter(subquery.c.max_rating == subquery.c.max_rating.max())
        )

        favourite_restaurant_id = query.scalar()

        if favourite_restaurant_id is not None:
            favourite_restaurant = session.query(Restaurant).filter_by(id=favourite_restaurant_id).first()
            return favourite_restaurant

        return None 


    def get_reviews(self):
        return self.reviews

   


class Review(Base):
    __tablename__ = 'reviews'


    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id')) 
    restaurant_name = Column(String, ForeignKey('restaurants.id'))
    rating = Column(Integer)

    customer = relationship("Customer", back_populates="reviews", primaryjoin='Customer.id == Review.customer_id')
    restaurant = relationship("Restaurant", back_populates="reviews") 

    def __init__(self, customer, restaurant_name, rating):
        self.customer = customer
        self.restaurant_name = restaurant_name
        self.rating = rating

    
    # def full_review(self):
        # return f"Review for {self.restaurant_name} by {self.customer.get_full_name()}: {self.rating} stars."
    
    def __str__(self):
        customer_name = self.customer.get_full_name()
        restaurant_name = self.restaurant_name
        return f"Review for {restaurant_name} by {customer_name}: {self.rating} stars"


    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant
    

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, ForeignKey('restaurants.name'))
    price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")

    def __init__(self, name, price):
        self.name = name
        self.price = price
    

    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()  

    def average_star_rating(self):
        reviews = self.session.query(Review).filter_by(restaurant=self).all()

        if not reviews:
            return None

        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / len(reviews)
        return average_rating
    
    def get_reviews(self, session):
        reviews = session.query(Review).filter_by(restaurant = self).all()
        formatted_reviews = [
            f"Review for {self.name} by {review.customer.get_full_name()}: {review.rating} stars."
            for review in reviews
        ]
        return formatted_reviews


    def get_customers(self, session):
        reviews = session.query(Review).filter_by(restaurant = self).all()
        customers = set([review.customer for review in reviews])
        return list(customers)
    
    


customer = session.query(Customer).filter_by(id=3).first()
new_review = Review(customer=customer, restaurant_name='Krusty Krab', rating=4)
# formatted_review = new_review.full_review()
print(new_review)
session.add(new_review)
session.commit()

all_reviews = session.query(Review).all()

for review in all_reviews:
    print(f"Customer ID: {review.customer_id}, Restaurant: {review.restaurant_name}, Rating: {review.rating}")

session.close()




