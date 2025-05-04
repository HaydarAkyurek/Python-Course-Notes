sayilar = []

for i in range(10):
    sayilar.append(i * 3)

print(sayilar)

sayilar_2 = [i * 3 for i in range(10)]

print(sayilar_2)

person = "Haydar Akyurek"

for i in person:
    print(i.upper())

sonuc = [i.upper() for i in person]
print(sonuc)
