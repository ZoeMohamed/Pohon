from biner_ver2 import *
def isSimpul(x, P):
    if IsOneElmnt(P):
        return akar(P) == x
    else:
      # Khusus ngecek kalo [a,[b,d],c]
      if akar(P) == x :
          return True
      elif isBiner(P):
          return isSimpul(x, left(P)) or isSimpul(x, right(P))
      # [b,d] or [c]
      elif IsUnerLeft(P):
          return isSimpul(x, left(P))
      # [b,d] -> False
      # [b,d] -> True kalo yang dicari b
      elif IsUnerRight(P):
          return isSimpul(x, right(P))
      # [c] -> True
        
pohon = tree('a',tree('b',tree('d',[],[]),[]),tree('c',[],[]))
print(isSimpul('dx',pohon))