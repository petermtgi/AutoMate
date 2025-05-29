from db import engine, Session, Base
from models.customer import Customer
from models.vehicle import Vehicle
from models.service_record import ServiceRecord
import datetime

def seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()

    # Customers
    alice = Customer(name="Alice Smith", phone="555-1234", email="alice@example.com")
    bob = Customer(name="Bob Johnson", phone="555-5678", email="bob@example.com")
    session.add_all([alice, bob])
    session.commit()

    # Vehicles
    v1 = Vehicle(license_plate="ABC123", make="Toyota", model="Camry", year=2015, customer=alice)
    v2 = Vehicle(license_plate="XYZ789", make="Honda", model="Civic", year=2018, customer=alice)
    v3 = Vehicle(license_plate="LMN456", make="Ford", model="Focus", year=2012, customer=bob)
    session.add_all([v1, v2, v3])
    session.commit()

    # Service Records
    s1 = ServiceRecord(description="Oil Change", cost=39.99, date=datetime.date(2024, 1, 10), vehicle=v1)
    s2 = ServiceRecord(description="Brake Replacement", cost=250.00, date=datetime.date(2024, 2, 15), vehicle=v1)
    s3 = ServiceRecord(description="Tire Rotation", cost=49.99, date=datetime.date(2024, 3, 5), vehicle=v2)
    s4 = ServiceRecord(description="Battery Replacement", cost=120.00, date=datetime.date(2024, 4, 20), vehicle=v3)
    session.add_all([s1, s2, s3, s4])
    session.commit()
    session.close()
    print("Database seeded with sample data.")

if __name__ == "__main__":
    seed()