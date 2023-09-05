# from models.reviews import Customer, Review, Restaurant, Base
# from sqlalchemy import func, MetaData
# from sqlalchemy import create_engine, engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.reviews import Customer, Review, Restaurant, Base
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()




customer1 = Customer(
    first_name = 'Matthew', 
    family_name = 'Tentacles'
    )
customer2 = Customer(
    first_name = 'Teresa', 
    family_name = 'Cheeks'
    )
customer3 = Customer(
    first_name = 'Sandy', 
    family_name = 'Cheeks'
    )
customer4 = Customer(
    first_name = 'Squidward', 
    family_name = 'Tentacles'
    )






engine = create_engine('sqlite:///reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

Customer.metadata.create_all(engine)
Review.metadata.create_all(engine)
Restaurant.metadata.create_all(engine)








restaurant1 = Restaurant(name = 'Pizza Place', price=1750)
restaurant2 = Restaurant(name = 'Burger Joint', price=2500)
restaurant3 = Restaurant(name = 'Krusty Krab', price=3700)
restaurant4 = Restaurant(name = 'Chum Bucket', price=1400)


customer1.add_review(session=session, restaurant_name=restaurant3.name, rating=5)
customer3.add_review(session=session, restaurant_name=restaurant2.name, rating=3)
customer3.add_review(session=session, restaurant_name=restaurant1.name, rating=4)
customer3.add_review(session=session, restaurant_name=restaurant3.name, rating=7)
customer2.add_review(session=session, restaurant_name=restaurant3.name, rating=4)
customer1.add_review(session=session, restaurant_name=restaurant1.name, rating=5)
customer4.add_review(session=session, restaurant_name=restaurant3.name, rating=6)
customer1.add_review(session=session, restaurant_name=restaurant4.name, rating=1)
customer4.add_review(session=session, restaurant_name=restaurant2.name, rating=2)
customer3.add_review(session=session, restaurant_name=restaurant4.name, rating=2)

session.commit()

print("Customers:")
for customer in session.query(Customer).all():
    print(f"{customer.get_full_name()}")

print("\nReviews:")
for review in session.query(Review).all():
    print(f"Customer: {review.customer.get_full_name()}, Restaurant: {review.restaurant.name}, Rating: {review.rating}")

print("\nRestaurant Average Ratings:")
for restaurant in session.query(Restaurant).all():
    print(f"Restaurant: {restaurant.name}, Average Rating: {restaurant.average_star_rating()}")

print("\n Fanciest Restaurants:")
fanciest_restaurant = Restaurant.fanciest(session)
print(f"The fanciest restaurant is: {fanciest_restaurant.name}")

reviews = restaurant.get_reviews(session)
for review in reviews:
    print(review)
session.close()

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
    print(f"Customer ID: {review.customer}, Restaurant: {review.restaurant_name}, Rating: {review.rating}")

session.close()



