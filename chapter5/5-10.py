current_users=['SMITH','ALLEN','WARD','JONES','MARTIN','BLAKE']
new_users=['smith','SMITH','Smith','SCOTT','TURNER']
for user in new_users:
 if (user.upper() in current_users): 
  print("Sorry,username ["+user+"] is occupied!") 
 else:print("Username ["+user+"] is available.")
