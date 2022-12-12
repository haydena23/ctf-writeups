fileInput = open("vpn.log", "r")

logins = []
for line in fileInput:
    logins.append(line.split(','))
fileInput.close()

userNames = []
startTimes = []
duration = []
active = []
auth = []   
realIP = []
vpnIP = []
proto = []
port = []
bytesTotal = []
error = []

for entry in logins:
    userNames.append(entry[1])
    startTimes.append(entry[2])
    duration.append(entry[3])
    active.append(entry[5])
    auth.append(entry[6])
    realIP.append(entry[7])
    vpnIP.append(entry[8])
    proto.append(entry[9])
    port.append(entry[10])
    bytesTotal.append(entry[11])
    error.append(entry[12])
    
res = [*set(userNames)]
print(res)
    
searchInput = input("Name: ")
print("0: All\n1: Username\n2: Start Time\n3: Duration\n4: Service\n5: Active\n6: Auth\n7: Real IP\n8: VPN IP\n9: Proto\n10: Port\n11: Bytes Total\n12: Error")
choice = input("What data would you like: ")
indexes = choice.split(" ")

found = False

for entry in logins:
    if(searchInput in entry[1]):
        joinedString = []
        for index in indexes:
            joinedString.append(entry[int(index)])
        print(joinedString)       
        found = True
        
if(found is False):
    print("No entry found with that name")