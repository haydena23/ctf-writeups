""" void main.checkPassword(int param_1,uint param_2)

{

  byte local_20 [28];

  if ((int)param_2 < 32) {
    os.Exit(0);
  }
  local_40 = 942749240;
  local_3c = 828782131;
  local_38 = 1681089843;
  local_34 = 1681338934;
  local_30 = 926114150;
  local_2c = 1650745909;
  local_28 = 959984440;
  local_24 = 1697919282;
  uVar2 = 0;
  iVar3 = 0;
  while( true ) {
    if (0x1f < (int)uVar2) {
      if (iVar3 == 0x20) {
        return;
      }
      return;
    }
    if ((param_2 <= uVar2) || (31 < uVar2)) break;
    if ((*(byte *)(param_1 + uVar2) ^ *(byte *)((int)&local_40 + uVar2)) == local_20[uVar2]) {
      iVar3 = iVar3 + 1;
    }
    uVar2 = uVar2 + 1;
  } """


def check(param_1,param_2):
    parm1 = param_1
    parm2 = param_2
    uVar2 = 0;
    iVar3 = 0;
    
    while(True):
        if (31 < uVar2):
            if (iVar3 == 32):
                return
            return
        if ((parm2 <= uVar2) or (31 < uVar2)):
            break
        if (((parm1 + uVar2) ^ (942749240 + uVar2)) == local_20[uVar2])
            iVar3 = iVar3 + 1
        uVar2 = uVar2 + 1