
from database.engine import Session
from models import Tour, TourGuide, Booking, Customer, TourCompany
from datetime import date


session = Session()
# --- Tour Functions ---
def list_tours():

        tours = session.query(Tour).all()
        for tour in tours:
            print(f"{tour.id}: {tour.title} - {tour.description}")

def list_companies(session):
    companies = session.query(TourCompany).all()
    if not companies:
        print("No companies found.")
    else:
        print("\n--- Available Tour Companies ---")
        for company in companies:
            print(f"{company.id}: {company.name} - {company.address}")

def create_tour():
    
        title = input("Enter tour title: ")
        description = input("Enter description: ")
        company_id = int(input("Enter company ID: "))
        company = session.get(TourCompany, company_id)
        if company:
            tour = Tour(title=title, description=description, company=company)
            session.add(tour)
            session.commit()
            print(f"Tour '{title}' created.")
        else:
            print("Company not found.")


def delete_tour():
    
        list_tours()
        tour_id = int(input("Enter Tour ID to delete: "))
        tour = session.get(Tour, tour_id)
        if tour:
            session.delete(tour)
            session.commit()
            print("Tour deleted.")
        else:
            print("Tour not found.")


# --- Guide Functions ---
def list_guides():
    with Session() as session:
        for guide in session.query(TourGuide).all():
            print(f"{guide.id}: {guide.name} ({guide.expertise})")


def create_guide():
    
        name = input("Enter guide name: ")
        expertise = input("Enter expertise: ")
        guide = TourGuide(name=name, expertise=expertise)
        session.add(guide)
        session.commit()
        print(f"Guide '{name}' created.")


def delete_guide():
    
        list_guides()
        guide_id = int(input("Enter Guide ID to delete: "))
        guide = session.get(TourGuide, guide_id)
        if guide:
            session.delete(guide)
            session.commit()
            print("Guide deleted.")
        else:
            print("Guide not found.")


# --- Booking Functions ---
def list_bookings():
    
        bookings = session.query(Booking).all()
        for b in bookings:
            print(f"#{b.id}: {b.customer.name} booked '{b.tour.title}' on {b.booking_date}")


def create_booking():
    
        customer_id = int(input("Enter Customer ID: "))
        tour_id = int(input("Enter Tour ID: "))
        customer = session.get(Customer, customer_id)
        tour = session.get(Tour, tour_id)
        if customer and tour:
            booking = Booking(customer=customer, tour=tour, booking_date=date.today())
            session.add(booking)
            session.commit()
            print("Booking created.")
        else:
            print("Invalid customer or tour ID.")


def delete_booking():
    
        list_bookings()
        booking_id = int(input("Enter Booking ID to delete: "))
        booking = session.get(Booking, booking_id)
        if booking:
            session.delete(booking)
            session.commit()
            print("Booking deleted.")
        else:
            print("Booking not found.")


# --- Menus ---
def tour_menu():
    while True:
        print("\n--- Tour Management ---")
        print("1. List Tours")
        print("2. Add Tour")
        print("3. Delete Tour")
        print("4. Back")
        choice = input("Choose: ")
        if choice == "1":
            list_tours()
        elif choice == "2":
            create_tour()
        elif choice == "3":
            delete_tour()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


def guide_menu():
    while True:
        print("\n--- Guide Management ---")
        print("1. List Guides")
        print("2. Add Guide")
        print("3. Delete Guide")
        print("4. Back")
        choice = input("Choose: ")
        if choice == "1":
            list_guides()
        elif choice == "2":
            create_guide()
        elif choice == "3":
            delete_guide()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


def booking_menu():
    while True:
        print("\n--- Booking Management ---")
        print("1. List Bookings")
        print("2. Add Booking")
        print("3. Delete Booking")
        print("4. Back")
        choice = input("Choose: ")
        if choice == "1":
            list_bookings()
        elif choice == "2":
            create_booking()
        elif choice == "3":
            delete_booking()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


# --- Main App ---
def main():
    while True:
        print("""
=== Ace Ecotours CLI ===
1. Manage Tours
2. Manage Guides
3. Manage Bookings
4. Exit
        """)
        option = input("Enter your choice: ")
        if option == "1":
            tour_menu()
        elif option == "2":
            guide_menu()
        elif option == "3":
            booking_menu()
        elif option == "4":
            print("Goodbye!See you later😍")
            break
        else:
            print("Oooops! Invalid choice. Try again.")


if __name__ == "__main__":
    main()
