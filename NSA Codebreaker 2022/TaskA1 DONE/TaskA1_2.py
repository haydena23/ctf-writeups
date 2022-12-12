class Employee:
    def __init__(self, username, logs):
        self.username = username
        self.logs = logs
        
    def showLogs(self):
        for log in self.logs:
            print(log)

def grabNames(logs):
    names = []
    for entry in logs:
        names.append(entry[1])
    names = sorted([*set(names)])
    return names

def main():
    # Open log file
    f = open("vpn.log","r")
    # Add each line to a list
    fullLog = []
    for line in f:
        fullLog.append(line)
    # Close log file
    f.close()
    # Remove the log headers
    fullLog.pop(0)
    # Sort the log based on names since names=entries[1]
    fullLog.sort()
    
    # Split log into individual entries
    entries = []
    for entry in fullLog:
        entries.append(entry.split(','))

    # Grab all employee names
    #enmployeeNames = grabNames(entries)
    
    #for name in enmployeeNames:
        #print(name)
        
    for i in entries:
        if "Aaron.O" in i[1]:
            print(i)
        
main()