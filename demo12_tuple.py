a = 6
b = 8
print 'a=%d,b=%d\n' % (a, b)
temp = a
a = b
b = temp
print 'a=%d,b=%d\n' % (a, b)
c = 7
d = 9
print 'c=%d, d=%d\n' % (c, d)
c, d = d, c
print 'c=%d, d=%d\n' % (c, d)
e = 3.14
f = 'pi'
print 'e,f', e, f
e, f = f, e
print 'e,f', e, f
first, second, third, fourth, fifth = 'A', 'K', 'Q', 'J', '10'
print first, second, third, fourth, fifth
third, fifth, first, fourth, second = first, second, third, fourth, fifth
print first, second, third, fourth, fifth
