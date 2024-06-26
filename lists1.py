spendigs = [32.45, 18.65, 23.45, 78.32, 5.23]

sum = 0.0
for spending in spendigs:
    sum += spending
print('Money spent:', sum)

spendigs.sort(reverse = True)
print(spendigs)