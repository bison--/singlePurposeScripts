
class ClassName:
    @staticmethod
    def myFoo(a, b):
        return a * b

# other file
#from myfile import ClassName
myMethodX = ClassName.myFoo

print(myMethodX(10, 20))
