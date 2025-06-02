
from database.engine import engine, Session
from models import Base, TourPackage, Booking
from datetime import datetime

Base.metadata.create_all(bind=engine)

session = Session()

# Seed TourPackages
tour1 = TourPackage(destination="Ngong Hills", price=50.0, duration=1,
                    description="Half-day hike across scenic hills.")

tour2 = TourPackage(destination="Maasai Mara Safari", price=300.0, duration=3,
                    description="3-day guided safari through Maasai Mara reserve.")

session.add_all([tour1, tour2])
session.commit()

# Seed Bookings
booking1 = Booking(customer_name="Mitchelle Ngetich", email="mitchellngetich25@gmail.com", number_of_people=2, tour_package_id=tour1.id)

booking2 = Booking(customer_name="Charity Jameson", email="charityjameson@gmail.com", number_of_people=4, tour_package_id=tour2.id)

session.add_all([booking1, booking2])
session.commit()
session.close()
