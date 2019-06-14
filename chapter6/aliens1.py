aliens=[]
#创建30个外星人
new_alien={'color':'greem','points':5,'speed':'slow'}
for alien_number in range(30):
  aliens.append(new_alien)
#显示前5个外星人
for alien in aliens[:5]:
 print(alien)
print("......")
#显示创建了多少个外星人
print("Total number of aliens: "+str(len(aliens)))
