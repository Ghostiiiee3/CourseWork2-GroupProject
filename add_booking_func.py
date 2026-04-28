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