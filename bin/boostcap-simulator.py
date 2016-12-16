#! /usr/bin/env python
# Source: http://kmkeen.com/boostcap/

from math import expm1

cap = 3000.0  # farads
watt = 7.0  # watts of device
vstart = 2.5  # capacitor Vmax
vstop = 1.2  # regulator Vmin
effi = .80  # regulator efficiency

assert vstart > vstop
v = vstart
t = 0
delta_t = 0.1  # seconds

while v > vstop:
    r = v**2 * effi / watt
    rc = cap * r
    v += v * expm1(-delta_t / rc)
    t += delta_t

print(int(round(t)), 'seconds')
