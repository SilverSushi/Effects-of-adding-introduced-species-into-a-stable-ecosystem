from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a0 = 700
b0 = 800
c0 = 1200
d0 = 1300
e0 = 400
sp0 = 10


a1, a2 = 0.004, 5e-5
b1, b2 = 0.04, 5e-5
c1, c2 = 0.02, 5e-5
d1, d2 = 0.02, 5e-5
e1 = 0.02
sp1, sp3, sp4, sp5, sp6 = 0.01, 5e-5, 5e-5, 5e-5, 5e-5
k = 1000


def da(a, b):
    return a1 * a * (1 - ((a + a2 * b) / k))


def db(a, b, c, sp):
    return b * (-b1 + (a2 * a) - (b2 * c) - (sp3 * sp))


def dc(b, c, d, sp):
    return c * (-c1 + (b2 * b) - (c2 * d) - (sp4 * sp))


def dd(c, d, e, sp):
    return d * (-d1 + (c2 * c) - (d2 * e) - (sp5 * sp))


def de(d, e):
    return e * (-e1 + (d2 * d))


def dsp(a, b, c, d, sp):
    return sp * (-sp1 + (sp3 * b) + (sp4 * c) + (sp5 * d))


def F(X, t=0):
    return np.array([da(X[0], X[1]), db(X[0], X[1], X[2], X[5]), dc(X[1], X[2], X[3], X[5]), dd(X[2], X[3], X[4], X[5]), de(X[3], X[4]), dsp(X[0], X[1], X[2], X[3], X[5])])


t = np.linspace(0, 8000, 10000)

X = odeint(F, np.array([a0, b0, c0, d0, e0, sp0]), t)

a_population = []
b_population = []
c_population = []
d_population = []
e_population = []
sp_population = []

for a in X:
    a_population.append(a[0])
    b_population.append(a[1])
    c_population.append(a[2])
    d_population.append(a[3])
    e_population.append(a[4])
    sp_population.append(a[5])

a_population = np.array(a_population)
b_population = np.array(b_population)
c_population = np.array(c_population)
d_population = np.array(d_population)
e_population = np.array(e_population)
sp_population = np.array(sp_population)

fig = plt.figure(figsize=(12, 7.4))
ax = fig.add_subplot(1, 1, 1)

ax.plot(t, a_population, label="A Population", linewidth=3, color='green')
ax.plot(t, b_population, label="B Population", linewidth=3, color='red')
ax.plot(t, c_population, label="C Population", linewidth=3, color='blue')
ax.plot(t, d_population, label="D Population", linewidth=3, color='black')
ax.plot(t, e_population, label="E Population", linewidth=3, color='magenta')
ax.plot(t, sp_population, label="SP Population", linewidth=3, color='brown')

ax.legend()
ax.set_xlabel("time")
ax.set_ylabel("Number of Individuals")

plt.show()
