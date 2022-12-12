void * encryption(long param_1,long param_2,int param_3,int param_4)

{
  void *pvVar1;
  int local_30;
  int local_2c;
  
    // param1 = input
    // param2 = flag
    // param3 = 5
    // param4 = 63

    for(int i = 0; i < 63; i + 5) {
        for(int k = 0; k < 5 && (k + i != 63); k + 1) {

        }
    }

  pvVar1 = malloc(63);
  for (local_2c = 0; local_2c < param_4; local_2c = param_3 + local_2c) {
    for (local_30 = 0; (local_30 < param_3 && (local_2c + local_30 != param_4)); local_30 = local_30 + 1) {
        ((long)pvVar1 + (long)(local_2c + local_30)) =
           (param_1 + local_30) ^ (param_2 + (local_2c + local_30));
    }
  }
  return pvVar1;
}