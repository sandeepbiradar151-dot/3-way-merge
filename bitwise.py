a = 12
b = 5

# & bitwiose OR operator returns 1 if atleast one of bits is 1

print(a & b)

# | bitwiose OR operator returns 1 if atleast one of bits is 1

print(a | b)

# ^ bitwiose XOR operator returns 1 if both bits are different

# 12 -> 0 0 0 0 1 1 0 0
# 05 -> 0 0 0 0 0 1 0 1
                 
print(a ^ b)

# ~ bitwiose NOT operator inverts the bits

print(~a)

# << bitwise leftshift operator shifts the bits to left
print(a << 2)

# >> bitwise rightshift operator shifts the bits to right

print(a >> 2)