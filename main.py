class Kitob:
    def __init__(self, nom, muallif, yil):
        self.nom = nom
        self.muallif = muallif
        self.yil = yil

    def malumot(self):
        return f"{self.nom} ({self.muallif}, {self.yil})"

class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, yil, format):
        super().__init__(nom, muallif, yil)
        self.format = format

    def malumot(self):
        return f"{self.nom} ({self.muallif}, {self.yil}, {self.format})"

class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qosh(self, kitob):
        self.kitoblar.append(kitob)
        return f"{kitob.nom} kutubxonaga qo’shildi."

    def kitoblar_royxati(self):
        return [kitob.malumot() for kitob in self.kitoblar]


kutubxona = Kutubxona()
kitob1 = Kitob("O’tkan kunlar", "Abdulla Qodiriy", 1926)
kitob2 = ElektronKitob("Python dasturlash", "John Doe", 2020, "PDF")

print(kutubxona.kitob_qosh(kitob1))
print(kutubxona.kitob_qosh(kitob2))
print(kutubxona.kitoblar_royxati())
