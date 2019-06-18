def sample_fix(x1, x2, x3):
    print 'first element:', x1
    print 'second element:', x2
    print 'third element:', x3


sample_fix('apple', 'banana', 'citron')
sample_fix(*('apple', 'banana', 'citron'))
sample_fix('apple', *('banana', 'citron'))
sample_fix(*('7-11', 'Fami'), x3='OK')


#Test
def test(fix1, fix2, *args,**kargs):
    print "fix part1=%s, part2=%s" % (str(fix1), str(fix2))
    for p in args:
        print p
    for k, v in kargs.items():
        print 'key=%s, value=%s' % (str(k), str(v))


test('hey','You',1,2,3,4,5,*{'course': 'BDPY', 'duration': 35, 'instructor': 'MarkHo'})
