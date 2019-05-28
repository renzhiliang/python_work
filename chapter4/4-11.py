pizzas=['Super','Seafood','New Orleans','Popcorn Chicken','Delicious Bacon']
friend_pizzas=pizzas[:]
pizzas.append('Thick style')
friend_pizzas.append('Cracker and Thin Styles')
print("My favorite pizzas are:")
for pizza in pizzas:
 print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
 print(pizza)
