string = [*"jU5t_a_sna_3lpm18g947_u_4_m9r54f"]
indexLoop1 = [0,1,2,3,4,5,6,7]
indexLoop2 = [8,9,10,11,12,13,14,15]
indexLoop3 = [16,18,20,22,24,26,28,30]
indexLoop4 = [31,29,27,25,23,21,19,17]

val = [''] * 32

for i in indexLoop1:
    val[i] += string[i]
for i in indexLoop2:
    val[i] += string[23-i]
for i in indexLoop3:
    val[i] += string[46-i]
for i in indexLoop4:
    val[i] += string[i]

flag = ''.join(val)
print('picoCTF{' + flag + '}')