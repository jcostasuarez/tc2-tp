import numpy as np
import scipy.signal as sig
import splane as tc2
import matplotlib.pyplot as plt

# elijo un orden luego de iterar ...
nn = 3
rp = 0.5
q = 5
f0 = 22E3

w0 = 2*np.pi * f0
bw = w0 /q

num, den = sig.cheby1(nn, rp, 1, btype='low', analog=True, output='ba')

print('\n\n')
print('------------------')
print('Particiono en SOSs')
print('------------------')

# particiono en 2 SOS's para la implementación
sos_pa = tc2.tf2sos_analog(num, den)

### la visualizamos de algunas formas, la tradicional
tc2.pretty_print_SOS(sos_pa)

tc2.pretty_print_lti(num, den)

#tc2.analyze_sys(sos_pa)

num, den = sig.lp2bp(num, den, wo=1.0, bw=bw)

print('\n\n')
print('------------------')
print('Particiono en SOSs')
print('------------------')

# particiono en 2 SOS's para la implementación
sos_pa = tc2.tf2sos_analog(num, den)

### la visualizamos de algunas formas, la tradicional
tc2.pretty_print_SOS(sos_pa)

tc2.pretty_print_lti(num, den)

tc2.analyze_sys(sos_pa)