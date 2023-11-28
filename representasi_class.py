class Pohon:
    def __init__(self,akar=None,left=None,right=None) -> None:
        self.akar = akar
        self.left = left
        self.right = right

pohon = Pohon(akar="C",left=Pohon(akar="I",left=Pohon("N"),right=Pohon("D",left=Pohon(akar="U",left=Pohon("T"),right=Pohon("P")),right=Pohon("N"))))

print(pohon.left.akar)
# akses properti left yang berada pada properti akar
# child->akar

print(pohon.left.right.left.right.akar) # --> Properti Akar Buat Akses Hurufnya
