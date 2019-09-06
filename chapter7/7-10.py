places={}

active=True
while active:
 name=input("Tell me your name:")
 place=input("Which place would you like:")

 places[name]=place

 yorn=input("\nDo you like let another guy to answer my question?(y/n)")
 if yorn=='n':active=False

print(places)
