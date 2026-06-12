baho = int(input("bahoyingizni kiriting: "))

if baho >= 90 and baho <= 100:
    print("A (A'lo)")
elif baho >= 80 and baho <= 89:
    print("B (Yaxshi)")
if baho >= 70 and baho <= 79:
    print("C (Qoniqarli)")
elif baho >= 60 and baho <= 69:
    print("D (Qoniqarsiz)")
elif baho >= 60 and baho <= 0:
    print("F (Yomon)")
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")