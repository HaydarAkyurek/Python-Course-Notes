numbers = [1,4,7,15,34,56,79]
result = []

for sayi in numbers:
    if(sayi % 2 == 0):
        result.append(sayi)

result = [sayi for sayi in numbers if sayi % 2 == 0]
result = [sayi if sayi % 2 == 0 else "tek sayı" for sayi in numbers]

products = [4500,1000,0, 15350,0,4421]
tax = []

for fee in products:
    if(fee > 0):
        tax.append(fee * 1.35)

tax = [fee * 1.35 for fee in products if fee > 0]
tax = [fee if fee > 0 else "vergi çıkmadı" for fee in products]

print(tax)
