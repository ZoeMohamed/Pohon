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

def TebangPohon(P):
    if IsTreeEmpty(P):
        return []
    else:
        return [Akar(P)] + TebangPohon(Left(P)) + TebangPohon(Right(P))
        # [a,[b,[],[]],[c,[],[]]]
        # [a] + TebangPohon([b,[],[]]) + TebangPohon([c,[],[]])
        # TebangPohon([b,[],[]]) -> [b]
        # TebangPohon([c,[],[]]) -> [c]

        # [a] + [b] + [c]

        # [a,[b,[1,[],[]],[]],[c,[],[]]]
        # [a] + TebangPohon([b,[1,[],[]],[]]) + TebangPohon([c,[],[]])
        # TebangPohon([b,[1,[],[]],[]])
        # TebangPohon([1,[],[]])
def FirstElement(L):
    return L[0]
def Konso(x,L):
    return [x] + L
def Tail(L):
    return L[1:]

def Insert(x,L):
    if L == []:
        return [x]
    else:
        if (x <= FirstElement(L) ):
            return Konso(x,L)
        else:
        
            return Konso(FirstElement(L),Insert(x,Tail(L)))

def Insort(L):
    if L == []:
        return []
    else:
        return Insert(FirstElement(L),Insort(Tail(L)))
def Flatten(P):
    return Insort(TebangPohon(P))
print(MakePB("a",MakePB('a',[],[]),[]))
print(TebangPohon(MakePB("a",MakePB('a',[],[]),[])))
print(["aa"] + ["bb"] + ["cc"])
# def Flattenx(P):
#     result = [Akar(P)]
    
#     if Left(P) is not None:
#         result.extend(Flattenx(Left(P)))
    
#     if Right(P) is not None:
#         result.extend(Flattenx(Right(P)))
    
#     return result
# def Flatten(P):
#     listx = Flattenx(P)
#     listx.sort()
#     return listx





