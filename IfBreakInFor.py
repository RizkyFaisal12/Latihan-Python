#13 Maret 2026
#program ini difungsikan untuk membuat loop terhadap iterasi yanga da, namun akan berhenti disaat 
#diberikan perintah "break", dan menghentikan loop

# Program 1
for i in range (1, 10):
    print (f"angka yang masuk {i}")
    if i == 7:
        break
print (f"angka ditemukan! = {i}")

#Program 2

keranjang_apel = ("Bagus", "Bagus", "Bagus", "Busuk", "Busuk", "Bagus")

for apel in keranjang_apel:
    if apel == "Busuk":
        break
    print (f"apel ini {apel}")