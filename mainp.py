from databaze import Databaze

def main():

    moje_databaze = Databaze(db_name="pojistenci.db")
    moje_databaze.startuj()

if __name__ == "__main__":
    main()