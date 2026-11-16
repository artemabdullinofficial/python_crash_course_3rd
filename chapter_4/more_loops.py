my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]  # This creates a copy of the list

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"\t{food}")

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(f"\t{food}")