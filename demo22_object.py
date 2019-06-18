x = 8
print "x=", x, ", x id=", hex(id(x))
x = 9
print "x=", x, ", x id=", hex(id(x))


class Person:
    def __init__(self, age,jojo):
        self.age = age




p1 = Person(8)
print "p1 id=", hex(id(p1)), ", p1.age=", p1.age, " ,p1.age id=", hex(id(p1.age))
p1.age = 9
print "p1 id=", hex(id(p1)), ", p1.age=", p1.age, " ,p1.age id=", hex(id(p1.age))

y=8
print "y=", y, ", y id=", hex(id(y))
