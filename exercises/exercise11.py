# 9-6
# 1
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " makes good " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. All are welcome!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nAvailable flavors:")
        for flavor in self.flavors:
            print(flavor.title())


big_one = IceCreamStand('Dairy Queen')
big_one.flavors = ['vanilla', 'sherbert', 'cookie dough']

big_one.describe_restaurant()
big_one.show_flavors()


# 9-7
# 2
class User:

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(" " + privilege)


jane = Admin('Jane', 'Doe', 'j_doe', 'j_doe@email.com', 'Kansas')
jane.describe_user()

jane.privileges = [
    'can lock posts',
    'can delete posts',
    'can ban users',
]

jane.show_privileges()


# 9-8
# 3

class User:

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


class Privileges:

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(" " + privilege)
        else:
            print("- This user has no privileges.")


jane = Admin('Jane', 'Doe', 'j_doe', 'j_doe@email.com', 'Kansas')
jane.describe_user()

jane.privileges.show_privileges()

print("\nNew privileges inbound...")
jane_privileges = [
    'can reset passwords',
    'can unban users',
    'can start a new event',
    ]

jane.privileges.privileges = jane_privileges
jane.privileges.show_privileges()
