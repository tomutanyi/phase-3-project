from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

    car_name = Column(String(), ForeignKey('cars.name'))  # Change to car_name

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

