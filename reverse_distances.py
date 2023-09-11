#This program takes a list of distances and prints them from the highest number to the lowest.

def sort_distances(distances):
    distances.sort(reverse=True)
    return distances

# Example distances list
distances = [10, 5, 15, 8, 20]
sorted_distances = sort_distances(distances)
print(sorted_distances)  # Should print [20, 15, 10, 8, 5]
