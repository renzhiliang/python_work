prompt="\nTell me something,and I'll repeate it back to you:"
prompt+="\nEnter 'quit' to end the program.\n"
message=""
while message!='quit':
 message=input(prompt)
 if message!='quit':
  print(message)
