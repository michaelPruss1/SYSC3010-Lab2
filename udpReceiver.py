# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('', port)
s.bind(server_address)

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    echoBuf = "ACK: " + buf
    s.sendto(echoBuf.encode('utf-8'), address)
    
    print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))

s.shutdown(1)
