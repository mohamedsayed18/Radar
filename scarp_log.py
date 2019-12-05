azmu=[]
rad_dist=[]
vel=[]
fh=open("candump-2019-12-05_104350.log")
for i in fh:
    i=i.split('#')
    #print(i[1][0])
    #print(i[1][1])
    rad_dist.append(int(i[1][4:6],16))
    azmu.append(int(i[1][6:8],16))
    vel.append(int(i[1][9:12],16))
print("vel")
print(vel)
print("azmu angle")
print(azmu)
print("rad_dist")
print(rad_dist)
