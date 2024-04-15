N, r, c = map(int, input().split())

def z_order(N, r, c):
    if N == 1:
        return r * 2 + c
    
    half_size = 2 ** (N - 1)
    if r < half_size and c < half_size:
        return z_order(N - 1, r, c)
    elif r < half_size and c >= half_size:
        return half_size * half_size + z_order(N - 1, r, c - half_size)
    elif r >= half_size and c < half_size:
        return 2 * half_size * half_size + z_order(N - 1, r - half_size, c)
    else:
        return 3 * half_size * half_size + z_order(N - 1, r - half_size, c - half_size)

print(z_order(N, r, c))