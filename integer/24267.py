n = int(input())

output = n**2*(n-2) - n*(n-2) - n*(n-2)*(n-1)//2
output -= (n**2*(n-2) - n*(n-2) - (n-2)*(n-1)*(2*n-3)//6 - (n-2)*(n-1)//2)//2

print(f"{output}\n3")