f = open("intro_4_3_2_positions.txt")
positions = []
for line in f:
    line = line.strip()
    positions.append(line)
f.close()
f = open("intro_4_3_2_heights.txt")
heights = []
for line in f:
    line = line.strip()
    heights.append(int(line))
f.close()