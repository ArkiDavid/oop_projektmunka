from auto import Szemelyauto, Teherauto
from autokolcsonzo import Autokolcsonzo
from datetime import date

def main():
    kolcsonzo = Autokolcsonzo("Villám Rent")

    # Előre feltöltött autók
    auto1 = Szemelyauto("ABC123", "Toyota Corolla", 10000)
    auto2 = Szemelyauto("DEF456", "Suzuki Swift", 8000)
    auto3 = Teherauto("GHI789", "Ford Transit", 15000)

    kolcsonzo.hozzaad_auto(auto1)
    kolcsonzo.hozzaad_auto(auto2)
    kolcsonzo.hozzaad_auto(auto3)

    # Előre feltöltött bérlések
    kolcsonzo.berel_auto("ABC123", "Kiss József", date(2025, 4, 30))
    kolcsonzo.berel_auto("DEF456", "Nagy Anna", date(2025, 4, 30))
    kolcsonzo.berel_auto("GHI789", "Tóth Péter", date(2025, 5, 1))
    kolcsonzo.berel_auto("ABC123", "Fekete Réka", date(2025, 5, 1))

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            rendszam = input("Adja meg a rendszámot: ")
            nev = input("Adja meg a bérlő nevét: ")
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN): ")
            try:
                ev, ho, nap = map(int, datum_str.split("-"))
                datum = date(ev, ho, nap)
                sikeres, uzenet = kolcsonzo.berel_auto(rendszam, nev, datum)
                print(uzenet)
            except Exception as e:
                print("Hibás dátumformátum.")

        elif valasztas == "2":
            rendszam = input("Rendszám: ")
            datum_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                ev, ho, nap = map(int, datum_str.split("-"))
                datum = date(ev, ho, nap)
                sikeres = kolcsonzo.lemond_berles(rendszam, datum)
                if sikeres:
                    print("Bérlés sikeresen törölve.")
                else:
                    print("Nem található ilyen bérlés.")
            except:
                print("Hibás dátumformátum.")

        elif valasztas == "3":
            kolcsonzo.listaz_berlesek()

        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen opció.")

if __name__ == "__main__":
    main()
