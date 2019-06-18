a1 = "abc"
a2 = ['a', 'b', 'c']
print type(a1), len(a1), a1,hex(id(a1))
print type(a2), len(a2), a2,hex(id(a2))
print a1[1:],hex(id(a1)), a2[1:],hex(id(a2))
a2[1] = 'B'
print a2,hex(id(a2))
a1="cde"
print a1,hex(id(a1))
a1 = "abc"
print a1,hex(id(a1))


a3 = list("ABCDEFG1234567" * 2)
print a3
a3[:5] = 'T'
print a3
del a3[:5]
print a3
a3[1:5:2]='*'*2
print a3
