def makePb(A, L=None, R=None):
    return [A, L, R]

def akar(P):
    return P[0]


def left(P):
    return P[1]


def right(P):
    return P[2]


def is_member(P, x):
    if is_tree_empty(P):
        return False
    else:
        if akar(P) == x:
            return True
        else:
            if is_one_element(P):
                return akar(P) == x
            elif is_biner(P):
                return is_member(left(P), x) or is_member(right(P), x)
            elif is_uner_left(P):
                return is_member(left(P), x)
            elif is_uner_right(P):
                return is_member(right(P), x)

def is_tree_empty(P):
    if P == None:
        return True
    else:
        return False


def is_one_element(P):
    if not (is_tree_empty(P)) and is_tree_empty(left(P)) and is_tree_empty(right(P)):
        return True
    else:
        return False


def is_uner_left(P):
    if (not (is_tree_empty(P)) and not (is_tree_empty(left(P))) and is_tree_empty(right(P))):
        return True
    else:
        return False


def is_uner_right(P):
    if (not (is_tree_empty(P)) and is_tree_empty(left(P)) and not (is_tree_empty(right(P)))):
        return True
    else:
        return False


def is_biner(P):
    if (not (is_tree_empty(P)) and not (is_tree_empty(left(P))) and not (is_tree_empty(right(P)))):
        return True
    else:
        return False


def repPrefixPB(P):
    if is_one_element(P):
        return [akar(P)]
    else:
        if is_biner(P):
            return [akar(P)] + repPrefixPB(left(P)) + repPrefixPB(right(P))
        elif is_uner_left(P):
            return [akar(P)] + repPrefixPB(left(P))
        elif is_uner_right(P):
            return [akar(P)] + repPrefixPB(right(P))


def nbDaunPB(P):
    if is_one_element(P):
        return 1
    elif is_biner(P):
        return nbDaunPB(left(P)) + nbDaunPB(right(P))
    elif is_uner_left(P):
        return nbDaunPB(left(P))
    elif is_uner_right(P):
        return nbDaunPB(right(P))


p = ((('a', (makePb('b',makePb('d',None,None),makePb('f',None,None))), (makePb('c',makePb('g',None,None),makePb('h',None,makePb('I',None,None)))))))
# print(nbDaunPB(makePb('a', (makePb('b',makePb('d',None,None),makePb('f',None,None))), (makePb('c',makePb('g',None,None),makePb('h',None,makePb('I',None,None)))))))
# print (repPrefixPB(p))
# print (is_member(p,'z'))

def BSearchX(P, X):
    if is_tree_empty(P):
        return False
    if akar(P) == X:
        return True
    else:
        if (is_one_element(P)):
            if (akar(P) == X):
                return True
            else:
                return False
        else:
            if X < akar(P):
                return BSearchX(left(P), X)
            else:
                return BSearchX(right(P), X)

p = ((('a', (makePb('b',makePb('d',None,None),makePb('f',None,None))), (makePb('c',makePb('g',None,None),makePb('h',None,makePb('I',None,None)))))))
print(BSearchX(p, 'a')) 
print(BSearchX(p, 'z'))
print(BSearchX(p, 'I'))