import fractions

A1 = [55, 34, 2231] # 55x + 34y = 2231
A2 = [43, -212, -2321] # 43x + (-212y) = -2321


def kgV(a, b): return abs(a*b) / fractions.gcd(a, b) if a and b else 0

def solve2d(a1, a2):
	# x werte der gleichung auf die gleiche Zahl bringen
	old_a1 = a1
	a2faktor = kgV(a1[0], a2[0]) / a2[0]#old_a1[0]
	a1faktor = kgV(a1[0], a2[0]) / a1[0]
	a1[0] *= a1faktor
	a1[1] *= a1faktor
	a1[2] *= a1faktor
	a2[0] *= a2faktor
	a2[1] *= a2faktor
	a2[2] *= a2faktor
	# Nun sind beide x werte die selben bei beiden gleichungen. Nun kann man die erste Gleichung von der zweiten abziehen
	a2[0] = a2[0] - a1[0]
	a2[1] = a2[1] - a1[1]
	a2[2] = a2[2] - a1[2]
	y = a2[2] / a2[1] # bei der zweiten gleichung ist jetzt nur noch die y variable. Wenn man ihn durch b2 teilt, erhält man y
	# nun kann man y in die erste gleichung einsetzen um x zu erhalten
	gl1y = a1[1]*y
	a1[1] = 0
	a1[2] -= gl1y
	x = a1[2] / a1[0]
	print("X: " + str(x))
	print("Y: " + str(y))
solve2d(A1, A2)
