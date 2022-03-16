def tree_types(tree_type, final_trees):
    while tree_type:
        current_tree = tree_type.pop()
        print("This tree is: " + current_tree)
        final_trees.append(current_tree)


def show_final_trees(final_trees):
    print("\nThe following trees have been shown:")
    for final_tree in final_trees:
        print(final_tree)
