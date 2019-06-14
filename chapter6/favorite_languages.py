favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for name,language in favorite_languages.items():
  print(name.title()+"'s favorite language is "+language.title()+".\n")

print("sarah's favorite language is "+ favorite_languages['sarah'].title()+".")
