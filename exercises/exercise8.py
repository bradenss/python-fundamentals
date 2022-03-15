# 5-8 & 5-9
# 1

usernames = ['Brian', 'Colton', 'Denise', 'Ethan', 'Admin']


def users():
    for user in usernames:
        print(f"Thanks for logging back in, {user}.")
    if 'Admin' in usernames:
        print('Hello, Admin, welcome back to the Jungle.')


users()


# 5-9

def users_gone():
    if '' in usernames:
        print("We need to find some users!")
    else:
        print("Phew, looks like we have some users!")


users_gone()

# 5-10
# 2

current_users = ['Brian', 'Colton', 'Denise', 'Ethan', 'Alan']
new_users = ['Frank', 'George', 'Hank', 'Colton', 'Jeffery']
for new_user in new_users:
    if new_user in current_users:
        print(f"The username, {new_user}, has been taken. \nTry something new.")
    else:
        print(f"Welcome in, newcomer: {new_user}.")

# 5-11
# 3

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

# 6-1
# 4

person = {
    'first_name': 'Greg',
    'last_name': 'Doe',
    'age': '25',
    'city': 'St. Louis',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-7
# 5
people = []

person1 = {
    'first_name': 'Greg',
    'last_name': 'Doe',
    'age': '25',
    'city': 'St. Louis',
    }
people.append(person1)

person1 = {
    'first_name': 'Clay',
    'last_name': 'Trail',
    'age': '55',
    'city': 'Albuquerque',
    }
people.append(person1)

person1 = {
    'first_name': 'Jordan',
    'last_name': 'Learn',
    'age': '37',
    'city': 'St. Petersburg',
    }
people.append(person1)

for person1 in people:
    name = person1['first_name'].title() + " " + person1['last_name'].title()
    age = str(person1['age'])
    city = person1['city'].title()

    print(name + ", of " + city + ", is " + age + " Years old.")
