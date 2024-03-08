verbose = 1

def listing(module):
    if verbose:
        print ("-"*30)
        print ("name : ", module.__name__," file : ",module.__file__)
        print ("-"*30)
    
    count = 0
    for key in module.__dict__.keys():        
        count = count + 1
        print("[%02d] %s" % (count, key))
        
        
    if verbose:
        print("-"*30)
        print(module.__name__, " has %d names." % count)            
        print("-"*30)
        

if __name__ == "__main__":
    import _05_05_meta #파일명의 첫글자에 숫자는 안됨!!!!
    listing(_05_05_meta)
        