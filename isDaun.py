from biner_ver2 import *

def isDaun(x,P):
    if IsOneElmnt(P):
        if x != akar(P):
            return True
        elif x == akar(P):
            return False
    else:
        if isBiner(P):
            return isDaun(x,left(P)) or isDaun(x,right(P))
        elif IsUnerLeft(P):
            return isDaun(x,left(P))
        elif IsUnerRight(P):
            return isDaun(x,right(P))
        
pohon = tree('a',tree('b',tree('x',tree('c',tree('d',[],[]),[]),[]),[]),tree('xx',[],[]))
print(isDaun('a',pohon))