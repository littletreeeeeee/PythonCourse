dayOfWeek = ('sunday', 'monday')
print type(dayOfWeek), len(dayOfWeek)
dayOfWeek += ('tuesday', 'wednesday')
print dayOfWeek
dayOfWeek += ('thursday',)
print dayOfWeek
print type(('thursday')), type(('thursday',))
print ('thursday') * 5
print('thursday',) * 5
print dayOfWeek[0], dayOfWeek[len(dayOfWeek) - 1]
print dayOfWeek[-1], dayOfWeek[-len(dayOfWeek)]
# print dayOfWeek[len(dayOfWeek)]
list1 = list('ABCDEFG1234567abcdefg')
print list1[0], list1[len(list1) - 1]
print list1[-1], list1[-(len(list1))]


def split_head(seq):
    return seq[0], seq[1:]


p, q = split_head(list1)
print type(p), p
print type(q), q