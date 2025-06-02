from sqlalchemy import Column, Integer, String, Text, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database.engine import Base

class TourPackage(Base):
    __tablename__ = "tour_packages"

    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)
    duration = Column(Integer, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    bookings = relationship("Booking", back_populates="tour_package")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    number_of_people = Column(Integer, nullable=False)
    tour_package_id = Column(Integer, ForeignKey("tour_packages.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    tour_package = relationship("TourPackage", back_populates="bookings")
