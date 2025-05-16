from sys import stdin

N = int(stdin.readline().rstrip())
Xs = list(map(int, stdin.readline().split()))

Xss = sorted(list(set(Xs)))

mapping_dict = {s:i for i, s in enumerate(Xss)}

print(" ".join([str(mapping_dict[s]) for s in Xs]))