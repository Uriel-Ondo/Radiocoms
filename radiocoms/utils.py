import math

def fsl(f, d):
    return 32.44 + (20 * math.log(f * d) / math.log(10))

def margelibre(pire, fsl1, rxgain, sensi):
    return pire - fsl1 + rxgain - sensi

def rayonfresnel(d1, d2, f):
    return 17.31 * math.sqrt((0.6 * d1 * d2) / ((d1 + d2) * f))

def longueurpylone(altso, ho, r, alt, hbat):
    return altso + ho + r - (alt + hbat)
