import models

def feedback_menu():
    feedback_menu_prompt = '''
Please enter an option below to navigate through our feedback entries.

0. Main Menu
1. List all feedback entries
2. List average feedback score by client
3. List all feedback of a client by id
4. Go back one level
5. Exit
'''
    print (feedback_menu_prompt)
    option = int(input("Enter an option: "))

    if option == 1:
        reviews = models.list_all_reviews()
        for review in reviews:
            print(f"Review ID: {review.id}, Star Ratings: {review.star_ratings}")
        feedback_menu()


    elif option == 2:
        average_reviews_per_user = models.list_average_review_per_user()
        for user_id, average_rating in average_reviews_per_user:
            print(f"User ID: {user_id}, Average Rating: {average_rating}")
        feedback_menu()

    elif option == 3:
        customer_id = input('Enter Customer ID: ')
        print(f"\nList of reviews for customer {customer_id}:")
        customer_reviews = models.list_reviews_by_customer(customer_id)

        if customer_reviews is None:
            print("No reviews found for this customer.")
            feedback_menu()

        if not customer_reviews:
            print(f"No reviews found for customer with ID {customer_id}.")
            feedback_menu()
        else:
            for review in customer_reviews:
                print(f"Review ID: {review.id}, Star Ratings: {review.star_ratings}, Car Name: {review.car_name}")
            feedback_menu()

    elif option == 4:
        main_menu()
    
    elif option == 5:
        exit()

    elif option == 0:
        main_menu()

    
def cars_menu():
    cars_menu_prompt = '''
Please enter an option below to navigate through the our cars.

0. Main Menu
1. List all cars
2. Add a car
3. Delete a car
4. Go back one level
5. Exit
'''


    print(cars_menu_prompt)

    option = int(input("Enter an option: "))

    if option == 1:
        cars = models.list_all_cars()
        print("\nList of all cars:")
        for car in cars:
            print(f"Car: {car.name},Daily Rental Price: ${car.price}")
        cars_menu()

    elif option == 2:
        car_name = input("Please enter a car name: ")
        car_price = int(input("Please enter a car price: "))
        new_car = models.add_car(car_name, car_price)
        print(f"Added Car ID: {new_car.id}, Name: {new_car.name}, Price: {new_car.price}")
        cars_menu()
 
    elif option == 3:
        delete_a_car()
    elif option == 4:
        main_menu()
    elif option == 5:
        exit()
    elif option == 0:
        main_menu()
    else:
        print("Invalid option. Please try again.")
        cars_menu()

def delete_a_car():

    car_to_delete = input("Enter a car ID to delete: ")

# Check if the car ID exists in the database
    if models.car_exists(car_to_delete):
        models.delete_car_by_id(car_to_delete)
        print(f"Car with ID {car_to_delete} has been deleted successfully.")
        cars_menu()
    
    else:
        print(f"Invalid car ID: ID {car_to_delete} does not exist in the database. Try again")
        delete_a_car()
        cars_menu()



def delete_a_client():

    client_to_delete = input("Enter a client ID to delete: ")

    # Check if the client ID exists in the database
    if models.client_exists(client_to_delete):
        models.delete_client_by_id(client_to_delete)
        print(f"Client with ID {client_to_delete} has been deleted successfully.")
        clients_menu()
    else:
        print(f"Invalid client ID: ID {client_to_delete} does not exist in the database. Try again")
        delete_a_client()

def clients_menu():
    clients_menu_prompt = '''
Please enter an option below to navigate through the our clients.

0. Main Menu
1. List all clients
2. Add a client
3. Delete a client
4. Go back one level
5. Exit
'''

    print(clients_menu_prompt)

    option = int(input("Enter an option: "))

    if option == 1:
        customers = models.list_all_clients()
        for customer in customers:
            print(f"{customer.first_name} {customer.last_name}")
        clients_menu()
    elif option == 2:
        first_name = input("Please enter a client's first name: ")
        last_name = input("Please enter a client's last name: ")
        new_client = models.add_client(first_name, last_name)
        print(f"Added Client ID: {new_client.id}, First Name: {new_client.first_name}, Last Name: {new_client.last_name}")
        clients_menu()

    elif option == 3:
        delete_a_client()
           
    elif option == 4:
        main_menu()

    elif option == 5:
        exit()
    elif option == 0:
        main_menu()
    
    else:
        print("Invalid option")
        clients_menu()
        
def main_menu():
    main_menu_prompt = """
Welcome to lightning rental service!

Please enter an option below to navigate through the our database.


1. Clients
2. Cars
3. Feedback
4. Exit

"""
    print(main_menu_prompt)

    option = int(input("Enter an option: "))
    if option == 1:
        clients_menu()
    elif option == 2:
        cars_menu()
    elif option == 3:
        feedback_menu()
    elif option == 4:
        exit()
    else:
        print("Invalid option. Please enter a valid option")
        main_menu()
        
main_menu()






