
from database.engine import Session
from models import TourPackage, Booking
from datetime import datetime



def list_packages(session):
    print("\n-- Tour Packages --")
    for tp in session.query(TourPackage).all():
        print(f"{tp.id}: {tp.destination} - {tp.description} (${tp.price}) [{tp.duration} days]")

def add_package(session):
    destination = input("Destination: ")
    price = float(input("Price: "))
    duration = int(input("Duration (days): "))
    description = input("Description: ")
    package = TourPackage(destination=destination, price=price, duration=duration, description=description)
    session.add(package)
    session.commit()
    print("--------Congrats! You have added a Tour Package-----")

def delete_package(session):
    list_packages(session)
    id_to_delete = int(input("Enter package ID to delete: "))
    package = session.get(TourPackage, id_to_delete)
    if package:
        session.delete(package)
        session.commit()
        print("Deleted.")
    else:
        print("Tour package not found.")
        

def list_bookings(session):
    print("\n------------------Bookings Available----------------")
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
    list_packages(session)
    customer_name = input("Customer Name: ")
    email = input("Email: ")
    number_of_people = int(input("Number of People: "))
    tour_package_id = int(input("Tour Package ID: "))

    booking = Booking(
        customer_name=customer_name,
        email=email,
        number_of_people=number_of_people,
        tour_package_id=tour_package_id,
        created_at=datetime.utcnow()
    )
    session.add(booking)
    session.commit()
    print("Yay 🥳 Booking added.")

def delete_booking(session):
    list_bookings(session)
    id_to_delete = int(input("Enter booking ID to delete: "))
    booking = session.get(Booking, id_to_delete)
    if booking:
        session.delete(booking)
        session.commit()
        print("Deleted.")
    else:
        print("------------------/n Booking not found.-------------------------")

def update_booking(session):
    list_bookings(session)
    booking_id = int(input("Booking ID to update: "))
    booking = session.get(Booking, booking_id)
    if booking:
        booking.customer_name = input(f"New name (current: {booking.customer_name}): ") or booking.customer_name
        booking.email = input(f"New email (current: {booking.email}): ") or booking.email
        booking.number_of_people = int(input(f"New number of people (current: {booking.number_of_people}): ") or booking.number_of_people)
        session.commit()
        print("Booking updated.")
    else:
        print("Booking not found.")

def main():
    session = Session()

    while True:
        print("""
=== Ecotours CLI ===
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
            print("Goodbye!See you Again 😍")
            session.close()
            break
        else:
            print("Oops! Invalid choice. Try again.")

if __name__ == "__main__":
    main()
   
    
