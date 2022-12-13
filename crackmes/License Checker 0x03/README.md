# license_checker_3

## Problem Description
[license_checker_3](license_checker_3)

Author: NomanProdhan

Language: C/C++

Platform: Unix/linux etc.

Difficulty: 1.8

Quality: 4.0

Arch: x86-64

"This binary is for beginners to practice reversing. Don't patch the binary, try to create a keygen to solve it."

## Process
After Ghidra analysis, we can see that the program has a main function. Immedietely, the while(true) loop looks of interest. By Renaming some variables, the function of it becomes very clear. An input that when each char is added up, it totals 50.

<table>
<tr>
<th> Decompiled </th>
<th> Readable </th>
</tr>
<tr>
<td>

```C
void main(int param_1,undefined8 *param_2)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  char local_19;
  int local_18;
  int local_14;
  undefined8 local_10;
  
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  if (param_1 != 2) {
    printf("Usage : %s <license pass code here [numbers only]>\n",*param_2);
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  local_18 = 0;
  local_14 = 0;
  while( true ) {
    sVar2 = strlen((char *)param_2[1]);
    if ((int)sVar2 <= local_14) break;
    local_19 = *(char *)((long)local_14 + param_2[1]);
    iVar1 = atoi(&local_19);
    local_18 = local_18 + iVar1;
    local_14 = local_14 + 1;
  }
  if (local_18 == 0x32) {
    puts("Premium access has been activated !");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("Wrong license code");
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```

</td>
<td>

```C
int main(int argc,char **argv)

{
  int int_val_of_letter;
  size_t input_length;
  long in_FS_OFFSET;
  char letter;
  int sum;
  int i;
  undefined8 local_10;
  
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  if (argc != 2) {
    printf("Usage : %s <license pass code here [numbers only]>\n",*argv);
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  sum = 0;
  i = 0;
  while( true ) {
    input_length = strlen(argv[1]);
    if ((int)input_length <= i) break;
    letter = argv[1][i];
    int_val_of_letter = atoi(&letter);
    sum = sum + int_val_of_letter;
    i = i + 1;
  }
  if (sum == 50) {
    puts("Premium access has been activated !");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("Wrong license code");
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```

</td>
</tr>
</table>

## Flag
flag{5555555555}