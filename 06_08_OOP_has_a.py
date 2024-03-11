import sys
import os
#현재 폴더의 절대경로를 알아낸 다음 하위폴더(mymodule)을 추가
sys.path.append(os.path.abspath(os.path.dirname(__file__))+"\\mymodule") 

from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name," orders from ",server)
            
    def pay(self, server):
        print(self.name," pays for item to ",server)
        

class Oven:
    def bake(self):
        print("oven bakes ... ")

        
class PizzaShop:
    def __init__(self):
        self.server = Server("John")        
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)
        
if __name__ == "__main__":
    scene = PizzaShop()
    scene.order("Customer1")
    print("...")
    scene.order("customer2")
            
        