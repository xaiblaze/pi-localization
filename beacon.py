import sys

def collect_MAC():
    print("Enter beacon MAC address: ")
    a = raw_input()
    return a

def distance(rssi):
    txpower = -56.0 #standard value

    #2's compliment is needed here
    rssi = -((rssi ^ 255) + 1)

    if rssi == 0 :
        return -1
    else:
	ratio = rssi/txpower
        if ratio < 1:
	    return ratio**10
	else:
	    return 0.89976 * ratio**7.7095 + 0.111

def write_to_file(addr, dist):
    with open('distances.txt','a') as d:
	tmp = addr + " " + str(dist) + "\n"
	d.write(tmp)
    d.closed

