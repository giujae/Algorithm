import sys
from itertools import combinations

dwarfs = [int(sys.stdin.readline()) for _ in range(9)]

false_dwarfs = [list(d) for d in combinations(dwarfs, 2)]

found = 0

for f_d in false_dwarfs:
    if not found:
        if (sum(dwarfs) - sum(f_d)) == 100:
            for d in sorted(dwarfs):
                if d not in f_d:
                    print(d)
            found = 1
