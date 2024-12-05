import math

t1FF = 1.14
t1F = 3.0
t1S = 25.73

t2 = 2

t1FF *= 2
t1F *= 2
t1S *= 2

print("t1FF =", t1FF)
print("t1F =", t1F)
print("t1S =", t1S)

T = 3.0
T2 = 1
T3 = 1
T4 = 1
g = 0.5

T *= 2
T2 *= 2
T3 *= 2
T4 *= 2

w1FF = round(1 - math.exp(-T / t1FF), 4)
w1F = round(1 - math.exp(-T / t1F), 4)
w1S = round(1 - math.exp(-T / t1S), 4)

print("w1FF =", w1FF)
print("w1F =", w1F)
print("w1S =", w1S)

w2 = round(1 - math.exp(-T2 / t2), 4)
print("w2 =", w2)

w3 = 0.999
print("w3 =", w3)

print("------------------------------------")

eta = 1 / T4
print("eta =", eta)
