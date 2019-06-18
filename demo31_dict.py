sales = {'iphone6': 500, 'iphone7': 800, 'iphone8': 1000, 'iphoneXS': 1800}
print type(sales)
print sales['iphoneXS'], sales['iphone8']
# print sales['xxxx']
print sales.get('iphoneXR'), sales.get('iphoneXS')
sales['iphoneXR'] = 700
print sales
print 'watch4' in sales, 'iphone7' in sales
for x in sales:
    print x,sales[x]

for x in sales.keys():
    print x, sales.get(x)

for y in sales.values():
    print y,
print "\n"

for z  in sales.items():
    print type(z),z[0],z[1]

sales.update({'ipad':300,'iphone7':1800})
for p,q in sales.items():
    print p,q