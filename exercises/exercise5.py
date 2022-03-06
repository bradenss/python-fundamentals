# Lab exercise 5
# Do it yourself 5-1


# equal & not equal
def compare_two(arg1, arg2):
    result_equal = arg1 == arg2
    # I think that this will be false
    result_not = arg1 != arg2
    # I think that this will be true
    print(result_equal)
    print(result_not)


compare_two(7, 6)

alpha = 10
beta = 15


# greater than and less than
def great_less():
    outcome = alpha < beta
    # I think this statement will be true.
    outcome2 = alpha > beta
    # I think that this statement will be false.
    print(outcome)
    print(outcome2)


great_less()


# greater, less than or equal to

def great_less_equal(anon1):
    result_great = alpha >= anon1
    # This statement would be false.
    result_less = beta <= anon1
    # This statement would be true
    print(result_great)
    print(result_less)


great_less_equal(50)

orbits_around_earth = 'moon'
print("One of the objects that orbits around earth == 'moon'.\
 I predict True.")
print('moon' == orbits_around_earth)
print("One of the objects that orbits around earth != 'sun'. \
I predict this to be false.")
print('sun' == orbits_around_earth)

Led = 'efficient'
print("LED light bulbs is one of the more energy == 'efficient',\
 light source on the market. I predict this to be true.")
print(Led == 'efficient')
print("Incandescent light bulbs are != 'less_efficient',\
than LED bulbs. I predict this to be false.")
print(Led == 'less-efficient')


# 5-2

def compare(num1, num2):
    result_equal = num1 == num2
    result_not = num1 != num2
    print(result_equal)
    print(result_not)


compare('The sky is blue', 'The sky is Red.')

Sherbert = "An icecream that usually comes in different fruit varieties."


def member_in(arg):
    result = arg in Sherbert
    print(result)
    result = arg not in Sherbert
    print(result)


member_in('That'.lower())


def compare_two(value1, value2):
    result_equal = value1 == value2
    result_not = value1 != value2
    print(result_equal)
    print(result_not)


compare_two(10, 20)


def great_less():
    result1 = alpha < beta
    result2 = alpha > beta
    print(result1)
    print(result2)


great_less()


def great_less_equal(num2):
    result_great = alpha >= num2
    result_less = beta <= num2
    print(result_great)
    print(result_less)


great_less_equal(10)

keyword = "The keyword of the day is operations"


def member_in(arg):
    result = arg in keyword
    print(result)
    result = arg not in keyword
    print(result)


member_in('keyword')

banned_foods = ('Flour', 'Milk', 'Eggs')
food = 'Flour'

if food not in banned_foods:
    print(f"{food.title()}, is allowed for purchase.")
else:
    print(f"{food.title()}, is not allowed for purchase.")


def all_example(sum1, sum2):
    result = sum1 + sum2
    print(result)
    result2 = sum1 - sum2
    print(result2)
    result3 = sum1 * sum2
    print(result3)
    result4 = sum1 / sum2
    print(result4)
    result5 = sum1 % sum2
    print(result5)
    result6 = sum1 ** sum2
    print(result6)
    result7 = sum1 // sum2
    print(result7)


all_example(7, 13)


def assign_op(num7):
    num7 += beta
    print(num7)
    num7 -= beta
    print(num7)
    num7 *= beta
    print(num7)
    num7 /= beta
    print(num7)


assign_op(5)
