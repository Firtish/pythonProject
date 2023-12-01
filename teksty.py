tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
tekst.upper()
print(tekst)  # Witaj świecie
tekst2 = tekst.upper()
print(tekst2)  # WITAJ ŚWIECIE
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # WITAJ ŚWIECIE

tekst3 = tekst.lower()
print(tekst3)  # witaj świecie

print(tekst.removesuffix("świecie"))  # "Witaj"
print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst)

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # "b'Witaj \xc5\x9bwiecie'"
print(type(encoded_s))  # "<class 'bytes'>"
# \x - dane w systemie szesnastkowym
print(encoded_s.decode('utf-8'))  # "Witaj świecie"

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 3))  # 0,  1,2,3 = 5,6,7,8 z prawej zbior otwarty
print(tekst.count("i", 5, 9))  # 0,  1,2,3 = 5,6,7,8 z prawej zbior otwarty
print(tekst.count("j", 0, 4))  # 0,  1,2,3 = 5,6,7,8 z prawej zbior otwarty

imie = "Adek"
tekst_format = f"Mam na imię {imie} i lubie pythona."
print(tekst_format)
# f - string - string sformatowanie
tekst_format2 = (f"\tam na imię {imie}\n i lubie pythona.\b"
                 f" Dodatkowe zdanie")
print(tekst_format2)
# \t tabulator
# \n znak nowej linii
# \b backspace

starszy = "Witaj %s!"
print(starszy % imie)

print ("Witaj {}!".format(imie))

print("""
tekst
      wielolinijkowy
      """)
# tekst
#       wielolinijkowy
