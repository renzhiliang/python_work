rivers={'Nile':'Egypt','Amazon':'American','Yangtze':'China',}
print("The first print is:")
for river,country in rivers.items():
  print("The "+river+" runs through "+country+".")
print("\nThe second print is:")
for river in rivers.keys():
  print(river.title())
print("\nThe third print is:")
for country in rivers.values():
  print(country.title())

