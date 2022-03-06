# Try it yourself on Pg. 29
# 2-8
print(5+3)
print(10-2)
print(4*2)
print(16/2)

# 2-9
value = 24
message = f'My favorite number is: {value}.'
print(message)

# 2
value1 = 456_234
value2 = 68_423_791
value3 = 13_794_628
value4 = 96_374
number_sets = f'{value1}, {value2}, {value3}, {value4}'

message = f'That is a lot of numbers: \n{number_sets.title()}!'
print(message)

# 3
value5 = float(36)
value6 = int(36.5)
message = 'I can not tell if that 36 is floating {0} or if it is integer {1}.'

print(message.format(value5, value6))

# 4
movie = input('What is your favorite movie? ')
movie2 = input('How many times have you seen it? ')
movie3 = int(movie2)

if movie3 <= 5:
    print('You should see it again!')
else:
    print('Wow, is sounds like your really like it!')

