prompt="\nTell me the condiment you want for pizza"
prompt+="(Enter 'quit' to end this program):\n"

flag=True
while flag:
 message=input(prompt)
 
 if message!='quit':
  flag=True
  print("\nI will add "+message+" for you!")
 else:
  flag=False
