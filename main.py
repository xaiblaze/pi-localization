import sys
import os
import struct
from ctypes import (CDLL, get_errno)
from ctypes.util import find_library
from socket import (
    socket,
    AF_BLUETOOTH,
    SOCK_RAW,
    BTPROTO_HCI,
    SOL_HCI,
    HCI_FILTER,
)

import beacon
from .dataLogger.dataLogger import my_logger

#changes here
iBeacon_addr = beacon.collect_MAC()
logger = my_logger.MyLogger()

btlib = find_library("bluetooth")
bluez = CDLL(btlib, use_errno=True)

dev_id = bluez.hci_get_route(None)

sock = socket(AF_BLUETOOTH, SOCK_RAW, BTPROTO_HCI)
sock.bind((dev_id,))

err = bluez.hci_le_set_scan_parameters(sock.fileno(), 0, 0x10, 0x10, 0, 0, 1000);
if err < 0:
    raise Exception("Set scan parameters failed")
    # occurs when scanning is still enabled from previous call

# allows LE advertising events
hci_filter = struct.pack(
    "<IQH",
    0x00000010,
    0x4000000000000000,
    0
)
sock.setsockopt(SOL_HCI, HCI_FILTER, hci_filter)

err = bluez.hci_le_set_scan_enable(
    sock.fileno(),
    1,  # 1 - turn on;  0 - turn off
    0, 	# 0-filtering disabled, 1-filter out duplicates
    30	# timeout
)

while True:
    #sys.stdout.flush()
    #os.system('clear')

    data = sock.recv(1024)
    # print bluetooth address from LE Advert. packet
    addr = ':'.join("{0:02x}".format(ord(x)) for x in data[12:6:-1])
    rssi = (ord(data[-1]))
    dist = beacon.distance(rssi)
    if(iBeacon_addr.lower() == addr):
	os.system('clear')
	beacon.write_to_file(addr,dist)
	
	#sets current distance and sends json packet
	logger.set_distance(dist)
	logger.send()
        print iBeacon_addr, dist

