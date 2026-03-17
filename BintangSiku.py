#13 Maret 2026

#Program ini menjalankan perhitungan logika unutuk membangun sebuah output segitiga siki siku.

for i in range (1,6):#tinggi segitiga mulai dari i=1, sampai i=5
    print ( ) #ini akanmengosongkan bagian paling atas, jika tidak prcya masukkan nila 1
    for a in range (1, i+1): # logika yang berjalan, dari iterasi =1, meuju iterasi i+1 yang artinya padas etiap baris, bintang dapat bertambah karena bintang per abris, linear dengan iterasi i
        print ("*", end ="") # end disini berfungsi unutk meluruskan bintang, kalo tidak setiapb aris bintangnya akan kebawah