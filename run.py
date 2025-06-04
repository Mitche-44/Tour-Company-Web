
from database.engine import Session
from models import TourPackage, Booking
from datetime import datetime

def list_packages(session):
    print("\n-- Tour Packages --")
    packages = session.query(TourPackage).all()

    if not packages:
        print("------------\n Sorry!!! No tour packages found.------------")
        return

    for tp in packages:
        print("---------------------------------------------------")
        print(f"id: {tp.id}")
        print(f"destination: {tp.destination}")
        print(f"description: {tp.description}")
        print(f"price: ${tp.price}")
        print(f"duration: {tp.duration} days")


def add_package(session):
    print("\n--- Add a New Tour Package ---")
    destination = input("Destination: ")
    price = float(input("Price (in USD): "))
    duration = int(input("Duration (days): "))
    description = input("Description: ")

    package = TourPackage(
        destination=destination,
        price=price,
        duration=duration,
        description=description
    )
    session.add(package)
    session.commit()

    print("\n-------- Congrats! You have added a Tour Package -----")


def delete_package(session):
    print("\n--- Delete a Tour Package ---")
    list_packages(session)
    
    try:
        id_to_delete = int(input("Enter package ID to delete: "))
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")
        return

    package = session.get(TourPackage, id_to_delete)
    if package:
        session.delete(package)
        session.commit()
        print("------------Deleted!!! Hope you did not need that-----------")
    else:
        print("Tour package not found.")


def list_bookings(session):
    print("\n--- Bookings Available ---")
    bookings = session.query(Booking).all()

    if not bookings:
        print("------------\n Sorry!!! No bookings found.------------")
        return

    for booking in bookings:
        print("---------------------------------------------------")
        print(f"id: {booking.id}")
        print(f"name: {booking.customer_name}")
        print(f"email: {booking.email}")
        print(f"number_of_people: {booking.number_of_people}")
        print(f"tour_package_id: {booking.tour_package_id}")
        if booking.tour_package:
            print(f"destination: {booking.tour_package.destination}")
        else:
            print("destination: N/A (no package linked)")
        print(f"created_at: {booking.created_at}")


def add_booking(session):
    print("\n--- Add a New Booking ---")
    list_packages(session)
    
    customer_name = input("Customer Name: ")
    email = input("Email: ")
    
    try:
        number_of_people = int(input("Number of People: "))
    except ValueError:
        print("Invalid number of people. Please enter a valid integer.")
        return

    try:
        tour_package_id = int(input("Tour Package ID: "))
    except ValueError:
        print("Invalid Tour Package ID. Please enter a valid integer.")
        return

    booking = Booking(
        customer_name=customer_name,
        email=email,
        number_of_people=number_of_people,
        tour_package_id=tour_package_id,
        created_at=datetime.utcnow()
    )
    session.add(booking)
    session.commit()
    print("-------------------------\n Yay 🥳 Booking added.------------------")


def delete_booking(session):
    print("\n--- Delete a Booking ---")
    list_bookings(session)

    try:
        id_to_delete = int(input("Enter booking ID to delete: "))
    except ValueError:
        print("Invalid input! Please enter a numeric booking ID.")
        return

    booking = session.get(Booking, id_to_delete)
    if booking:
        session.delete(booking)
        session.commit()
        print("-------------------Booking Deleted Successfully-----------------")
    else:
        print("\nBooking not found.")

def update_booking(session):
    print("\n--- Update a Booking ---")
    list_bookings(session)

    try:
        booking_id = int(input("Booking ID to update: ").strip())
    except ValueError:
        print("Invalid input! Please enter a numeric booking ID.")
        return

    booking = session.get(Booking, booking_id)
    if booking:
        new_name = input(f"New name (current: {booking.customer_name}): ").strip() or booking.customer_name
        new_email = input(f"New email (current: {booking.email}): ").strip() or booking.email
        
        try:
            new_number = input(f"New number of people (current: {booking.number_of_people}): ").strip()
            if new_number:
                new_number_of_people = int(new_number)
            else:
                new_number_of_people = booking.number_of_people
        except ValueError:
            print("Invalid number of people entered. Keeping the current value.")
            new_number_of_people = booking.number_of_people

        booking.customer_name = new_name
        booking.email = new_email
        booking.number_of_people = new_number_of_people

        session.commit()
        print("Yes!! Booking updated.")
    else:
        print("---------------\n Unfortunately the Booking is not found.--------------------")



def main():
    session = Session()

    while True:
        print("""
              
=== Welcome to Ace Ecotours CLI ===
1. List Tour Packages
2. Add Tour Package
3. Delete Tour Package
4. List Bookings
5. Add Booking
6. Delete Booking
7. Update Booking
8. Exit
""")
        choice = input("Enter choice: ")
        if choice == "1":
            list_packages(session)
        elif choice == "2":
            add_package(session)
        elif choice == "3":
            delete_package(session)
        elif choice == "4":
            list_bookings(session)
        elif choice == "5":
            add_booking(session)
        elif choice == "6":
            delete_booking(session)
        elif choice == "7":
            update_booking(session)
        elif choice == "8":
            print("------------------\n Goodbye! See you Again 😍--------------")
            session.close()
            break
        else:
            print("---------------\n Oops! Invalid choice. Try again.-----------------")

if __name__ == "__main__":
    main()
   