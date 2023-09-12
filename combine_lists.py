#The program takes 2 lists and prints one combined list.

def combine_lists(list1, list2):
    list1.reverse()  # Reverse the order of list1
    combined_list = list2 + list1  # Combine the two lists
    return combined_list

drews_list = ["Alice", "Bob", "Charlie"]
jamies_list = ["Eve", "Frank", "Grace"]

combined = combine_lists(jamies_list, drews_list)
print(combined)  # Should print ["Eve", "Frank", "Grace", "Charlie", "Bob", "Alice"]
