from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

Base = declarative_base()
engine = create_engine('sqlite:///lightning.db')
Session = sessionmaker(bind=engine)
session = Session()

car_client = Table(
    'car_client',
    Base.metadata,
    Column('client_id', ForeignKey('clients.id'), primary_key=True),
    Column('car_id', ForeignKey('cars.id'), primary_key=True),
    extend_existing=True,
)

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    price = Column(Integer())

    clients = relationship('Client', secondary=car_client, back_populates='cars')
    feedbacks = relationship("Feedback", back_populates="car")

    def __repr__(self):
        return f"Car name: {self.name}, price: {self.price}"

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String())

    feedbacks = relationship("Feedback", back_populates="client")
    cars = relationship('Car', secondary=car_client, back_populates='clients')

    def __repr__(self):
        return f"Client's first name: {self.first_name}, last name: {self.last_name}"



class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer(), primary_key=True)

    star_ratings = Column(Integer())
    car_name = Column(String(), ForeignKey('cars.name'))
    client_id = Column(Integer(), ForeignKey('clients.id'))

    client = relationship("Client", back_populates="feedbacks")
    car = relationship("Car", back_populates="feedbacks", foreign_keys=[car_name])


# list all clients
def list_all_clients():
    return session.query(Client).all()

# Method 2: List all cars
def list_all_cars():
    return session.query(Car).all()

# Method 3: List all reviews
def list_all_reviews():
    return session.query(Feedback).all()

# Method 4: List all reviews per customer
def list_reviews_by_customer(customer_id):
    return session.query(Feedback).filter(Feedback.client_id == customer_id).all()

# Method 5: List all cars used by a customer
def list_cars_used_by_customer(customer_id):
    customer = session.query(Client).get(customer_id)
    if customer:
        return customer.cars
    else:
        return []


# Method 6: List average restaurant review per user
def list_average_review_per_user():

    return (
        session.query(Feedback.client_id, func.avg(Feedback.star_ratings).label('average_rating'))
        .group_by(Feedback.client_id)
        .all()
    )
# method 7: Add a car
def add_car(name, price):
    car = Car(name=name, price=price)
    session.add(car)
    session.commit()
    return car

# method 8: Add a client
def add_client(first_name, last_name):
    client = Client(first_name=first_name, last_name=last_name)
    session.add(client)
    session.commit()
    return client 

# method 9: Delete a car
def delete_car_by_id(car_id):
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        session.delete(car)
        session.commit()
        return True
    else:
        print("Car not deleted successfully")
        return False

# method 9a: car exists

def car_exists(car_id):
    # Query the database to check if a car with the given ID exists
    return session.query(Car).filter(Car.id == car_id).count() > 0

# method 10a

# method 10: delete a client from the database
def delete_client_by_id(client_id):
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        session.delete(client)
        session.commit()
        return True
    else:
        return False 
    
# method 10a: client exists

def client_exists(client_id):

    return session.query(Client).filter(Client.id == client_id).count() > 0

# Method 11: Add feedback
def add_feedback(star_ratings, car_id, client_id):
    feedback = Feedback(
        star_ratings=star_ratings,
        car_id=car_id,
        client_id=client_id,
    )

    session.add(feedback)
    session.commit()
    return feedback


