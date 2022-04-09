from socket import *
from datetime import datetime

ip = "localhost"
port = 6789

sock = socket(AF_INET, SOCK_DGRAM)  #SOCK_DGRAM for UDP
sock.bind((ip, port))

print("%s\t%s" % (ip, port))

while True:
    try:
        data, client = sock.recvfrom(1024)
        data = data.decode()

        print("Received << ", data, " >> from client : ", client)
        print("Client Address:", client[0])
        print("Client Port:", client[1])

        time = datetime.now()
        log = ""
        time1 = time.strftime("%d%m%Y%H%M%S")

        try:
            f = open("log_file.txt", "x")
        except:
            f = open("log_file.txt", "a")

        log = log + '[%s]: received "%s"\n' % (time, data) 
        f.write(log)
        f.close()    
            
        data = data.upper()
        data2 = "[" + str(time) + "]: " + data
        
        print("Sending << %s >> to client" % data2)
        sock.sendto(data2.encode(), client)

    except:
        print("Something went wrong, socket will close.")
        sock.close()
        break