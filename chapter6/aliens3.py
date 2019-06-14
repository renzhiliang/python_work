aliens=[]
#创建30个外星人
new_alien={'color':'green','points':5,'speed':'slow'}
for alien_number in range(30):
  aliens.append(new_alien)
for alien in aliens[0:5]:
 print(alien)
#改变前三个外星人
for alien in aliens[0:3]:
 if alien['color']=='green':
    alien['color']='yellow'
    alien['speed']='medium'
    alien['points']=10
 elif alien['color']=='yellow':
  alien['color']='red'
  alien['speed']='fast'
  alien['points']=15
#显示前5个外星人
for alien in aliens[0:5]:
 print(alien)
print("......")
#显示创建了多少个外星人
#print("Total number of aliens: "+str(len(aliens)))
