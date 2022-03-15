# 8-3
# 1
def make_shirt(size, message):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It says, \n"' + message + '"')


make_shirt('x-large', 'Sleep,\neat, \ncode.')
make_shirt(message="Cloud Computing", size='medium')


# 8-4
def make_shirt(size='large', message='I Love Python!'):
    print("\nI will be making a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Coffee required.')


# 8-5

def describe_city(city, country='USA'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)


describe_city('\nKansas City')
describe_city('Peabody')
describe_city('Dodge City')


# 8-9
# 2
def show_messages(messages):
    for message in messages:
        print(message.title())


messages = ['\nCoding time.', 'Sleep is needed.', 'It\'s chow time.']
show_messages(messages)


# 8-10

def show_message(messages):
    for message in messages:
        print(message)


def send_message(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        sent_message = message
        sent_messages.append(sent_message)
    for sent_message in sent_messages:
        messages.append(sent_message)


messages = ['Coding time.', 'Sleep is needed.', 'It\'s chow time.']
show_messages(messages)
print("\n")
send_message(messages)
show_message(messages)


# 8-11

def show_message(messages):
    for message in messages:
        print(message)


def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        sent_message = message
        sent_messages.append(sent_message)
    for sent_message in sent_messages:
        messages.append(sent_message)
    return messages


messages = ['Coding time.', 'Sleep is needed.', 'It\'s chow time.']
show_messages(messages)

print("\n")
send_message = send_messages(messages[:])
show_message(send_message)
print("\n")


# 9-1
# 3
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " makes good " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. All are welcome!"
        print("\n" + msg)


restaurant = Restaurant('Olive Garden', 'Italian food')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " makes good " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. All are welcome!"
        print("\n" + msg)


olive_garden = Restaurant('Olive Garden', 'Italian food')
olive_garden.describe_restaurant()

chezzies_pizza = Restaurant('Chezzies Pizza', 'pizza')
chezzies_pizza.describe_restaurant()

freddies = Restaurant('Freddie\'s', 'American Food')
freddies.describe_restaurant()


# 9-3

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print(" Username: " + self.username)
        print(" Email: " + self.email)
        print(" Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")


jane = User('Jane', 'Doe', 'j_doe', 'j_doe@email.com', 'Kansas')
jane.describe_user()
jane.greet_user()

steve = User('Steve', 'Jobs', 's_jobs', 's_jpbs@email.com', 'California')
steve.describe_user()
steve.greet_user()


# 9-4

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

    def set_numbers_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('Olive Garden', 'Italian food')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 10000
print("\nNumber served: " + str(restaurant.number_served))

restaurant.set_numbers_served(15000)
print("\nNumber served: " + str(restaurant.number_served))

restaurant.increment_number_served(1000)
print("\nNumber served: " + str(restaurant.number_served))


# 9-5

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
        print(" Username: " + self.username)
        print(" Email: " + self.email)
        print(" Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


jane = User('Jane', 'Doe', 'j_doe', 'j_doe@email.com', 'Kansas')
jane.describe_user()
jane.greet_user()

print('\nMaking 2 login attempts...')
jane.increment_login_attempts()
jane.increment_login_attempts()
print(" Login attempts: " + str(jane.login_attempts))

print("resetting login attempts...")
jane.reset_login_attempts()
print(" Login attempts: " + str(jane.login_attempts))
