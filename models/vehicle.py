from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    license_plate = Column(String, unique=True, nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    customer = relationship("Customer", back_populates="vehicles")
    service_records = relationship("ServiceRecord", back_populates="vehicle", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Vehicle(id={self.id}, plate='{self.license_plate}', make='{self.make}', model='{self.model}', year={self.year})>"