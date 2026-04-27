#save bookings
    def save_bookings(self):

        with open(BOOKING_FILE, "w") as file:
            json.dump(self.bookings, file, indent=4)

    #validate date format
    def validate_date(self, date):

        try:
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    #validate time
    def validate_time(self, time):

        if time not in self.times:
            return False
        return True

    #check for double booking
    def check_conflict(self, room, date, time):

        for booking in self.bookings:

            if (
                booking["room"] == room
                and booking["date"] == date
                and booking["time"] == time
            ):
                return True

        return False
