def tree(A,L,R):
    return [A,L,R]
def akar(A):
    return A[0]
def left(L):
    return L[1]
def right(L):
    return L[-1]

def IsOneElmnt(P):
    if not(IsTreeEmpty(P)) and IsTreeEmpty(right(P)) and IsTreeEmpty(left(P)):
        return True
    else:
        return False
def IsTreeEmpty(P):
    if P == []:
        return True
    else:
        return False
# Sub Pohon Kiri Tidak Boleh Kosong dan Sub Pohon Kanan harus Kosong
def IsUnerLeft(P):
    if not(IsTreeEmpty(P)) and not(IsTreeEmpty(left(P))) and IsTreeEmpty(right(P)):
        return True
    else:
        return False

# Sub Pohon Kanan Tidak Boleh Kosong dan Sub Pohon Kiri harus Kosong

def IsUnerRight(P):
    if not(IsTreeEmpty(P)) and not(IsTreeEmpty(right(P))) and IsTreeEmpty(left(P)):
        return True
    else:
        return False

def isBiner(P):
    if not (IsTreeEmpty(P)) and not(IsTreeEmpty(right(P))) and not(IsTreeEmpty(left(P))):
        return True
    else:
        return False
def NbDaun(P):
    if IsTreeEmpty(P):
        return 0
    else:
        if IsOneElmnt(P):
            return 1
            # [1,[1,[],[]]]
        elif isBiner(P):
            return NbDaun(left(P)) + NbDaun(right(P))
        elif IsUnerLeft(P):
            return NbDaun(left(P)) 
        elif IsUnerRight(P):
            return NbDaun(right(P)) 


def NbElement(P):
    if IsTreeEmpty(P):
        return 0
    else:
        return NbElement(left(P)) + 1 + NbElement(right(P))
        # Plus 1 disini artinya sudah include root paling atas dari sebuah pohon
        # jadi jika rooot kita input [] tetap dihitung 

        # NbElement(left(P))
        # NbElement(['a',['c',[],[]],[]]) # 2

        # NbElement(right(P))
        # NbElement(['b',[],[]])

x = tree(1,tree('a',tree('c',[],[]),[]),tree('b',[],[]))
y = tree(1,tree(1,[],[]),tree(2,[],[]))
print(x)
print(NbElement(x))
print(NbDaun(y))
# A['B'['D','E'],'C'['G','H'[None,'I']]]