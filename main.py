from booking_system import BookingSystem

system = BookingSystem()

# creating menu
def menu():
    print("\n====== UniScheduler ======")
    print("1. Make booking")
    print("2. View bookings")
    print("3. Show timetable")
    print("4. Exit")


# menu options  
while True:

    menu()

    choice = input("Choose option: ").strip()

    if choice == "1":

        room = input("Room ID (LAB1, LAB2, ROOMA, ROOMB): ").strip()
        user = input("Your name: ").strip()
        date = input("Date (DD/MM/YYYY): ").strip()
        time = input("Time (09:00, 10:00, 11:00, 12:00, 13:00): ").strip()

        try:
            attendees = int(input("Number of attendees: "))
            capacity = int(input("Room capacity: "))
        except ValueError:
            print("Error: Attendees and capacity must be numbers.")
            continue

        system.add_booking(room, user, date, time, attendees, capacity)

    elif choice == "2":
        system.view_bookings()

    elif choice == "3":
        date = input("Enter date (DD/MM/YYYY): ").strip()
        system.show_timetable(date)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Error: Invalid menu choice.")
