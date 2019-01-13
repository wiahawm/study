class Calc:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result +=num
        return self.result

    def sub(self,num):
        self.result -=num
        return self.result
    
    def mul(self,num):
        self.result *=num
        return self.result

    def div(self, num):
        try:
            self.result /=num
            if self.result.is_integer() == True:
                return int(self.result)
        except ZeroDivisionError:
            self.result="0으로는 나눌 수 없습니다."

        return self.result


calc=Calc()
print(calc.add(7))
print(calc.add(2))
print(calc.sub(5))
print(calc.mul(3))
print(calc.div(6))
print(calc.div(4))
print(calc.div(0))