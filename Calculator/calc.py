class calc:
    def add(*args):
        sum = 0
        for nums in args:
            sum = sum + nums
        return sum
    
    def subt(a,b):
        diff = 0
        diff = float(a-b)
        return diff

    def multiply(*args):
        prod = 1
        for nums in args:
            prod = prod*nums
        return prod
    

    def divide(a,b):
        quo = 0
        quo = a/b
        return quo

'''
DRIVER CODE
print(calc.add(1,2,45))
print(calc.multiply(2,5,6))
print(calc.divide(4,2))
print(calc.subt(-5,3))

'''  
