#!/usr/bin/env python
import socket
import time, sys
from datetime import datetime
from tld import get_tld

#assign variables
host = ''
min_port = 20
max_port = 30

# This dictionary contains the most popular ports used
# You can add ports here. 
# The key is the port number and the values is the service used by that port
common_ports = {

	'21': 'FTP',
	'22': 'SSH',
	'23': 'TELNET',
	'25': 'SMTP',
	'53': 'DNS',
	'69': 'TFTP',
	'80': 'HTTP',
	'109': 'POP2',
	'110': 'POP3',
	'123': 'NTP',
	'137': 'NETBIOS-NS',
	'138': 'NETBIOS-DGM',
	'139': 'NETBIOS-SSN',
	'143': 'IMAP',
	'156': 'SQL-SERVER',
	'389': 'LDAP',
	'443': 'HTTPS',
	'546': 'DHCP-CLIENT',
	'547': 'DHCP-SERVER',
	'995': 'POP3-SSL',
	'993': 'IMAP-SSL',
	'2086': 'WHM/CPANEL',
	'2087': 'WHM/CPANEL',
	'2082': 'CPANEL',
	'2083': 'CPANEL',
	'3306': 'MYSQL',
	'8443': 'PLESK',
	'10000': 'VIRTUALMIN/WEBMIN'
}

#This is the limited number of ports that we want to scan.
#You can add some to if you want to scan more ports
listing_ports = [21, 22, 23, 25, 80, 109, 110, 156, 443, 3306]

#initial information to display to the user
def initializing():
    #print out some information
    print("[*] PORT SCANNING SCRIPT BY EMMALLEN NETWORKS<br>")
    print("[*] For educational purposes only [*]<br>")
    print("*" * 100, end='<br>')
    
#call the the very first function
initializing()

#request the user to enter domain name
#host    = input("[*] Enter a Remote Host to scan: ")
host = sys.argv[1]

#get the top level domain name
host = get_tld(host)

#get the real ip address of the domain name entered by the user
ipaddress  = socket.gethostbyname(host)

#get the starting time
t1 = time.time()

# Print a nice banner with information on which host we are about to scan
print("[*]", "-" * 100, "[*]<br>")
print("[*] Remote Host: <strong>", host, "</strong> IP Address: <strong>", ipaddress, "</strong><br>")
print("[*] Scanning started at <strong>", host, "</strong> TIME: ", time.strftime("%I:%M:%S %p"), "<br>")
print("[*]", "-" * 100, "[*]<br>")

#function to fetch the name of a port
def port_opened(port):
    # converts the int to string
    port = str(port)
    # check if the port is available in the common ports dictionary
    if port in common_ports:
        # returns the service name if available
        print("<tr style='color:green'><td width='10%'>[*]</td><td width='20%'>", port, "</td><td width='40%'>", common_ports[port] ,"</td><td width='30%'>Port is Opened</td></tr>")

#if the port is closed then run this script
def port_closed(port):
    # converts the int to string
    port = str(port)
    # check if the port is available in the common ports dictionary
    if port in common_ports:
        # returns the service name if available
        print("<tr style='color:red'><td width='5%'>[*]</td><td width='10%'>", port, "</td><td width='30%'>", common_ports[port] ,"</td><td width='20%'>Port is Closed</td></tr>")

#using the range function to specify ports to scan
#we also put in some error handling for catching errors
try:

    #print header of table
    print("<table border='0' width='500px'>")
    print("<tr style='font-weight:bolder'><td>[*]</td><td>PORT</td><td>SERVICE</td><td>STATUS</td><td>SOFTWARE VERSION</td></tr>")
    
    for port in listing_ports:
        
        #port : port to scan
        #ipaddress : the ipaddress of the domain name
        #create the connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
	#set the timeout else there will be delays
        sock.settimeout(5)
        
	#fetch the connection results
        #check the port connection to
        result = sock.connect_ex((ipaddress, port))
        #the result is 0 if the port is opened
        if result == 0:
            #call the port name function
            port_opened(port)
        else:
            port_closed(port)
        sock.close()

    #print footer of table
    print("</table>")
        
except KeyboardInterrupt:
    print("[*] You interrupted the process<br>")
    sys.exit(1)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting<br>")
    sys.exit(1)
except socket.error:
    print("Couldn't connect to the server<br>")
    sys.exit(1)


#get the time that the system finished checking the ports
t2 = time.time()

#difference
time_spent = t2 - t1

#print out the final information
print("[*]", "-" * 100, "[*]<br>")
print("<br>[*] Scanning completed at: <em>", time.strftime("%I:%M:%S %p"), "</em>")
#time spent calcultion
if time_spent <= 60:
    time_spent = str(round(time_spent, 2))
    print("<br>[*] Scanning Duration: <em>", time_spent, " seconds</em><br>")
else:
    time_spent = round((time_spent / 60), 2)
    print("[*] Scanning Duration: <em>", time_spent, " minutes</em><br>")

print("*" * 100)
print("""This program is intended for individuals to test their own equipment for weak
security, and the author will take no responsibility if it is put to any other use""")
print("[*] Enjoy your day and have fun!<br>")
print("*" * 100)
