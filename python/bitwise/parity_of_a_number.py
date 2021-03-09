def parity(n):
    result = 0
    while n:
        result ^= n & 1
        n >>= 1
        print(result)
    return result

parity(5)

