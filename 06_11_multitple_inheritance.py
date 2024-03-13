class Lister:
    def __repr__(self):
        return "<Instance of %s, addr : %s\n%s" % \
            (self.__class__.__name__, 
             id(self), 
             self.attrnames())                
                
    def attrnames(self):
        result = ""
        for attr in self.__dict__.keys():
            if attr[:2] == "__":
                result = result + "\tname %s = <built-ins>\n" % attr
            else:
                result = result + "\tname %s = %s\n" % (attr, self.__dict__[attr])
        return result
    

class Super:
    def __init__(self):
        self.data1 = "Superman"
    
class Sub(Super, Lister):
    def __init__(self):
        Super.__init__(self)
        self.data2 = "Subeggs"
        self.data3 = "Sub42"
        

if __name__ == "__main__":
    X = Sub()
    print(X)
        