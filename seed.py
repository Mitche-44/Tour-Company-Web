
from database.engine import Session, engine
from models import Base, TourCompany, Tour, Customer, Booking, TourGuide
from datetime import date

Base.metadata.create_all(bind=engine)
# add a session instance
session = Session()

company = TourCompany(name="Ace Ecotours", address="Kilimani")
session.add(company)

guide = TourGuide(name="Peter Oyugi", expertise="Animal spotting")
session.add(guide)

tour = Tour(title="Day trip to Nairobi National Park", description="Explore the Giraffe Centre, Elephant Orphanage and visit the Nairobi National Park", company=company)
tour.guides.append(guide)
session.add(tour)

customer = Customer(name="Mitchelle Ngetich", email="mitchellngetich24@gmail.com")
session.add(customer)

booking = Booking(customer=customer, tour=tour, booking_date=date.today())
session.add(booking)

session.commit()

