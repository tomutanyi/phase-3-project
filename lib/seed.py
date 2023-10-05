#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import Base, engine

Base.metadata.create_all(engine)
from models import Car, Client, Feedback

if __name__ == '__main__':
    engine = create_engine('sqlite:///lightning.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Car).delete()
    session.query(Client).delete()
    session.query(Feedback).delete()

    fake = Faker()

    # a list of 40 car names to choose from
    car_names = [
    "Nissan Sunny", "Toyota Camry", "Lamborghini Aventador",
    "Ford Mustang", "Honda Civic", "Chevrolet Corvette", "BMW X5", "Audi Q7",
    "Mercedes-Benz S-Class", "Tesla Model 3", "Volkswagen Golf", "Subaru Outback",
    "Mazda CX-5", "Hyundai Sonata", "Kia Sportage", "Lexus RX", "Jeep Wrangler",
    "Acura MDX", "Volvo XC60", "Jaguar F-Type", "Porsche 911", "Mini Cooper",
    "Land Rover Range Rover", "Cadillac Escalade", "GMC Sierra", "Chrysler 300",
    "Infiniti Q50", "Buick Encore", "Lincoln Navigator", "Ferrari 488", "Maserati GranTurismo",
    "Dodge Challenger", "Aston Martin Vantage", "Lotus Evora", "McLaren 720S",
    "Bugatti Chiron", "Koenigsegg Jesko", "Pagani Huayra", "Audi R8", "Porsche Cayenne"]




    cars = []
    for car_name in car_names:
        price = random.randint(10, 25) * 100
        car = Car(
            name=car_name,
            price=price
        )

        session.add(car)
        session.commit()
        cars.append(car)


    clients = []
    for i in range(50):
        client = Client(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

        session.add(client)
        session.commit()

        clients.append(client)

    feedbacks = []
    for client in clients:
        for _ in range(random.randint(1, 2)):
            car_name = random.choice(car_names)  # Select a random car name

            feedback = Feedback(
                star_ratings=random.randint(1, 5),
                car_name=car_name,  # Use car name instead of car ID
                client_id=client.id,
            )

            session.add(feedback)
            session.commit()
            feedbacks.append(feedback)

    session.close()