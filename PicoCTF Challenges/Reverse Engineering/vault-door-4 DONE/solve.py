myBytes = [
    106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
    85, 110, 67, 104, 95, 48, 102, 95,
    98, 89, 116, 51 , 115, 95, 56 , 102,
    '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
    ]
flag = ""
for val in myBytes:
    if isinstance(val, str):
        flag += val
    else:
        flag += chr(val)

print(flag)