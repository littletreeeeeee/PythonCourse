# encoding=UTF-8
p=u'中文輸入'
print repr(p)
print repr(p.encode('UTF-8'))
print repr(p.encode('UTF8'))
print repr(p.encode('ms950'))
print repr(p.encode('big5'))
#print p.encode('ms950')