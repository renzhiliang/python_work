def describe_pet(animal_type,pet_name):
 """显示宠物信息"""
 print("\nI have a "+animal_type+".")
 print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet(pet_name='harry',animal_type='hamster')
describe_pet('dog','willie')
