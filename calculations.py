import math

t1FF = 1.14
t1F = 3.0
t1S = 25.73

T = 3.0

w1FF = round(1 - math.exp(-T / t1FF), 4)
w1F = round(1 - math.exp(-T / t1F), 4)
w1S = round(1 - math.exp(-T / t1S), 4)

print("w1FF = ", w1FF)
print("w1F = ", w1F)
print("w1S = ", w1S)
# print("lol: ", 1/t1S)

# newT = T
# for i in range(1, 10):
#     print(1/newT)
#     newT = newT + 0.5

T2 = 1
t2 = 1
w2 = round(1 - math.exp(-T2 / t2), 4)

print("w2 = ", w2)

beta = 1 / T2
print("beta = ", beta)

T3 = 1
delta = 1 / T3
print("delta = ", delta)

T4 = 1
eta = 1 / T4
print("eta = ", eta)
