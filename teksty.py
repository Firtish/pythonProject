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

