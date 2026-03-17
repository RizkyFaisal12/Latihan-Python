#13 Maret 2026

#Program ini dibuat untuk mengeluarkan for each loop, dengan sayarat if(kondisi) jika mengandung kata "busuk" maka akan di continue (di lanjutkan), meuju kata selain busuk
keranjang_apel = ("Bagus", "Bagus", "Bagus", "Busuk", "Busuk", "Bagus")

for apel in keranjang_apel:
    if apel == "Busuk":
        continue
    print (f"apel ini {apel}")
    