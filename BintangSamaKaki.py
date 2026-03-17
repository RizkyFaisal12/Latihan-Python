#14 Maret 2026

tinggi = 20
totalbintang = 0

#logika perhitungan membuat segitiga siku siku
for i in range (1, tinggi+1): #pakai +1 agar jumlah i sampai 20, karena python membaca <
    spasi = " " *(tinggi-i) #membuat polas egitiga dari kiri menggunakan spasi yang berkurang
    bintang = "*" * ((2*i)-1)#membuat bintangnya dengan pola bertambah dengan pola matematis
    print (spasi+bintang)#menggabungkan keduanya, diletakan didalam for karena agar terbentuk segitiga

#logika menghitung jumlah bintang yang keluar
for j in range (1, tinggi+1): ##pakai +1 agar jumlah j sampai 20, karena python membaca <
    bintang = ((2*j)-1) # karena diatas pake *, kita tidak menggunakan, karena anggapannya dia 1. kita hanya menghitung jumlahnya saja, bukan mengeluarkan *
    totalbintang += bintang #penambahan varavel, untuk mempermudah pembacaan. disimpan didalam for akrena agar bertambah setiap looping
    
print (f"jumlah bintang = {totalbintang}")#hasil yang diambil dari perhitungan didalam loop dari j=1 - j=20
