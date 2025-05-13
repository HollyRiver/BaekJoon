from sys import stdin

score_dict = {s:(4.5 - 0.5*i) for i, s in enumerate(["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0"])}
score_dict["F"] = 0.0

ss = 0
p = 0

for i in range(20) :
    _, g, s = stdin.readline().rstrip().split(" ")
    
    if s != "P" :
        ss += float(g)*score_dict[s]
        p += float(g)
    
gpa = ss/p

print(gpa)