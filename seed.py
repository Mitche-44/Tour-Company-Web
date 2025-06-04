
from database.engine import engine, Session
from models import Base, TourPackage, Booking
from datetime import datetime

# Create tables
Base.metadata.create_all(bind=engine)

# Start session
session = Session()

# Remove old data
print("Removing previous seed data... ")
session.query(Booking).delete()
session.query(TourPackage).delete()

# Seed TourPackages
print("Seeding tour packages... ")
tour1 = TourPackage(
    destination="Ngong Hills",
    price=50.0,
    duration=1,
    description="Half-day hike across scenic hills.",
    created_at=datetime.now()
)
tour2 = TourPackage(
    destination="Maasai Mara Safari",
    price=300.0,
    duration=3,
    description="3-day guided safari through Maasai Mara reserve.",
    created_at=datetime.now()
)
session.add_all([tour1, tour2])
session.commit()

# Seed Bookings
print("Seeding bookings... 📅")
booking1 = Booking(
    customer_name="Mitchelle Ngetich",
    email="mitchellngetich25@gmail.com",
    number_of_people=2,
    tour_package_id=tour1.id,
    created_at=datetime.now()
)
booking2 = Booking(
    customer_name="Charity Jameson",
    email="charityjameson@gmail.com",
    number_of_people=4,
    tour_package_id=tour2.id,
    created_at=datetime.now()
)
session.add_all([booking1, booking2])
session.commit()

session.close()
print("Finished seeding data successfully! ")
