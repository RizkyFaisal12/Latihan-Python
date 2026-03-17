#6 Maret 2026
BeratBadan = float(input("Masukkan berat badan = "))
TinggiBadan = float(input("Masukkan tinggi badan = "))

TinggiBadan = TinggiBadan / 100 # pembentukan nilai baru

BMI = BeratBadan/(TinggiBadan*TinggiBadan) #pembentukan variabel baru
print(f"nilai BMI = {BMI}")

if BMI < 18.5: #pengkategorian nilai variabel
 print ('Masuk kategori kurus')
elif 18.5 >= BMI <= 24.9: 
 print ('Masuk kategori kurus')
else :
 print ("Masuk kategori gemuk")