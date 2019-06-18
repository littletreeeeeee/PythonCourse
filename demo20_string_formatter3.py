# encoding=UTF-8
print '==%10s==' % ('0123456789')
print '==%10s==' % ('01234')
print '==%-10s==' % ('01234')
print '==%*s==' % (-10, '01234')
print '==%*s==' % (10, '01234')
print '=={:<10s}=='.format('01234')
print '=={:>10s}=='.format('01234')
print '=={:<{}s}=='.format('01234', 10)
print '=={:>{}s}=='.format('01234', 10)

# :< is default 左縮排
# :> is default 右縮排又縮排
#%10



