print("""
***************
Puan Hesaplama
***************
""")

vize1 = float(input("Birinci Vize Notunuzu Giriniz:"))
vize2 = float(input("İkinci Vize Notunuzu Giriniz:"))
final = float(input("Final Notunuzu Giriniz:"))
toplam = (vize1 * (30/100) + vize2 * (30/100) + final * (40/100))

print("Notunuz:", toplam)

if toplam >= 90:
    print("Tebrikler! Notunuz: AA")
elif toplam >= 85:
    print("Tebrikler! Notunuz: BA")
elif toplam >= 80:
    print("Tebrikler! Notunuz: BB")
elif toplam >= 75:
    print("Tebrikler! Notunuz: CB")
elif toplam >= 70:
    print("Tebrikler! Notunuz: CC")
elif toplam >= 65:
    print("Tebrikler! Notunuz: DC")
elif toplam >= 60:
    print("Tebrikler! Notunuz: DD")
elif toplam >= 55:
    print("Tebrikler! Notunuz: FD")
else:
    print("Notunuz: FF")


print("""
Aşağıda Puan Sistemi Verilmiştir:

    Vize1 toplam notun %30'una etki eder.
    Vize2 toplam notun %30'una etki eder.
    Final toplam notun %40'ına etki eder.
""")