# 10-6
# 1
try:
    x = input("Provide a number: ")
    x = int(x)

    y = input("Provide another number: ")
    y = int(y)

except ValueError:
    print("A number is needed to be able to make a sum.")

else:
    _sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(_sum) + ".")

# 10-7
# 2

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nProvide a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Provide another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("A number is needed to be able to make a sum.")

    else:
        sum1 = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum1) + ".")

# 10-8
# 3

filenames = ['dogs.txt', 'cats.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Apologizes, that file can't be found.")

# 10-9
# 4

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

    try:
        with open(filename) as echo:
            text = echo.read()

    except FileNotFoundError:
        pass

    else:
        print("\nReading file: " + filename)
        print(text)
