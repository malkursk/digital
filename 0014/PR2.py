
p1 = input('персона 1: ')
p2 = input('персона 2: ')
p3 = input('персона 3: ')
print('присутствуют' , p1,p2,p3)


m1 = p1.split()
m2 = p2.split()
m3 = p3.split()

m = [ m1[1]+' '+m1[0],m2[1]+' '+m2[0],m3[1]+' '+m3[0],]

m.sort()
print(m)

m1 = m[0].split()
m2 = m[1].split()
m3 = m[2].split()

print (m1[0],m2[0],m3[0])                     
