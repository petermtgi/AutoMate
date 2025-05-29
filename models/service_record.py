from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base
import datetime

class ServiceRecord(Base):
    __tablename__ = 'service_records'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    date = Column(Date, default=datetime.date.today)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)

    vehicle = relationship("Vehicle", back_populates="service_records")

    def __repr__(self):
        return f"<ServiceRecord(id={self.id}, desc='{self.description}', cost={self.cost}, date={self.date})>"