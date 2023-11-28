def MakePB(A,L=None,R=None):
    return [A,L,R]

def Akar(P):
    return P[0]

def Left(P):
    return P[1]

def Right(P):
    return P[2]



def IsTreeEmpty(P):
    if P == None:
        return True
    else:
        return False
    
def Nbelement(P):
    if IsTreeEmpty(P):
        return 0
    else:
        return Nbelement(Left(P)) + 1 + Nbelement(Right(P))
    
biner = MakePB("A",MakePB("B",MakePB("D")),MakePB("C"))
print(biner)
print(Nbelement(biner)    )