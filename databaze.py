from pojistenec import Pojistenec

#vytvoření classy Databaze, kde při jejím zavolání bude vytvořenen seznam pojištěnců 
class Databaze:
    def __init__(self):
        self.seznam_pojistencu = []

#přidá pojištence do databáze
    def pridat_pojistence(self):
        
        jmeno = input("Zadejte své jméno:\n")
        prijmeni = input("Zadejte své prijmeni:\n")
        vek = self.ziskej_cislo("Zadejte svůj věk:\n", povinne_cislo=True)

        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek)
        self.seznam_pojistencu.append(novy_pojistenec)
        print("Přidali jste nového pojištence")

#ošetření víjimky: Aby se při zadávání věku nebo vyhledávání dle čísla zadal INT, v případě vyhledávání může uživatel "odentrovat"
    def ziskej_cislo(self, zprava, povinne_cislo=True):
        while True:
            number = input(zprava)
            if number == "":
                if not povinne_cislo:
                    return ""
                else:
                    print("Musíš zadat číslo.")
            else:
                try:
                    return int(number)
                except ValueError:
                    print("Špatně jsi to zadal, chci po tobě číslo, kámo")

#vypíše pojištence
    def vypis_pojistence(self):

        for pojistenec in self.seznam_pojistencu:
            print(pojistenec)

#najde pojištence dle jména, příjmení, čísla, výsledek je jen return, print je ošetřen při zavolání funkce
    def najit_pojistence(self):

        najit_jmeno = input("Zadejte jméno, které chcete najít:\n")
        najit_prijmeni = input("Zadejte příjmení, které chcete najít:\n")
        najit_cislo = self.ziskej_cislo("Zadejte číslo pojištence, které chcete najít:\n", povinne_cislo=False)

        for pojistenec in self.seznam_pojistencu:
            if najit_jmeno == pojistenec.jmeno or najit_prijmeni == pojistenec.prijmeni or najit_cislo == pojistenec.cislo:
                return pojistenec
        print("Uživatel nebyl nalezen")

#smaže pojištěnce tak, že ho nejdříve najde využitím metody "nait_pojostence" a pak ho smaže  
    def smazat_pojistence(self):

        print("Pojďme si nejprave najít, toho, jehož jméno se nevyslovuje a kterého chceme smáznout")
        nalezeny_pojistenec = self.najit_pojistence()

        if nalezeny_pojistenec is not None:
            self.seznam_pojistencu.remove(nalezeny_pojistenec)
            print("Pojištěnec byl smazán, můžeme si to ověřit vypsáním databáze níže:")
            self.vypis_pojistence()
        else:
            print("Uživatel nebyl nalezen, a proto nemůže být logicky smazán")

#upraví pojištence ta, že ho nejdříve najde pomocí metody "najit_pojistence" 
    def upravit_pojistence(self):

        print("Nejprve pojďme najít pojištence, kterého chcete upravit...")
        nalazeny_pojistenec = self.najit_pojistence()

        if nalazeny_pojistenec is not None:
    
            nove_jmeno = input("Zadejte nové jméno:\n")
            nove_prijmeni = input("Zadejte nové příjmneí")
            novy_vek = self.ziskej_cislo("Zadejte nový věk:\n")

            nalazeny_pojistenec.jmeno = nove_jmeno
            nalazeny_pojistenec.prijmeni = nove_prijmeni
            nalazeny_pojistenec.vek = novy_vek

            print("Pojištenec byl upraven na:")
            print(nalazeny_pojistenec)
        
        else: 
            print("Uživatel nebyl nalezen, proto se nemůže upravit")

#tato metoda zapne celou aplikaci, je to lepší vypsat zde, aby main nebyl zahlcen
    def startuj(self):

        pokracovat = True
        while pokracovat:
            print("-----------------")
            print ("Vítejte v aplikace na správu pojištěnců".upper())
            print("Co si přejete udělat?")
            print("-----------------")
            print("Pro ZAVEDENÍ nového pojštěnce stiskněte --1--")
            print("Pro VÝPIS všech zapsaných pojištěnců stiskněte --2--")
            print("Pokud chcete NAJÍT nějakého pojištěnce, stiskněte --3--")
            print("Pokud chcete nějakého pojištence SMAZAT, stiskněte --4--")
            print("Pokud chcete nějakého pojištence UPRAVIT, stiskněte --5--")
            print("Pokud chcete UKONČIT aplikaci, stiskněte --6--")

            volba = input("Zadejte vaši volbu:\n")

            if volba == "1":
                self.pridat_pojistence()
            elif volba == "2":
                self.vypis_pojistence()
            elif volba == "3":
                print(self.najit_pojistence())
            elif volba == "4":
                self.smazat_pojistence()
            elif volba == "5":
                self.upravit_pojistence()
            elif volba == "6":
                pokracovat = False
            else:
                pass