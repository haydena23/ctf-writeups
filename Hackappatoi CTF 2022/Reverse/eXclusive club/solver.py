def signed8bit_to_int(val):
    return (((val >> 7) * 128) ^ val) - ((val >> 7) * 128)

check_vals = [ 
    41,34,53,39,58,36,
    25,34,45,20,116,112,
    55,114,30,113,51,31,
    15,71,53,126,60,
]

# Algorithm
# (i * 4) + (input ^ 0x41) = check_val[i]
# Reverse algorithm
# input = ((check_val[i] - (i * 4)) ^ 0x41)

flag = 'hctf{'
for i in range(len(check_vals)):
    print(signed8bit_to_int((check_vals[i]-(i*4)) ^ 0x41))
print(flag + "}")
