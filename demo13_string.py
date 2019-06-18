str1 = 'abcdefg1234567'
print type(str1), len(str1), str1
print str1[0], str1[len(str1)-1]
#print str1[len(str1)]
print str1[2:7]
print str1[:7], str1[7:]
print str1[7:14]

str2 = 'www.uuu.com.tw'
print(str2.split('.'))
print '#'.join(str2.split('.'))
