
# 1
from dataclasses import dataclass

@dataclass
class Talaba:
    ism: str
    yosh: int
    guruh: int
    ortacha_baho: int

    def stipendiya(self):
        return self.ortacha_baho >= 45


s = Talaba("Ali", 24, 3, 67)

print(s.stipendiya())




# 2
from dataclasses import dataclass

@dataclass
class Kitob:
    nomi: str
    muallif: str
    sahifa_soni: int
    narx: int


    def chegirma(self):
        self.narx = self.narx * 0.9
        print("10 % chegirma bn sotib olishingiz mumkin")


k = Kitob("UFQ", "Said Ahmad", 636, 70)

print(k.chegirma())




# 3
from dataclasses import dataclass

@dataclass
class Avtomobil:
    marka: str
    model: str
    yil: int
    tezlik: int

    def tezlik_oshirish(self):
        self.tezlik += 10
        return self.tezlik

    def tezlik_kamaytir(self):
        self.tezlik -= 10
        return self.tezlik


tezlik = Avtomobil("bmw m5", 'bmw', 1908, 200)

print(tezlik.tezlik_oshirish())
print(tezlik.tezlik_kamaytir())

