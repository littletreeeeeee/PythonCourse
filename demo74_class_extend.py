#endcoding=utf-8
class EmpBoss:
    bigBoss="子賢"

class Emp(EmpBoss):
    gradeLevel = 6
    hungryOrNot = True

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    tool = "rolaiba";
    pass


class PM(Emp):
    tool = "office";
    hungryOrNot = False
    pass


print "RD, PM, Emp grade level=", RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel
RD.gradeLevel = 7
print "RD, PM, Emp grade level=", RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel
Emp.gradeLevel = 8
print "RD, PM, Emp grade level=", RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel

print "RD, PM, Emp grade tool=", RD.tool, PM.tool, 'no tool'

print "RD, PM, Emp grade hungryOrNot=", RD.hungryOrNot, PM.hungryOrNot, Emp.hungryOrNot

print "RD, PM, Emp grade BigBoss=", RD.bigBoss, PM.bigBoss,Emp.bigBoss
