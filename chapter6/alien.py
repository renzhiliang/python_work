alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))
#根据速度决定位移
if alien_0['speed']=='slow':x_increment=1
elif alien_0['speed']=='medium':x_increment=2
else:x_increment=3
#新坐标等于旧坐标加位移
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position: "+str(alien_0['x_position']))


