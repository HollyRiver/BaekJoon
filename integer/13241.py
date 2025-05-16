from sys import stdin

A, B = map(int, stdin.readline().split())

ints = [A, B]
ints.sort(reverse = True)

for j in range(2**16) :
    R = ints[0]%ints[1]

    if R == 0 :
        print((A*B)//ints[1])
        break
    else :
        ints = [ints[1], R]