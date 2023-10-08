import models
# # # test method 1
# customers = models.list_all_clients()
# for customer in customers:
#     print(f"{customer.first_name} {customer.last_name}")

# #Test Method 2: List all cars
# cars = models.list_all_cars()
# print("\nList of all cars:")
# for car in cars:
#     print(f"Car: {car.name}, Rental Price: {car.price}")

# # Test Method 3: List all reviews
# reviews = models.list_all_reviews()
# for review in reviews:
#     print(f"Review ID: {review.id}, Star Ratings: {review.star_ratings}")

# # Test Method 4: List all reviews per customer Enter the customer id when prompted
# customer_id = input('Enter Customer ID: ')
# print(f"\nList of reviews for customer {customer_id}:")
# customer_reviews = models.list_reviews_by_customer(customer_id)

# if customer_reviews is None:
#     print("No reviews found for this customer.")
# else:
#     for review in customer_reviews:
#         print(f"Review ID: {review.id}, Star Ratings: {review.star_ratings}, Car Name: {review.car_name}")

# # Test method 5: List all cars used by a customer
# customer_id = 7  # Replace with the desired customer ID

# # Call the list_cars_used_by_customer method
# cars_used_by_customer = models.list_cars_used_by_customer(customer_id)

# # Check if the customer exists and has used cars
# if cars_used_by_customer:
#     print(f"Cars used by customer with ID {customer_id}:")
#     for car in cars_used_by_customer:
#         print(f"Car ID: {car.id}, Name: {car.name}, Price: {car.price}")
# else:
#     print(f"No cars found for customer with ID {customer_id}")


# # Test Method 6: List average restaurant review per user
# average_reviews_per_user = models.list_average_review_per_user()
# for user_id, average_rating in average_reviews_per_user:
#     print(f"User ID: {user_id}, Average Rating: {average_rating}")


# # # Test Method 7: Add a car with name and price
# car_name = input("Please enter a car name: ")
# car_price = int(input("Please enter a car price: "))
# new_car = models.add_car(car_name, car_price)
# print(f"Added Car ID: {new_car.id}, Name: {new_car.name}, Price: {new_car.price}")

# # Test method 8: Add a client
# first_name = input("Please enter a client's first name: ")
# last_name = input("Please enter a client's last name: ")
# new_client = models.add_client(first_name, last_name)
# print(f"Added Client ID: {new_client.id}, First Name: {new_client.first_name}, Last Name: {new_client.last_name}")

# # Test method 9: Delete a car
# def delete_a_car():

#     car_to_delete = input("Enter a car ID to delete: ")

# # Check if the car ID exists in the database
#     if models.car_exists(car_to_delete):
#         models.delete_car_by_id(car_to_delete)
#         print(f"Car with ID {car_to_delete} has been deleted successfully.")
#     else:
#         print(f"Invalid car ID: ID {car_to_delete} does not exist in the database. Try again")
#         delete_a_car()

# delete_a_car()

# # Test method 10: delete a client by id
# def delete_a_client():

#     client_to_delete = input("Enter a client ID to delete: ")

#     # Check if the client ID exists in the database
#     if models.client_exists(client_to_delete):
#         models.delete_client_by_id(client_to_delete)
#         print(f"Client with ID {client_to_delete} has been deleted successfully.")
#     else:
#         print(f"Invalid client ID: ID {client_to_delete} does not exist in the database. Try again")
#         delete_a_client()

# delete_a_client()

# # Test method 11: Add feedback
# star_ratings = int(input("Enter star ratings (1-5): "))
# car_id = int(input("Enter car ID: "))
# client_id = int(input("Enter client ID: "))

# feedback = models.add_feedback(star_ratings, car_id, client_id)
# print(f"Feedback ID {feedback.id} added successfully.")

# method 12: Searching for cars by name or part of a name
# car_name = input("Enter car name to search for: ")
# found_cars = models.search_cars_by_name(car_name)
# if found_cars:
#     for car in found_cars:
#         print(f"Car name: {car.name}, Price: ${car.price}")
# else:
#     print("No cars found with the given name.")

# method 12: Searching for clients by name
client_name = input("Enter a client name to search: ")
found_clients = models.search_clients_by_name(client_name)
if found_clients:
    for client in found_clients:
        print(f"Client ID: {client.id}, First Name: {client.first_name}, Last Name: {client.last_name}")
else:
    print("No clients found with the given name.")












