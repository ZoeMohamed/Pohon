from biner_ver2 import *
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

def BSearchX(P, x):
    if IsTreeEmpty(P):
        return False
    else:
        if Akar(P) == x:
            return True
        else:
            # if IsOneElement(P):
            #     return Akar(P) == x
            if isBiner(P):
                return BSearchX(Left(P), x) or BSearchX(Right(P), x)
            elif IsUnerLeft(P):
                return BSearchX(Left(P), x)
            elif IsUnerRight(P):
                return BSearchX(Right(P), x)

print (BSearchX(MakePB(10, MakePB(13, MakePB(3, [], []), MakePB(7, [], [])), MakePB(17, MakePB(5, [], []), MakePB(20, [], []))),5))