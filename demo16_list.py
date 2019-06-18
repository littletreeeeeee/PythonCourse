a1 = list('abc')
a2 = list('def')
a1.append(a2)
print 'append==>', a1
a3 = list('abc')
a4 = list('def')
a3.extend(a4)
print 'extend==>', a3
a5 = list('abc')
a6 = list('def')
print '+ ==>', a5 + a6
a7 = list('abc')
a8 = list('def')
for x in a8:
    a7.append(x)
print 'append each by each==>', a7

a8 = list('abc')
a9 = list('def')
print '+ ==>', a8.append(a9)+a8 + a9