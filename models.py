
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship
from database.engine import Base

# Many-to-many association
association_table = Table(
    "tour_tour_guides", Base.metadata,
    Column("tour_id", Integer, ForeignKey("tours.id")),
    Column("guide_id", Integer, ForeignKey("tour_guides.id"))
)

class TourCompany(Base):
    __tablename__ = "tour_companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String)

    tours = relationship("Tour", back_populates="company")

class Tour(Base):
    __tablename__ = "tours"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    company_id = Column(Integer, ForeignKey("tour_companies.id"))

    company = relationship("TourCompany", back_populates="tours")
    bookings = relationship("Booking", back_populates="tour")
    guides = relationship("TourGuide", secondary=association_table, back_populates="tours")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

    bookings = relationship("Booking", back_populates="customer")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    tour_id = Column(Integer, ForeignKey("tours.id"))
    booking_date = Column(Date)

    customer = relationship("Customer", back_populates="bookings")
    tour = relationship("Tour", back_populates="bookings")

class TourGuide(Base):
    __tablename__ = "tour_guides"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    expertise = Column(String)

    tours = relationship("Tour", secondary=association_table, back_populates="guides")

