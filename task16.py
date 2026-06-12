yosh = int(input("yoshingizni kiriting: "))

narx = 100000
chegirma = 0

if yosh >= 0 and yosh <= 6:
    chegirma = 50
elif yosh >= 7 and yosh <= 17:
    chegirma = 20
elif yosh > 60:
    chegirma = 30

yakuniy_narx = narx * (100 - chegirma) / 100

print(f"Yakuniy narx: {int(yakuniy_narx)} so'm ({chegirma}% chegirma qo'llanildi)")