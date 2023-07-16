#vytvoření classy pojištenec s jeho atributy, od uživatele to nebude ctít jeho pořadové číslo, to je přiřazeno automaticky
class Pojistenec:
    poradnik = 0
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.cislo = Pojistenec.poradnik + 1
        self.vek = vek
        Pojistenec.poradnik += 1

#výpis při zavolání objektu
    def __str__(self):
        return f"{str(self.cislo).ljust(10)} {self.jmeno.ljust(10)} {self.prijmeni.ljust(10)} {str(self.vek).ljust(10)}" 

