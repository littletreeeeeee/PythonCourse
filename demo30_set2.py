#encoding=utf-8
class Course:
    def __init__(self, name, hour):
        self.name = name
        self.hour = hour

    def __str__(self):
        return "[%s]%s" % (str(self.name), str(self.hour))

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.name, self.hour))

    def __eq__(self, other):  #要先有Hash 才可以有 Eq ,若都一樣視為同的記憶體位置
        return self.name == other.name and self.hour == other.hour


c1 = Course('BDPY', 35)
c2 = Course('BDPY', 35)
c3 = c1
c4 = Course('PYKT', 35)
c5 = Course('BDPY', 42)
s1 = {c1, c2, c3, c4, c5}
s2 = {c1, c3}
print type(s1), s1
print type(s2), s2