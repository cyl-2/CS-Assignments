from socket import *
import sys

''' Command line input : python ./client_solution.py localhost 6789 HelloWorld.html '''

clientSocket = socket(AF_INET, SOCK_STREAM)

target_host = str(sys.argv[1])
target_port = int(sys.argv[2])
target_filename = str(sys.argv[3])
request = "GET /" + target_filename + " HTTP/1.1"

server_address = (target_host, target_port)
clientSocket.connect(server_address)

print('Connected to server at %s, port %s' % server_address)

print(request)

try:
    clientSocket.send(("GET /%s" % target_filename).encode())

    data = clientSocket.recv(1024).decode()
    while len(data) > 0:
        print("%s" % data, end="")
        data = clientSocket.recv(1024).decode()

finally:
    clientSocket.close()
    print("Socket Closed")