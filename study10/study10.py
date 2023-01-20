# 创建类



#最基本的定义类的语法
class CAR :
    brand = '奔驰'
    country = '德国'

    @staticmethod
    def run() :
        print('running')

#调用默认值
"""
print(f'brand = {CAR.brand}')
CAR.run()
"""

#创建实例
"""
car_1 = CAR()

print(f'car_1.brand = {car_1.brand}')
car_1.run()
"""


#构造函数__init__

class Car :
    brand = '奔驰'
    country = '德国'

    def report(self) :
        print(f'self.beand   = {self.brand}')
        print(f'self.country = {self.country}')

    def __init__(self) :
        self.color = 'red'
        self.engineSN = '666'

    def changeColor(self,newColor):
        self.color = newColor

"""
#创建实例
car_2 = Car()

#调用
car_2.report()
print(f'car_2.color = {car_2.color}')
car_2.changeColor('yellow')
print(f'newColor = {car_2.color}')
"""


#继承
class BMW_car(Car) :
    year = '2020'
    def logo(self) :
        print('is BMW')

class DZ_car(Car) :
    years = '2021'
    def logos(self) :
        print('is DZ')

"""
#创建
car_3 = BMW_car()
car_4 = DZ_car()

#调用自己的方法和属性
print(f'car_3.year = {car_3.year}')
print(f'car_4.year = {car_4.years}')

car_3.logo()
car_4.logos()
#调用父类的方法
car_3.report()
car_4.report()
"""

#对于构造函数,也是需要显式调用

class BaseClass :
    var1, var2 = 0, 0

    def fun_base(self) :
        print('base fun running')

    def __init__(self, var1, var2) :
        self.var1, self.var2 = var1, var2

class DeriveClass(BaseClass) :
    var3, var4 = 0, 0

    def fun_derive(self) :
        print('derive fun running')

    def __init__(self, Var1, Var2, Var3, Var4) :
        BaseClass.__init__(self, Var1, Var2)
        self.var3, self.var4  = Var3, Var4

"""
test = DeriveClass(1,2,3,4)

print(f'test.var1 = {test.var1}')
print(f'test.var2 = {test.var2}')
print(f'test.var3 = {test.var3}')
print(f'test.var4 = {test.var4}')
"""

