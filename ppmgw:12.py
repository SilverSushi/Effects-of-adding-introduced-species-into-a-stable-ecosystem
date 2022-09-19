from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# h0 = humans, mm0 = marine mammals, f0 = fish, br0 = birds, ce0 = cephalopods, cr0 = crustaceans
# g0 = gastropods, e0 = echinoderms, bv0 = bivalves, d0 = dinoflagellates, mb0 = marine bacteria, ma0 = macroalgae

h0 = 100
mm0 = 100
br0 = 100
f0 = 400
ce0 = 200
bv0 = 700
cr0 = 300
g0 = 400
e0 = 100
d0 = 100
mb0 = 500
ma0 = 300

h1, h2, h3, h4, h5, h6 = 0.04, 5e-5, 4e-5, 3e-5, 2e-5, 4e-5
mm1, mm2 = 0.004, 5e-5
br1, br2, br3 = 0.04, 5e-5, 9e-5
f1, f2, f3, f4, f5 = 0.04, 9e-5, 9e-5, 9e-5, 1e-5
ce1, ce2, ce3, ce4, ce5 = 0.04, 5e-5, 5e-5, 5e-5, 5e-5
bv1, bv2, bv3, bv4, bv5, bv6, bv7, bv8 = 0.04, 5e-5, 9e-5, 6e-5, 5e-5, 3e-5, 5e-5, 9e-5
cr1, cr2, cr3, cr4, cr5 = 0.04, 5e-5, 5e-5, 5e-5, 5e-5
g1, g2, g3, g4, g5, g6 = 0.04, 8e-5, 5e-5, 6e-5, 7e-5, 5e-5
e1, e2, e3 = 0.04, 5e-5, 9e-5
d1, d2, d3 = 0.03, 9e-5, 1e-5
mb1, mb2, mb3, mb4, mb5 = 0.07, 5e-5, 5e-5, 5e-5, 5e-5
ma1, ma2, ma3, ma4 = 0.06, 9e-5, 5e-5, 5e-5


def dh(h, f, ce, bv, cr, g):
    return h * (-h1 + (h2 * bv) + (h3 * cr) + (h4 * g) + (h5 * f) + (h6 * ce))


def dmm(mm, f):
    return mm * (-mm1 + (mm2 * f))


def dbr(br, f, bv):
    return br * (-br1 + (br2 * f) + (br3 * bv))


def df(h, mm, br, f, bv):
    return f * (-f1 + (f2 * bv) - (f3 * br) - (f4 * mm) - (f5 * h))


def dce(h, ce, bv, cr, g):
    return ce * (-ce1 + (ce2 * cr) + (ce3 * bv) + (ce4 * g) - (ce5 * h))


def dbv(h, br, f, ce, bv, g, e, d):
    return bv * (-bv1 + (bv2 * d) - (bv3 * br) - (bv4 * h) - (bv5 * f) - (bv6 * ce) - (bv7 * g) - (bv8 * e))


def dcr(h, ce, cr, mb, ma):
    return cr * (-cr1 + (cr2 * mb) + (cr3 * ma) - (cr4 * h) - (cr5 * ce))


def dg(ce, bv, g, e, mb, ma):
    return g * (-g1 + (g2 * mb) + (g3 * ma) + (g4 * bv) - (g5 * ce) - (g6 * e))


def de(bv, g, e):
    return e * (-e1 + (e2 * g) + (e3 * bv))


def dd(bv, d, ma):
    return d * (-d1 + (d2 * ma) - (d3 * bv))


def dmb(cr, g, d, mb, ma):
    return mb * (mb1 - (mb2 * d) - (mb3 * ma) - (mb4 * cr) - (mb5 * g))


def dma(cr, g, mb, ma):
    return ma * (-ma1 + (ma2 * mb) - (ma3 * cr) - (ma4 * g))


def F(X, t=0):
    return np.array([dh(X[0], X[3], X[4], X[5], X[6], X[7]), dmm(X[1], X[3]), dbr(X[2], X[3], X[5]), df(X[0], X[1], X[2], X[3], X[5]),
                     dce(X[0], X[4], X[5], X[6], X[7]), dbv(X[0], X[2], X[3], X[4],
                                                            X[5], X[7], X[8], X[9]), dcr(X[0], X[4], X[6], X[10], X[11]),
                     dg(X[4], X[5], X[7], X[8], X[10], X[11]), de(
                         X[5], X[7], X[8]), dd(X[5], X[9], X[11]),
                     dmb(X[6], X[7], X[9], X[10], X[11]), dma(X[6], X[7], X[10], X[11])])


t = np.linspace(0, 1000, 1000)

X = odeint(F, np.array(
    [h0, mm0, br0, f0, ce0, bv0, cr0, g0, e0, d0, mb0, ma0]), t)


h_pop = []
mm_pop = []
br_pop = []
f_pop = []
ce_pop = []
bv_pop = []
cr_pop = []
g_pop = []
e_pop = []
d_pop = []
mb_pop = []
ma_pop = []

for a in X:
    h_pop.append(a[0])
    mm_pop.append(a[1])
    br_pop.append(a[2])
    f_pop.append(a[3])
    ce_pop.append(a[4])
    bv_pop.append(a[5])
    cr_pop.append(a[6])
    g_pop.append(a[7])
    e_pop.append(a[8])
    d_pop.append(a[9])
    mb_pop.append(a[10])
    ma_pop.append(a[11])

h_pop = np.array(h_pop)
mm_pop = np.array(mm_pop)
br_pop = np.array(br_pop)
f_pop = np.array(f_pop)
ce_pop = np.array(ce_pop)
bv_pop = np.array(bv_pop)
cr_pop = np.array(cr_pop)
g_pop = np.array(g_pop)
e_pop = np.array(e_pop)
d_pop = np.array(d_pop)
mb_pop = np.array(mb_pop)
ma_pop = np.array(ma_pop)

fig = plt.figure(figsize=(8, 8))

asp = fig.add_subplot(1, 1, 1)

asp.plot(t, h_pop, label="Human Population",
         linewidth=3, color='Red')
asp.plot(t, mm_pop, label="Marine Mammal Population",
         linewidth=3, color='orange')
asp.plot(t, br_pop, label="Bird Population",
         linewidth=3, color='Yellow')
asp.plot(t, f_pop, label="Fish Population",
         linewidth=3, color='Green')
asp.plot(t, ce_pop, label="Cephalopods Population",
         linewidth=3, color='Blue')
asp.plot(t, bv_pop, label="Bivalves Population",
         linewidth=3, color='Indigo')
asp.plot(t, cr_pop, label="Crustaceans Population",
         linewidth=3, color='Purple')
asp.plot(t, g_pop, label="Gastropods Population",
         linewidth=3, color='Black')
asp.plot(t, e_pop, label="Echinoderms Population",
         linewidth=3, color='Grey')
asp.plot(t, d_pop, label="Dinoflagellates Population",
         linewidth=3, color='Pink')
asp.plot(t, mb_pop, label="Marine Bacteria Population",
         linewidth=3, color='Magenta')
asp.plot(t, ma_pop, label="Macroalgae Population",
         linewidth=3, color='Cyan')

asp.legend()

asp.set_title(
    "Evolution of predator and prey population over time with generalized food chain")
asp.set_xlabel("$t$")
asp.set_ylabel("Number of Individuals")

plt.show()
