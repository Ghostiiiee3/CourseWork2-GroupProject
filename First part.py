class User:

    def __init__(self, name, role):
        #store the user's name and role
        self.name = name
        self.role = role

    #display user information
    def display_user(self):
        return f"{self.role}: {self.name}"
