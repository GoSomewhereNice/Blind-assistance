from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

def handleDiscovery(self, dev, isNewDev, isNewData):
    if isNewDev:
        print "Discovered device", dev.addr
    elif isNewData:
        print "Received new data from", dev.addr

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(2.0) #time out
myDev = "b8:27:eb:c4:5d:2e"

def distance(rssi):
    iRssi = abs(rssi)
    power = (iRssi-59)/(10*2.0)
    return pow(10,power)

for dev in devices:
    if dev.addr == myDev:
        print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        print "Distance %s m" % (round(distance(dev.rssi),2))
        break
    else:
        print "Searching..."
