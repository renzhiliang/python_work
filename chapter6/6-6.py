favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
names=['sarah','phil','scott','king']
for name in favorite_languages:
  if name in names:
    print(name.title()+",thank you for taking the poll.")
  else:
    print(name.title()+",please take your poll!")
