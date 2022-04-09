from socket import *
import sys

try:
    domain_name = str(sys.argv[1])
    port = int(sys.argv[2])
except:
    print("Error! Run using << python ./UDPClient.py localhost 6789 >>")
    sys.exit()

sock = socket(AF_INET, SOCK_DGRAM)
data = input("Message: ").encode()
sock.sendto(data, (domain_name, port))

data_received, address = sock.recvfrom(1024)
print("Received from server:\t", data_received.decode())
sock.close()