def MakePB(A, L,R):
    return [A, L, R]
def IsTreeEmpty(P):
    return P == []
def IsOneElement(P):
    if not IsTreeEmpty(P) and  IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else:
        return False
def Akar(P):
    return P[0]

def Left(P):
    return P[1]

def Right(P):
    return P[2]

def Depth(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElement(P):
        return 1
    else:
  
        return 1 + max(Depth(Left(P)), Depth(Right(P)))


['a',['b',[],[]],[]]
print(Depth(MakePB("A",MakePB("B",[],[]),[])))


