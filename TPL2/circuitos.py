# -*- coding: utf-8 -*-
"""Circuitos módulo.

Este módulo fue creado para funciónes auxiliares de la materia circuitos 2.

juancost97@gmail.com
"""

import numpy as np
import scipy.signal as signal
from math import pi

def dibujar_plantilla_bp(ax,wc,ws,a_c,a_s,a_b):
    
    xmin, xmax, ymin, ymax = ax.axis()

    w_min = 0
    w_max = ws[1]*100
    t_max_b = -a_b
    t_min_c = -a_c
    t_max_s = -a_s
    t_min_plantilla = t_max_s-10
    t_max_plantilla = t_max_b+10
    ax.fill([ w_min  , w_min   , ws[0] , ws[0] ], [t_min_plantilla, t_max_s, t_max_s, t_min_plantilla]  ,  alpha=0.2, color="green") # stop
    ax.fill([ wc[0]  , wc[0]   ,  wc[1]   ,  wc[1]   ], [t_max_b,         t_min_c, t_min_c, t_max_b]          ,  alpha=0.2, color="green") # pass
    ax.fill([ ws[1]  , ws[1]   , w_max , w_max ], [t_min_plantilla, t_max_s, t_max_s, t_min_plantilla]  ,  alpha=0.2, color="green") # stop

    ax.axhline(t_max_b, color ='red',ls = '--')
    ax.axhline(t_min_c, color ='red',ls = '--') 
    ax.axhline(t_max_s, color ='red',ls = '--')
    
    ax.set_ylim(bottom=ymin,top=ymax)
    ax.set_xlim(left=xmin,right=xmax)
    
    return()


def dibujar_plantilla_lp(ax,wc,ws,a_s,a_c):
    
    xmin, xmax, ymin, ymax = ax.axis()
    
    # generate sample
    w_min = xmin
    w_max = xmax*10
    t_max_c = -a_c
    t_min_c = xmin
    t_max_s = -a_s
    t_min_plantilla = ymin-10
    t_max_plantilla = ymax+10
    ax.fill([w_min, w_min,  wc  ,  wc ], [t_max_c,t_min_c, t_min_c, t_max_c], alpha=0.2, color="green") # pass
    ax.fill([ws   , ws   , w_max,w_max], [t_min_plantilla, t_max_s, t_max_s, t_min_plantilla],  alpha=0.2, color="green")
    # stop

    ax.set_ylim(bottom=ymin,top=ymax)
    ax.set_xlim(left=xmin,right=xmax)

    return()


def dibujar_bode(ax,num,den):
    w, h = signal.freqs(num,den)
    h_db = 20 * np.log10(abs(h))
    ax.semilogx(w,h_db)    
    return()

def trans_pb_mod(W, W0,Q, K):
    return np.abs((1j* W *K * W0/Q)/((1j*W)**2 + (1j*W) * W0/Q + W0**2))

def trans_pb_arg(W, W0,Q, K):
    return np.angle((1j* W *K * W0/Q)/((1j*W)**2 + (1j*W) * W0/Q + W0**2))-pi

def mod_trans_pb(x,y, popt):
    return np.abs(((y*1j + x)*popt[2]* popt[0]/popt[1])/((y*1j + x)**2 + (y*1j + x) * popt[0]/popt[1]+  popt[0]**2))

def arg_trans_pb(x,y, popt):
    return np.angle(((y*1j + x)*popt[2]* popt[0]/popt[1])/((y*1j + x)**2 + (y*1j + x) * popt[0]/popt[1]+  popt[0]**2))-pi
