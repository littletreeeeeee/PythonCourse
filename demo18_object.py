class Foo:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '[Foo]:Str format:%s' % (self.name)

    def __repr__(self):
        return '[Foo]:repr format:s%s' % (self.name)


f1 = Foo('ken')
f2 = Foo('mark')
print f1, f2
print '%s,%r' % (f1, f1)
print '{0!s}, {0!r}'.format(f1)

