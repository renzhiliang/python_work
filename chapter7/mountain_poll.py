responses={}

active=True

while active:
 name=input("What's your name?")
 response=input("Whice mountain would you like？")

 responses[name]=response

 repeat=input("\nWould you like to let another person?(yes/no)")
 if repeat=='no':
  active=False

print("\n-----Poll Results-----")
for name,response in responses.items():
 print(name+" would like to climb "+response+".")
 
