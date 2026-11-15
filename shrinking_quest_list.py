guests = ['Artem', 'Maria', 'Olga', 'Ivan', 'Dmitry', 'Svetlana']
print(guests)

print("Only 2 guests can be invited to dinner.") 

removed_guest1 = guests.pop()  # Remove Svetlana
print(f"Sorry, {removed_guest1}, I can't invite you to dinner.")

removed_guest2 = guests.pop()  # Remove Dmitry
print(f"Sorry, {removed_guest2}, I can't invite you to dinner.")

removed_guest3 = guests.pop()  # Remove Ivan
print(f"Sorry, {removed_guest3}, I can't invite you to dinner.")

removed_guest4 = guests.pop()  # Remove Olga
print(f"Sorry, {removed_guest4}, I can't invite you to dinner.")

print(f"Hello, {guests[0]}! You are still invited to dinner.")
print(f"Hello, {guests[1]}! You are still invited to dinner.")

del guests[0]  # Remove Artem
del guests[0]  # Remove Maria 
print(guests)  # Output: []