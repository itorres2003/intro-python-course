f = open("intro_4_2_2_baseball.txt")
baseball = []
for line in f:
    line = line.strip()
    column = line.split()
    column[0] = int(column[0])
    column[1] = int(column[1])
    baseball.append(column)
f.close()
