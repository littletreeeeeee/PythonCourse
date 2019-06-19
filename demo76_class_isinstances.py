class Emp:
    pass


class Engineer(Emp):
    pass


class Pm(Emp):
    pass


class Hr(Emp):
    pass


emp1 = Emp()
engineer1 = Engineer()
pm1 = Pm()
hr1 = Hr()
staffs = [(emp1, "First Employee"), (engineer1, "First Engineer"), (pm1, "First PM"), (hr1, "First HR")]
print "Staffs ",staffs
emp_classes = [Emp, Pm, Hr, Engineer]

for staff, name in staffs:
    print '----------------------------'
    for emp_class in emp_classes:
        isA = isinstance(staff, emp_class) #函数来判断一个对象是否是一个已知的类型，类似 type()。
        msg1 = 'is a' if isA else 'is not a'
        print name, msg1, emp_class.__name__
