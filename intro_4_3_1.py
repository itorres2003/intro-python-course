import numpy as np
f = open("intro_4_2_3_baseball.txt")
baseball = []
for line in f:
    line = line.strip()
    column = line.split()
    column[0] = float(column[0])
    column[1] = float(column[1])
    column[2] = float(column[2])
    baseball.append(column)
f.close()
np_baseball = np.array(baseball)
