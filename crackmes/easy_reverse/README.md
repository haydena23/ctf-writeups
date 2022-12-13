# easy_reverse

## Problem Description
[rev50_linux64-bit](rev50_linux64-bit)

Author: cbm-hackers

Language: C/C++

Platform: Unix/linux etc.

Difficulty: 1.4

Quality: 4.7

Arch: x86-64

"an easy crackme"

## Solutions
After Ghidra analysis, we can see that the program is quite simple. By adjusting the function signature, and renaming some variables, it becomes quite clear. The program checks the user input is of length 10, and the 5th spot of the input is an @ char. 

<table>
<tr>
<th> Decompiled </th>
<th> Readable </th>
</tr>
<tr>
<td>

```C
undefined8 main(int param_1,undefined8 *param_2)

{
  size_t sVar1;
  
  if (param_1 == 2) {
    sVar1 = strlen((char *)param_2[1]);
    if (sVar1 == 10) {
      if (*(char *)(param_2[1] + 4) == '@') {
        puts("Nice Job!!");
        printf("flag{%s}\n",(char *)param_2[1]);
      }
      else {
        usage(*param_2);
      }
    }
    else {
      usage(*param_2);
    }
  }
  else {
    usage(*param_2);
  }
  return 0;
}
```

</td>
<td>

```C
int main(int argc,char **argv)

{
  size_t length_of_input;
  
  if (argc == 2) {
    length_of_input = strlen(argv[1]);
    if (length_of_input == 10) {
      if (argv[1][4] == '@') {
        puts("Nice Job!!");
        printf("flag{%s}\n",argv[1]);
      }
      else {
        usage(*argv);
      }
    }
    else {
      usage(*argv);
    }
  }
  else {
    usage(*argv);
  }
  return 0;
}
```

</td>
</tr>
</table>

## Flag
flag{aaaa@aaaaa}