from pojistenec import Pojistenec
import sqlite3

#vytvoření classy Databaze, kde při jejím zavolání bude vytvořenen seznam pojištěnců 
class Databaze:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pojistenci (
                id INTEGER PRIMARY KEY,
                jmeno TEXT,
                prijmeni TEXT,
                vek INTEGER
            )
        ''')
        self.conn.commit()

#přidá pojištence do databáze
    def pridat_pojistence(self):
        
        jmeno = self.ziskej_text("Zadejte své jméno:\n",povinny_text=True)
        prijmeni = self.ziskej_text("Zadejte své prijmeni:\n", povinny_text=True)
        vek = self.ziskej_cislo("Zadejte svůj věk:\n", povinne_cislo=True)

        self.conn.execute('''
            INSERT INTO pojistenci (jmeno, prijmeni, vek)
            VALUES (?, ?, ?)
        ''', (jmeno, prijmeni, vek))

        self.conn.commit()

        print(f"Přidali jste nového pojištence:\n{jmeno} {prijmeni}, Věk: {vek}")

#ošetření výjimky: Aby se při zadávání jména nebo vyhledávání dle jména zadal text, v případě vyhledávání může uživatel "odentrovat"
    def ziskej_text(self, zprava, povinny_text=True):
        while True:
            text = input(zprava)
            if text == "":
                if not povinny_text:
                    return ""
                else: print("Musíš zadat text!!!")
            
            else: 
                try:
                    for i in text:
                        if i.isdigit():
                            raise ValueError("Špatně jsi to zadal, chci po tobě pouze text!")
                    break  
                except ValueError as e:
                    print(e)                    
        return str(text)
                                
#ošetření výjimky: Aby se při zadávání věku nebo vyhledávání dle čísla zadal INT, v případě vyhledávání může uživatel "odentrovat"
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
                    if int(number) >= 0 and int(number)<= 150:
                        return int(number)
                    else: print("Můžeš zadat pouze reálné rozmezí od 0 do 150!!!")

                except ValueError:
                    print("Špatně jsi to zadal, chci po tobě číslo, kámo")

#vypíše pojištence
    def vypis_pojistence(self):

        self.cursor.execute('SELECT * FROM pojistenci')
        records = self.cursor.fetchall()

        print("ID".ljust(10), "JMÉNO".ljust(10), "PŘÍJMENÍ".ljust(10), "VĚK".ljust(10))
        for record in records:
            id, jmeno, prijmeni, vek = record
            print(f"{str(id).ljust(10)} {str(jmeno).ljust(10)} {str(prijmeni).ljust(10)} {str(vek).ljust(10)} ")

#najde pojištence dle jména, příjmení, čísla, výsledek je jen return, print je ošetřen při zavolání funkce

    def najit_pojistence(self):

        id = self.ziskej_cislo("Zadejte id, které chcete najít:\n", povinne_cislo=False)
        jmeno = self.ziskej_text("Zadejte jméno, které chcete najít:\n", povinny_text=False)
        prijmeni = self.ziskej_text("Zadejte příjmení, které chcete najít:\n", povinny_text=False)
        vek = self.ziskej_cislo("Zadejte věk, které chcete najít:\n", povinne_cislo=False)

        query = "SELECT * FROM pojistenci"
        conditions = []
        values = []

        if id:
            conditions.append(f"id = ?")
            values.append(id)
        if jmeno:
            conditions.append(f"jmeno = ?")
            values.append(jmeno)
        if prijmeni:
            conditions.append(f"prijmeni = ?")
            values.append(prijmeni)
        if vek:
            conditions.append(f"vek = ?")
            values.append(vek)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        self.cursor.execute(query, values)
        records = self.cursor.fetchall()

        if records:
            for record in records:
                id, jmeno, prijmeni, vek = record
                print(f"ID: {id}, Jméno: {jmeno}, Příjmení: {prijmeni}, Věk: {vek}")
            return records
        else:
            print("Pojištěnci nebyli nalezeni.")
            return None

#smaže pojištěnce tak, že ho nejdříve najde využitím metody "nait_pojostence" a pak ho smaže  
    def smazat_pojistence(self):

        found_pojistenci = self.najit_pojistence()
        if found_pojistenci:
            for pojistenec in found_pojistenci:
                self.cursor.execute(f"DELETE FROM pojistenci WHERE id = {pojistenec[0]}")
            self.conn.commit()
            print("Pojištěnci byli smazáni.")
        else:
            print("Pojištěnci nebyli nalezeni.")

#upraví pojištence ta, že ho nejdříve najde pomocí metody "najit_pojistence" 
    def upravit_pojistence(self):

        found_pojistenci = self.najit_pojistence()
        if found_pojistenci:
            for pojistenec in found_pojistenci:
                nove_jmeno = self.ziskej_text("Zadej nové jméno", povinny_text=True)
                nove_prijmeni = self.ziskej_text("Zadej nové jméno", povinny_text=True)
                novy_vek = self.ziskej_cislo("Zadejte nový věk:\n", povinne_cislo= True)

                self.cursor.execute(f"UPDATE pojistenci SET jmeno = '{nove_jmeno}', prijmeni = '{nove_prijmeni}', vek = {novy_vek} WHERE id = {pojistenec[0]}")
                self.conn.commit()

                print("Pojištěnec byl upraven na:")
                print((pojistenec[0], nove_jmeno, nove_prijmeni, novy_vek))
        else:
            print("Pojištěnci nebyli nalezeni nebo nebyly zadány kritéria pro úpravu.")

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

            volba = input("Zadejte vaši volbu:\t")
            print("XXXXXX")

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