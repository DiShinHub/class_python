

class Calculator:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0
    
    def set_num1(self, num1):
        self.num1 = num1

    def set_num2(self, num2):
        self.num2 = num2

    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

    def get_result(self):
        return self.result

    def add_num(self):
        self.result = self.num1 + self.num2
        return self.result

    def minus_num(self):
        self.result = self.num1 - self.num2
        return self.result

    def multi_num(self):
        self.result = self.num1 * self.num2
        return self.result

    def div_num(self):

        if self.num2 == 0:
            print("0으로 나눌 수 없습니다")
            return False

        else:
            self.result = self.num1 / self.num2
            return self.result


cal = Calculator()

cal.set_num1(1)
cal.set_num2(2)
print(cal.get_num1())
print(cal.get_num2())

cal.add_num()
print(cal.get_result())

cal.minus_num()
print(cal.get_result())

cal.multi_num()
print(cal.get_result())

cal.div_num()
print(cal.get_result())

cal.__init__()
print(cal.get_result())

cal.div_num()