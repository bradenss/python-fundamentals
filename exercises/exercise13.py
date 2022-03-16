# 1
# 8-15-8-17

import printing_functions as pf

tree_type = ['Maple', 'Dogwood', 'Oak']
final_tree = []

pf.tree_types(tree_type, final_tree)
pf.show_final_trees(final_tree)

# 2
# 9-10

from my_restaurant import Restaurant

bionic_burger = Restaurant('Bionic Burger', ' the six million dollar burger')
bionic_burger.describe_restaurant()
bionic_burger.open_restaurant()

# 9-11

from user import Admin

jane = Admin('Jane', 'Doe', 'j_doe', 'j_doe@email.com', 'Kansas')
jane.describe_user()

jane_privileges = [
    'can reset passwords',
    'can unban users',
    'can start a new event',
]

jane.privileges.privileges = jane_privileges

print("\nThe admin " + jane.username + " has these privileges: ")
jane.privileges.show_privileges()

# 9-12

from admin import Admin

jane = Admin('Jane', 'Doe', 'j_doe', 'j_doe@email.com', 'Kansas')
jane.describe_user()

jane_privileges = [
    'can reset passwords',
    'can unban users',
    'can start a new event',
]

jane.privileges.privileges = jane_privileges

print("\nThe admin " + jane.username + " has these privileges: ")
jane.privileges.show_privileges()

# 9-16
# 3

# I have gone to https://pymotw.com/ and found some modules that will useful
