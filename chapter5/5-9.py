#users=['Eric','admin','Scott','Ford','Jones']
users=[]
if users:
 for user in users:
  if user.lower()=='admin':print("Hello admin,would you like to see a report.")
  else:print("Hello "+user+",thank you for logging in again!")
else:print("We need to find some users!")  
