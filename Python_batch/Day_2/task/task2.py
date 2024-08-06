# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.

class Numbers:
    pass
class Arithmetic:
    def __init__(self,values) -> None:
        self.values = values
    def checkPrime(self):
        result = False
        for trash in range(2,self.values):
            if self.values%trash == 1:
                result = True
            else:
                result = False
                break
        return result
    def checkperfect(self):
        pass
        # return True
    def sumfactors(self):
        pass
        # return True
    def factoes(self):
        pass
        # return True
obj1=Arithmetic(4)
print(obj1.checkPrime())
    
    
