prompt="\nInput your age:"

price=0
while True:
 age=int(input(prompt))
 if age<=3:
  price=0
 elif age>3 and age<=12:
  price=10
 else:
  price=15 
 print("Your ticket price is:"+str(price))
