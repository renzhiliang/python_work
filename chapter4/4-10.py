#numbers=range(3,31,3)
numbers=[number**3 for number in range(1,11)]
print(numbers)
print("The first three items in the list are:")
print(numbers[0:3])
print("Three items from the middle of the list are:")
print(numbers[5:8])
print("The last three items in the list are:")
print(numbers[-3:])
