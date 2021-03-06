from bluepy.btle import Scanner, DefaultDelegate
import os


print "Searching..."

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

def handleDiscovery(self, dev, isNewDev, isNewData):
    if isNewDev:
        print "Discovered device", dev.addr
    elif isNewData:
        print "Received new data from", dev.addr

def distance(rssi):
    iRssi = abs(rssi)
    power = (iRssi-59)/(10*2.0)
    return pow(10,power)

while True:
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(2.0) #time out
    myDev = "b8:27:eb:c4:5d:2e"

    for dev in devices:
        if dev.addr == myDev:
            print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
            print "Distance %s m" % (round(distance(dev.rssi),2))
            dis = round(distance(dev.rssi),2)
            if dis<1:
                os.popen('./stopRecBee.sh detect_ed.py')
                os.popen('./stopRecBee.sh button.py')
                os.popen('./remoteStop.sh')
                os.popen('./stopRecBee.sh ble_scan_v4.py')
            break
        else:
            os.system('echo > /dev/null 2>&1')
            #os.system('clear')
