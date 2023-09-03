from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Reviews, Restaurant


engine = create_engine('sqlite:///reviews.db')

Customer.metadata.create_all(engine)
Reviews.metadata.create_all(engine)
Restaurant.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


customer1 = Customer(first_name = 'Matthew', family_name = 'Tentacles')
customer2 = Customer(first_name = 'Teresa', family_name = 'Cheeks')
customer3 = Customer(first_name = 'Sandy', family_name = 'Cheeks')
customer4 = Customer(first_name = 'Squidward', family_name = 'Tentacles')

restaurant1 = Restaurant(name = 'Pizza Place')
restaurant2 = Restaurant(name = 'Burger Joint')
restaurant3 = Restaurant(name = 'Krusty Krab')
restaurant4 = Restaurant(name = 'Chum Bucket')


customer1.add_review(restaurant3, 5)
customer3.add_review(restaurant2, 3)
customer3.add_review(restaurant1, 4)
customer3.add_review(restaurant3, 7)
customer2.add_review(restaurant3, 4)
customer1.add_review(restaurant1, 5)
customer4.add_review(restaurant3, 6)
customer1.add_review(restaurant4, 1)
customer4.add_review(restaurant2, 2)
customer3.add_review(restaurant4, 2)

session.commit()

print("Customers:")
for customer in session.query(Customer).all():
    print(f"{customer.get_full_name()}")

print("\nReviews:")
for review in session.query(Reviews).all():
    print(f"Customer: {review.customer.get_full_name()}, Restaurant: {review.restaurant.name}, Rating: {review.rating}")

print("\nRestaurant Average Ratings:")
for restaurant in session.query(Restaurant).all():
    print(f"Restaurant: {restaurant.name}, Average Rating: {restaurant.average_star_rating()}")


session.close()
