class Berles:
    def __init__(self, auto, berlo_nev, datum):
        self.auto = auto
        self.berlo_nev = berlo_nev
        self.datum = datum

    def info(self):
        return f"{self.auto.rendszam} - {self.auto.tipus} - {self.berlo_nev} - {self.datum} - {self.auto.ar} Ft"
