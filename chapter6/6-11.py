cities={
'BeiJing':{
'country':'China',
'population':2171,
'fact':'classic'
},
'NewYork':{
'country':'America',
'population':851,
'fact':'fashion'
},
'Tokyo':{
'country':'Japan',
'population':3703,
'fact':'beautiful'
}
}

for cityname,cityinfo in cities.items():
  print(cityname+"'s information are:")
  for k,v in cityinfo.items():
    print("\t"+k+":"+str(v))
