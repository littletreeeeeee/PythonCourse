#encoding=utf=8

class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.day * self.member

    # @classmethod
    # def get_member(cls):
    #     return cls.member

    @classmethod  #給Class用的方法，Class可以直接取得值，時做的也可以 =>不用實體化就可以使用
    def get_member(cls):
        return cls.member

    @staticmethod
    def calculate(x, y):
        return x ** y


t1 = Team()
print t1.all_working_hour()  #all_working_hour 要在working_hour前呼叫，不然day還沒有生成
print t1.working_hour()

print t1.get_member(), Team.get_member()
print t1.calculate(2, 3), Team.calculate(3, 2)
