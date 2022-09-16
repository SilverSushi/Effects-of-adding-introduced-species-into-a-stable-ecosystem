from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# x0: initial prey population, y0: initial predator1 population, z0: initial predator2 population, w0: initial predator3 population
x0 = 700
y0 = 800
z0 = 1200
w0 = 1300

alpha = 0.04
beta = 5e-5
gamma = 0.04
delta = 5e-5
epsilon = 5e-5
zeta = 0.01
eta = 5e-5
theta = 5e-5
iota = 0.01
kappa = 5e-5

# dx: x derivarive, dy: y derivative, dz: z derivative, x: prey population, y: predator1 population, z: predator 2 population


def dx(x, y):
    return x * (alpha - (beta * y))


def dy(x, y, z):
    return y * (-gamma + (delta * x) - (epsilon * z))


def dz(y, z, w):
    return z * (-zeta + (eta * y) - (theta * w))


def dw(z, w):
    return w * (-iota + (kappa * z))


def F(X, t=0):
    return np.array([dx(X[0], X[1]), dy(X[0], X[1], X[2]), dz(X[1], X[2], X[3]), dw(X[2], X[3])])


t = np.linspace(0, 2000, 5000)

X = odeint(F, np.array([x0, y0, z0, w0]), t)

prey_population = []
predator1_population = []
predator2_population = []
predator3_population = []

for a in X:
    prey_population.append(a[0])
    predator1_population.append(a[1])
    predator2_population.append(a[2])
    predator3_population.append(a[3])

prey_population = np.array(prey_population)
predator1_population = np.array(predator1_population)
predator2_population = np.array(predator2_population)
predator3_population = np.array(predator3_population)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)

ax.plot(t, prey_population, label="Prey Population", linewidth=3, color='green')
ax.plot(t, predator1_population, label="Predator1 Population",
        linewidth=3, color='red')
ax.plot(t, predator2_population, label="Predator2 Population",
        linewidth=3, color='blue')
ax.plot(t, predator3_population, label="Predator3 Population",
        linewidth=3, color='black')

ax.legend()

ax.set_title(
    "Evolution of predator and prey population over time with linear food chain")
ax.set_xlabel("$t$")
ax.set_ylabel("Number of Individuals")

plt.show()
