favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
friends=['phil','sarah']

for name in favorite_languages:
  if name in friends:
    print(name.title()+" 's favorite language is "+favorite_languages[name].title()+".")


