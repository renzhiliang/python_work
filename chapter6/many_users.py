users={
  'aeinstein':{
    'first':'albert',
    'last':'einstein',
    'location':'princeton',
  },
  'mcurie':{
    'first':'marie',
    'last':'curie',
    'location':'paris',
  }
}

for username,userinfo in users.items():
  print("\nusername:"+username)
  fullname=userinfo['first']+" "+userinfo['last']
  location=userinfo['location']
  print("\tFull name:"+fullname.title())
  print("\tLocation:"+location.title())
