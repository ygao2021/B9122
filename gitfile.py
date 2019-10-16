def EMI(floatrate, N, PV, FV):
    compound = (1 + floatrate)**N
    m = (floatrate * compound) / (compound -1)
    EMI = (PV + (FV/compound)) * m
    return EMI

floatrate = 0.05
N = 40
PV = 20000
FV = 1000

print("Question 1:")
print(EMI(floatrate, N, PV, FV))
