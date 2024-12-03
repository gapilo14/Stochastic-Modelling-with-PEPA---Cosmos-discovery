import math

t1FF = 1.14
t1F = 3.0
t1S = 25.73

t1FF *= 2
t1F *= 2
t1S *= 2

T = 3.0
T2 = 1
T3 = 1
T4 = 1
g = 0.5

for i in range(1, 7):
    print('\n')
    print("ROUND ", i)

    w1FF = round(1 - math.exp(-T / t1FF), 4)
    w1F = round(1 - math.exp(-T / t1F), 4)
    w1S = round(1 - math.exp(-T / t1S), 4)

    gammaFF = round(max(1/t1FF, 1/(T + (i-1)*g)), 4)
    gammaF = round(max(1/t1F, 1/(T + (i-1)*g)), 4)
    gammaS = round(max(1/t1S, 1/(T + (i-1)*g)), 4)

    print("w1FF =", w1FF)
    print("gammaFF =", gammaFF)
    print("w1F =", w1F)
    print("gammaF =", gammaF)
    print("w1S =", w1S)
    print("gammaS =", gammaS)

    t2 = 1
    w2 = round(1 - math.exp(-T2 / t2), 4)

    print("w2 =", w2)

    beta = round(max(1/t2, 1/(T2 + (i-1)*g)), 4)
    print("beta =", beta)

    delta = round(1/(T3 + (i-1)*g), 4)
    print("delta =", delta)

    w3 = 0.999
    print("w3 =", w3)

    eta = 1 / T4
    print("eta =", eta)
