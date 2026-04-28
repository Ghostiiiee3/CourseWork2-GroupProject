import json
import os
from datetime import datetime

BOOKING_FILE = "bookings.json"


class BookingSystem:

    def __init__(self):

        self.bookings = self.load_bookings()

        # rooms
        self.rooms = ["LAB1", "LAB2", "ROOMA", "ROOMB"]

        # booking times
        self.times = ["09:00", "10:00", "11:00", "12:00", "13:00"]

    # Load bookings
    def load_bookings(self):

        if not os.path.exists(BOOKING_FILE):
            return []

        try:
            with open(BOOKING_FILE, "r") as file:
                bookings = json.load(file)

            if not isinstance(bookings, list):
                return []

            valid_bookings = []
            for booking in bookings:
                if (
                    isinstance(booking, dict)
                    and "room" in booking
                    and "date" in booking
                    and "time" in booking
                    and "user" in booking
                    and "attendees" in booking
                ):
                    valid_bookings.append(booking)

            return valid_bookings

        except (json.JSONDecodeError, OSError):
            return []

    # Save bookings
    def save_bookings(self):

        with open(BOOKING_FILE, "w") as file:
            json.dump(self.bookings, file, indent=4)

    # Validate date format
    def validate_date(self, date):

        try:
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    # Validate time
    def validate_time(self, time):

        if time not in self.times:
            return False
        return True

    # Check for double booking
    def check_conflict(self, room, date, time):

        for booking in self.bookings:
            if not isinstance(booking, dict):
                continue

            if (
                booking.get("room") == room
                and booking.get("date") == date
                and booking.get("time") == time
            ):
                return True

        return False

    # Add booking
    def add_booking(self, room, user, date, time, attendees, capacity):

        # Check room
        if room not in self.rooms:
            print("Error: Invalid room ID.")
            return

        # Check date
        if not self.validate_date(date):
            print("Error: Invalid date. Use DD/MM/YYYY.")
            return

        # Check time
        if not self.validate_time(time):
            print("Error: Invalid time.")
            print("Allowed times:", self.times)
            return

        # Check attendees
        if attendees <= 0:
            print("Error: Attendees must be greater than 0.")
            return

        # Check capacity
        if attendees > capacity:
            print("Error: Attendees exceed room capacity.")
            return

        # Check double booking
        if self.check_conflict(room, date, time):
            print("Error: Room already booked at that time.")
            return

        booking = {
            "room": room,
            "user": user,
            "date": date,
            "time": time,
            "attendees": attendees
        }

        self.bookings.append(booking)

        self.save_bookings()

        print("Booking successful!")

    # Show bookings
    def view_bookings(self):

        if len(self.bookings) == 0:
            print("No bookings found.")
            return

        for b in self.bookings:

            print(
                f"Room: {b['room']} | "
                f"Date: {b['date']} | "
                f"Time: {b['time']} | "
                f"User: {b['user']} | "
                f"Attendees: {b['attendees']}"
            )

    # ASCII timetable
    def show_timetable(self, date):

        if not self.validate_date(date):
            print("Error: Invalid date format.")
            return

        print("\nTimetable for", date)

        print("TIME     LAB1     LAB2     ROOMA     ROOMB")
        print("---------------------------------------------")

        for time in self.times:

            row = time

            for room in self.rooms:

                if self.check_conflict(room, date, time):
                    row += "   BOOKED"
                else:
                    row += "   FREE"

            print(row)