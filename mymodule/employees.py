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
        
class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self,name,40000)
    def work(self):
        print(self.name + " interfaces with customers")    
        
class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self,name)
    def work(self):
        print(self.name + " makes pizza")        
