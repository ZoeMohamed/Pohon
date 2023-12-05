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


def BSearchX(P, X):
    if IsTreeEmpty(P):
        return False
    if Akar(P) == X:
        return True
    else:
        if (IsOneElement(P)):
            if (Akar(P) == X):
                return True
            else:
                return False
        else:
            if X < Akar(P):
                return BSearchX(Left(P), X)
            else:
                return BSearchX(Right(P), X)
            
def BSearchX2(P, X):
    if IsTreeEmpty(P):
        return False

    if Akar(P) == X:
        # Handle duplicate values
        while Akar(P) == X:
            if IsOneElement(P):
                return True
            P = Right(P)
        return False

    elif X < Akar(P):
        return BSearchX2(Left(P), X)

    else:
        # Corrected code: Continue searching in the right subtree
        return BSearchX2(Right(P), X)

            
      
pohon = MakePB('a',MakePB('b',[],[]),MakePB('c',[],[]))
print(BSearchX(pohon,'b'))
print(BSearchX2(pohon,'b'))


    