# Test with equality and inequality for strings
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

car = 'audi'
print("\nIs car == 'subaru'? I predict False.")
print(car == 'subaru')

# Test using the lower() method
car = 'BMW'
print("\nIs car.lower() == 'bmw'? I predict True.")
print(car.lower() == 'bmw') 

car = 'Audi'
print("\nIs car.lower() == 'mercedes'? I predict False.")
print(car.lower() == 'mercedes')

# Numureical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25) 

age = 30
print("\nIs age == 25? I predict False.")
print(age == 25) 

age = 20
print("\nIs age < 25? I predict True.")
print(age < 25) 

age = 15
print("\nIs age > 25? I predict False.") 
print(age > 25)

age = 25
print("\nIs age >= 25? I predict True.")
print(age >= 25)

age = 30
print("\nIs age <= 25? I predict False.")
print(age <= 25)

# Test using the and keyword and the or keyword
age = 25
print("\nIs age > 20 and age < 30? I predict True.")
print(age > 20 and age < 30)

age = 15
print("\nIs age > 20 and age < 30? I predict False.")
print(age > 20 and age < 30)

age = 15
print("\nIs age < 20 or age > 30? I predict True.")   
print(age < 20 or age > 30)

age = 25
print("\nIs age < 20 or age > 30? I predict False.")
print(age < 20 or age > 30)

# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("\nIs 'apple' in the list of fruits? I predict True.")
print('apple' in fruits)

print("\nIs 'grape' in the list of fruits? I predict False.")
print('grape' in fruits)

# Test whether an item is not in a list
print("\nIs 'grape' not in the list of fruits? I predict True.")
print('grape' not in fruits)

print("\nIs 'banana' not in the list of fruits? I predict False.")
print('banana' not in fruits)