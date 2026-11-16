my_pizza = ['pepperoni', 'mushrooms', 'green peppers', 'extra cheese']
friends_pizza = my_pizza[:]  # This creates a copy of the list

my_pizza.append('pineapple')
friends_pizza.append('sausage')

print("My favorite pizzas are:")
for pizza in my_pizza:
    print(f"\t{pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizza:
    print(f"\t{pizza}")
