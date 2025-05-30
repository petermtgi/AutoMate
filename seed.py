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
    Peter = Customer(name="Peter Mutua", phone="0791236742", email="peter@example.com")
    Claude = Customer(name="Claude Otieno", phone="0723344380", email="claude@example.com")
    session.add_all([Peter, Claude])
    session.commit()

    # Vehicles
    v1 = Vehicle(license_plate="KDK 421S", make="Toyota", model="Corolla", year=2003, customer=Peter)
    v2 = Vehicle(license_plate="KDD 001D", make="Honda", model="Fit", year=2009, customer=Peter)
    v3 = Vehicle(license_plate="KCF 122E", make="Ford", model="Ranger", year=2024, customer=Claude)
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