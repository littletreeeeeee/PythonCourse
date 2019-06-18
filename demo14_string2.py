a1 = 'abcdefg1234567'
print 'cde' in a1, 'CDE' in a1, 'cde' not in a1, 'CDE' not in a1

a2 = 'kkk'
print a1 + a2, a1 * 3, 5 * a2

a3 = a1 * 5
print a1[1:20:2]
print min(a3), max(a3)

a4 = '12345ABCDEabcde'
print min(a4), max(a4)

print a1.index('b'), a1.index('1')

if 'xxx' in a1:
    print a1.index('xxx')
else:
    print "oh no "

if 'fg' in a1:
    print a1.index('fg')
else:
    print "oh no "

print a1.count('1'), a1.count('ppp')
