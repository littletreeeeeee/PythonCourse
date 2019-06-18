x = 5
print x, hex(id(x))
x = 6
print x, hex(id(x))
l = [5]
print l, hex(id(l))
l[0] = 6
print l, hex(id(l))

k=[1,2,3,4]

print k ,hex(id(k))

k[0]=2
k[1]=78
print k ,hex(id(k))