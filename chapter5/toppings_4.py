avilable_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested in requested_toppings:
 if requested in avilable_toppings:
  print("Adding "+requested+".")
 else:
  print("Sorry we don't have "+requested+".")
print("\nFinished making your pizza!")
