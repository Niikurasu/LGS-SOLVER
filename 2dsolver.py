A1 = [4, 3] # [15, 6] ---->  [15, 6]
A2 = [1, -2] # [15, 25] ----> [0, 19] y = 19
B1 = [2]
B2 = [0]

def kgV(zahlen):
    mal = 1
    while True:
        vielfaches = zahlen[0] * mal
        try:
            for zahl in zahlen:
                rest = (vielfaches % zahl)
                if not rest: pass
                else:
                    raise
            break
        except: pass
        mal += 1
    return vielfaches
def solve2d(a1, a2, b1, b2):
	# x werte der gleichung auf die gleiche Zahl bringen
	old_a1 = a1
	a2faktor = kgV([a1[0], a2[0]]) / a2[0]#old_a1[0]
	a1faktor = kgV([a1[0], a2[0]]) / a1[0]
	a1[0] *= a1faktor
	a1[1] *= a1faktor
	b1[0] *= a1faktor
	a2[0] *= a2faktor
	a2[1] *= a2faktor
	b2[0] *= a2faktor
	# Nun sind beide x werte die selben bei beiden gleichungen. Nun kann man die erste Gleichung von der zweiten abziehen
	a2[0] = a2[0] - a1[0]
	a2[1] = a2[1] - a1[1]
	b2[0] = b2[0] - b1[0]
	y = b2[0] / a2[1] # bei der zweiten gleichung ist jetzt nur noch die y variable. Wenn man ihn durch b2 teilt, erhält man y
	# nun kann man y in die erste gleichung einsetzen um x zu erhalten
	gl1y = a1[1]*y
	a1[1] = 0
	b1[0] -= gl1y
	x = b1[0] / a1[0]
	print("X: " + str(x))
	print("Y: " + str(y))
solve2d(A1, A2, B1, B2)
