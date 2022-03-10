# 4-3 Try it Yourself.
# 1
for value in range(0, 21):
    print(value)


# 4-6
# 2
current_number = 0
while current_number < 20:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


# 4-7
# 3
for num in 'odd_numbers':
    print(3, 6, 9, 12, 15, 18, 21, 24, 27, 30)
    break

# 4-8
# 4
squares = []
for value in range(1, 11):
    square = value**3
    squares.append(square)

print(squares)
