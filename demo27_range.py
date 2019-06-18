#encoding=UTF-8
startRange = range(0, 20)
print startRange
for i in startRange:
    print i,
print "\n"
r2 = range(0, 10, 2)
print r2
# cmd
# pip install numpy
import numpy

r3 = numpy.arange(0, 20)
print type(r2), type(r3)
print r3
r4 = numpy.arange(0, 2, 0.1)
print r4
r5 = numpy.linspace(0, 20)
print r5
r6 = numpy.linspace(0, 20, 20)  #numpy.linspace 包頭也包尾,所以切20份要+1
print r6
r7 = numpy.linspace(0, 20, 21)
print r7