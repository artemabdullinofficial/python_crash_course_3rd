places = ['Paris', 'Tokyo', 'New York', 'London', 'Sydney']
print(places)

# Sort the list in alphabetical order without modifying the original list
print(sorted(places))
print(places)

# Sort the list in reverse alphabetical order without modifying the original list
print(sorted(places, reverse=True))
print(places)

# Reverse the order of the list and modify the original list
places.reverse()
print(places)

# Reverse the order of the list again to restore the original order
places.reverse()
print(places)

# Sort the list in alphabetical order and modify the original list
places.sort()
print(places)

# Sort the list in reverse alphabetical order and modify the original list
places.sort(reverse=True)
print(places)