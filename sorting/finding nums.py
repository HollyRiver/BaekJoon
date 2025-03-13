## N개의 정수가 주어져 있을 때, X라는 정수가 이 안에 존재하는지 알아내는 프로그램

from sys import stdin

N = int(stdin.readline().rstrip())
integer_lst = set(map(int, stdin.readline().split()))

M = int(stdin.readline().rstrip())
finding_lst = list(map(int, stdin.readline().split()))

for f in finding_lst :
    if f in integer_lst :
        print(1)
    else :
        print(0)