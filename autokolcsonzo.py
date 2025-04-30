from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def hozzaad_auto(self, auto):
        self.autok.append(auto)

    def keres_auto(self, rendszam):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                return auto
        return None

    def berel_auto(self, rendszam, berlo_nev, datum):
        auto = self.keres_auto(rendszam)
        if not auto:
            return False, "Nincs ilyen rendszámú autó."

        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                return False, "Az autó már foglalt ezen a napon."

        self.berlesek.append(Berles(auto, berlo_nev, datum))
        return True, f"Bérlés sikeres! Ár: {auto.ar} Ft"

    def lemond_berles(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                return True
        return False

    def listaz_berlesek(self):
        if not self.berlesek:
            print("Nincsenek aktív bérlések.")
        else:
            for berles in self.berlesek:
                print(berles.info())
