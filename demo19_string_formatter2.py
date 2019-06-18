# encoding=UTF-8
print '==%10s==' % ('0123456789')
print '==%10s==' % ('0123456789'[:5])
print '==%10s==' % ('0123456789' * 2)
print '==%10s==' % ('中文')
print '==%10s==' % (u'中文')
print '=={:10}=='.format('01234')
print '=={:>10}=='.format('01234')
print '=={:>10}=='.format('中文')
print u'=={:>10}=='.format(u'中文')

