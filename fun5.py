# stworzyć funkcji kantor
def kantor(waluta):
    def usd(kwota=0):
        print("licze dolary", kwota * 4.03)

    def eur(kwota):
        print("licze euro", kwota * 4.34)

    if waluta == "usd":
        return usd
    elif waluta == "eur":
        return eur
    else:
        return print("Nieznana waluta")


kantor_usd = kantor("usd")
kantor_usd()
kantor_usd(2000)
kantor_usd(1500)
kantor_eur = kantor("eur")
kantor_eur(2000)
kantor_eur(1500)
