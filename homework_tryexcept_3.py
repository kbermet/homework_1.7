spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]

for i in range(12):
    try:
        coeff = []
        coeff = spendings[i]/income[i]
        print(coeff)
    except ZeroDivisionError:
        print(0)
        continue
print (sum(coeff)/12)
