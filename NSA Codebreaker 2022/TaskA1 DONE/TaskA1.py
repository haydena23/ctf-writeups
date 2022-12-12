from os import remove
from datetime import datetime, timedelta, timezone
from time import strftime
from dateutil.parser import parse

def readLog(inputFile):
    entries = []
    for entry in inputFile:
        entries.append(entry)
    entries.pop(0)
    return entries

def removeUseless(listOfEntries):
    splitEntries = []
    for entry in listOfEntries:
        splitEntries.append(entry.split(','))
    
    for x in splitEntries:
        x.remove('openvpn-server')
        x.remove('VPN')
        x.remove('UDP')
        x.remove('1194')
        x.pop(3)
        
    splitEntries.sort()
    for l in splitEntries:
        date = parse(l[1])
        if l[2] == '':
            l[2] = 0
            l[5] = 0
            l[6] = 0
        end_time = date + timedelta(seconds=int(l[2]))
        if(l[2] != 0):
            bytes_per_hour = int(l[6])/int(l[2])
            l[3] = humanbytes(bytes_per_hour)
            
        l[2] = end_time.strftime("%Y.%m.%d %H:%M:%S")
        l[6] = humanbytes(l[6])      
        print(l)
        
        
def humanbytes(B):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)
    
f = open("vpn.log","r")
splitData = readLog(f)
removeUseless(splitData)
f.close()
