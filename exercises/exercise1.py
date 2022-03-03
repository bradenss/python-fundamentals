print("Hello World")

# A basic string can be defined using either
# single or double quotes.

print('Hello Again')

# I was able to create an error using an extra parentheses in
# the comment. The terminal suggested to close the bracket to
# be able to print message.
# I also added extra quotation marks to try and create an error
# but the terminal just included them into the print message.

# Following up on the instructions for The Zen of Python output.
# I did enter it into the python command line and understood
# what the author meant. I found the comment on the Dutch to be
# funny.

message = "The Los Angles Rams won Super Bowl LVI"
print(message)

# this completes section 2-1.

message = "Norway had the most total of medals in the 2022" \
          " Winter Olympics"
print(message)

# this completes section 2-2.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# This is example 1

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# This is example 2 where we bring in an argument with
# curly brackets.

def display_message():
    """We are learning functions and arguments"""
    print("We are learning about functions and arguments.")

display_message()

# This completes section 8-1.

def favorite_book(title):
    """We are learning functions and arguments"""
    print(f"My favorite books are {title.title()}.")

favorite_book('The Deltora Series')

# This completes section 8-2.



