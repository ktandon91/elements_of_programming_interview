def count_bits(n):
    num_bits = 0
    while n:
        num_bits += n&1 # and operation on least signification bit
        n = n >> 1 ## right shifting resigning the new number to n
    return num_bits

print(count_bits(12))

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def all_operations(x=6,y=4):
    print(x&y)
    print(x|y)
    print(-16 >> 2) # shift right by 2 places and keeping negative sign as it is and fill most significant bit with 0
    print(bin(-16))
    print(bin(16))
    print(16 >> 1)
    print(16 << 1) ## shift left by 1 and fill least significant bit by 0
    print(x^y) #XOR
    print((x|y)-(x&y))
    print(~8) ## returns negative of number + 1 (binary addition)
    print(~-9) ### returns positive of number - 1 (binary subtraction)
    print(bin(~-4))
    print(~-4)

all_operations()