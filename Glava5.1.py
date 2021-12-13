x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jb = x[9:]
int(''.join(map(str, jb)))
x[9:] = []
sd = x[8:]
int(''.join(map(str, sd)))
x[8:] = []
sf = x[7:]
int(''.join(map(str, sf)))
x[7:] = []
x.reverse()

x.extend(jb)
x.extend(sd)
x.extend(sf)
x.reverse()
#x.insert(-7,jb)
#x.insert(-8,sd)
#x.insert(-9,sf)
print(x)

