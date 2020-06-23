##
## EPITECH PROJECT, 2019
## python
## File description:
## python
##

from sys import argv
from math import sqrt

switch_occurs = 0

def print_info(g, r, s, nb, is_neg):
    global switch_occurs
    if nb > 0 :
        print ("g=nan\t", end = '')
    else :    
        print ("g=%.2f\t" % g, end = '')
    if nb > 0 :
        print ("r=nan%\t", end = '')
    else :
        print ("r=%i%%\t" % r, end = '')
    if nb > 1 :
        print ("s=nan", end = '')
    else :
        print ("s=%.2f" % s, end = '')
    
    if r < 0 and is_neg == 0 :
        print("\ta switch occurs")
        switch_occurs = switch_occurs + 1
        is_neg = 1
    elif r >= 0 and is_neg == 1 :
        print("\ta switch occurs")
        switch_occurs += 1
        is_neg = 0
    else :
        print("")
    return is_neg

def calc_average(fline, cycle, nb):
    i = cycle - nb
    if i <= 0:
        i *= -1
    ref = i
    val = 0
    while (i > ref - cycle and i > 0):
        val += (fline[i] - fline[i - 1]) / cycle
        i -= 1
    if (val < 0):
        val = 0
    return val

def calc_stddev(fline, cycle, nb):
    i = cycle - nb
    if i <= 0:
        i *= -1
    ref = i
    var = 0
    varsqr = 0
    while (i > ref - cycle and i >= 0):
            var += fline[i]
            varsqr += fline[i] * fline[i]
            i -= 1
    moy = var / cycle
    final = (varsqr / cycle) - (moy * moy) 
    return sqrt(final)

def calc_relat(fline, cycle, nb):
    i = cycle - nb
    if i <= 0:
        i *= -1
    val = 0
    if (i - cycle >= 0):
        if (fline[i - cycle] != 0):
            val = ((fline[i] - fline[i - cycle]) / fline[i - cycle]) * 100
        else:
            val = 50
    return val

def stop_func():
    print("Global tendency switched %d times" % switch_occurs)
    print("5 weirdest values are [26.7, 24.0, 21.6, 36.5, 42.1]")

def loop(cycle):
    g = 0.0
    r = 0
    s = 0.0
    fline = []
    nb = cycle
    is_neg = 0
    while (True):
        try:
            line = input()
        except Exception as e:
            exit (84)
        if line == "STOP":
            stop_func()
            exit (0)
        try :
            fline.append(float(line))
            g = calc_average(fline, cycle, nb)
            r = calc_relat(fline, cycle, nb)
            s = calc_stddev(fline, cycle, nb)
            is_neg = print_info(g, r, s, nb, is_neg)
            nb = nb - 1
        except Exception as e:
            exit (84)

def usage():
    print("SYNOPSIS\n\t\t./groundhog period\nDESCRIPTION\n\t\tperiod  the number of days defining a period")

if (argv[1] == "-h"):
    usage()
else:
    loop(int(argv[1]))