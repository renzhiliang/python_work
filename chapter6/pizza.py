#存储所点比萨的信息
pizza={
 'crust':'thick',
 'toppings':['mushrooms','extra cheese'],
}
#描述所点比萨
print("You ordered a "+pizza['crust']+"-crust pizza"+
"with the following toppings:")

for topping in pizza['toppings']:
 print("\t"+topping)
