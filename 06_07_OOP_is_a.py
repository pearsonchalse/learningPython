class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self,perc):
        self.salary = self.salary + (self.salary * perc)
    def work(self):
        print(self.name + " does something...")
    def __repr__(self):
        return "<Employee> name : %s, salary : %s " % (self.name, self.salary)
    
class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self,name,50000)
    def work(self):
        print(self.name + " makes food")    
        
class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self,name)
    def work(self):
        print(self.name + " makes pizza")        
        
        
if __name__ == "__main__":
    bob = PizzaRobot("bob")
    print(bob)
    bob.giveRaise(0.2)
    print(bob)
    print()        
    
    
    for cl in Employee, Chef, PizzaRobot:
        obj = cl(cl.__name__) # cl.__name__ : Employee, Chef, PizzaRobot의 클래스이름을 스트링으로 변환
        obj.work()