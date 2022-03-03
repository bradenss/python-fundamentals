first_name = 'Jack'
last_name = 'Black'
full_name = f'{first_name} {last_name}'
message = f'Hello, {full_name.title()}, King Kong still lives on skull island'
print(message)

name = 'jane doe'
print(name.upper())
print(name.lower())
print(f"Good Evening, {name.title()}.")

value = 'Theodore Roosevelt'
message = """Once said, "Better is it to dare mighty things, to win glorious triumphs, even though \
checkered by failure... than to rank with those poor spirits who neither enjoy nor suffer much, \
because they live in a gray twilight that knows not victory nor defeat."""
print(f"\n\t{value,message.format()}")

famous_person = 'Steve Jobs'
message2 = f"\n\t{famous_person} ""once said, 'Stay hungry, Stay foolish' meaning don't stay complacent and continue \
to stretch the bounds of your potential."""
print(message2)

name2 = '\n Percy Jackson '
print(name2.rstrip())
print(name2.lstrip())
print(name2.strip())

