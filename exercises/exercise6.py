# 5-3 Try it yourself
# 1

def alien_color(green, yellow, red):
    if green == 'green':
        print('You earned 5 points.')
    if yellow == 'yellow':
        print('')
    if red == 'red':
        print('')


alien_color('green', 'orange', 'white')


# 5-2
# 2
def alien_color2(green):
    if green == "green":
        print('You earned 5 points.')
    else:
        print('You earned 10 points.')


alien_color2("yellow")
alien_color2("green")


# 5-3
# 3
def alien_color3(green1):
    if green1 == "green":
        print('You earned 5 points')
    elif green1 == "yellow":
        print('You earned 10 points')
    else:
        print('You earned 15 points')


alien_color3("green")
alien_color3("yellow")
alien_color3("red")

# 5-6
# 4

age = 1
if age < 2:
    print('This person is a baby.')
elif age < 4:
    print('This person is a toddler.')
elif age < 13:
    print('This person is a kid.')
elif age < 20:
    print('This person is a teenager.')
elif age < 65:
    print('This person is an adult.')
else:
    print('This person is an elder.')


# 5 Boolean

def boolean_exercise():
    print(bool('exercise'))
    print(bool(0.0))


boolean_exercise()
