from math import log

k1 = 1.2
k2 = 100
b = 0.75
R = 0.0

def bm25_score(n, f, qf, r, N, dl, avdl):
	K = k1 * ((1-b) + b * (float(dl)/float(avdl)))
	first = log( ( (r + 0.5) / (R - r + 0.5) ) / ( (n - r + 0.5) / (N - n - R + r + 0.5)) )
	second = ((k1 + 1) * f) / (K + f)
	third = ((k2+1) * qf) / (k2 + qf)  # =1 (qf=1)
	return first * second * third
