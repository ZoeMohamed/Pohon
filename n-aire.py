def makeTreeN(A,PN=None):
    return [A,PN]

def Akar(P):
    return P[0]

def Anak(P):
    return P[1]

# Isempty
def isTreeEmpty(P):
    return P == []
def isOneElmnt(P):
    if  (not isTreeEmpty(P)) and Anak(P) == None:
        return True
    else:
        return False
    
def NbElement(P):
    pass

# [A[B,C]]
pohon = makeTreeN("A",[makeTreeN("B",["C","D","E"]),"I","K","N"])
akar = makeTreeN("x",makeTreeN("B","C"))
print(pohon)
print(isOneElmnt(akar))
print(akar)
print(NbElement(pohon))


# [a,[b[c,d,e,f,g]],i,k,n]