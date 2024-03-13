def factory(aClass, *args):
    #return apply(aClass, args)
    return aClass

class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job


obj1 = factory(Spam)
obj2 = factory(Person)