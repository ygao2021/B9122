def EMI(floatrate, N, PV, FV):
    compound = (1 + floatrate)**N
    m = (floatrate * compound) / (compound -1)
    EMI = (PV + (FV/compound)) * m
    return EMI

floatrate = 0.1
N = 30
PV = 10000
FV = 2000

print("Question 1:")
print(EMI(floatrate, N, PV, FV))
