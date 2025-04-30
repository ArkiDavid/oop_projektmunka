from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, ar):
        self.rendszam = rendszam
        self.tipus = tipus
        self.ar = ar

    @abstractmethod
    def info(self):
        pass

class Szemelyauto(Auto):
    def info(self):
        return f"Személyautó - {self.rendszam} ({self.tipus}) - {self.ar} Ft/nap"

class Teherauto(Auto):
    def info(self):
        return f"Teherautó - {self.rendszam} ({self.tipus}) - {self.ar} Ft/nap"
