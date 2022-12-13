chars = '0123456789abcdefghijklmnopqrstuvwxyzCTF_{}'
char_list = []
starting_hex = 0x2102
for letter in chars:
    temp = (hex(starting_hex), letter)
    char_list.append(temp)
    starting_hex += 0x34

function_calls = [
  "2616",
  "24aa",
  "2372",
  "25e2",
  "2852",
  "2886",
  "28ba",
  "2922",
  "23a6",
  "2136",
  "2206",
  "230a",
  "2206",
  "257a",
  "28ee",
  "240e",
  "26e6",
  "2782",
  "28ee",
  "226e",
  "2136",
  "226e",
  "233e",
  "23da",
  "230a",
  "21d2",
  "2956"
]

flag = ""

for call in function_calls:
    for tup in char_list:
        if call in tup[0]:
            flag += tup[1]

print(flag)