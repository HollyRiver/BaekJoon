temp = input()
x = input().split()
value = input()

print(sum([i == value for i in x]))