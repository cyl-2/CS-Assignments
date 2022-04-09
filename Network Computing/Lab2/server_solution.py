'''
Multiple clients can connect to one server, once connected, the clients can participate in the chatroom. 
Server receives chat messages from connected clients.
When the server receives a message from a client, the server sends that same message to the terminal of all other connected clients.
The server can also send its own special 'human-inputted' messages to clients. 
The server stores the chat messages in a log file.
'''

from socket import *
from threading import *
from datetime import *

# Establishing a TCP server socket connection
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((gethostname(), 10000))
sock.listen(1)
print('*** Waiting for a connection ***')

# Lists for users and their usernames
users = []
usernames = []

# Displays all messages that are sent by users to other connected chat users
def broadcast(message):
    for user in users:
        user.send(message)

# Receiving messages from client || Sending messages to all clients as the server
def send_receive(user):
    while True:
        try:
            message = user.recv(1024)
            mesg = message.decode()
            print("Received << %s >>" % mesg)
            store(message)
            print("Sending  << %s >> to all connected clients" % mesg)
            broadcast(message)
        except:
            print("ERROR!")
            sock.close()
            break

# Sending inputted messages as the server (command input line for server side)
def send_as_server():
    while True:
        try:
            message1 = input("")
            message1 = "Server: " + message1
            store(message1.encode())
            print("Sending << %s >> to clients" % (message1))
            broadcast(message1.encode())
        except:
            print("ERROR")
            sock.close()
            break

# Starting threads + storing usernames to a list 
def start():
    while True:
        user, address = sock.accept()
        print("Connected with %s" % (str(address)))

        # Ask for a username and append both the user and their username to two separate lists
        user.send('username'.encode())
        username = user.recv(128).decode()
        usernames.append(username)
        users.append(user)

        print("%s has connected to the server and has joined the chat" % (username))
        mesg = "{} joined the chat!".format(username).encode()
        broadcast(mesg)

        # Handling threads to execute tasks simultaneously
        thread = Thread(target=send_receive, args=(user,))
        thread.start()

        start_thread = Thread(target=start)
        start_thread.start()

        send_as_server_thread = Thread(target=send_as_server)
        send_as_server_thread.start()
        
# Stores chat messages in log file
def store(message):
    message = message.decode()
    log = ""
    file1 = open("%s.txt" % datetime.now().date(), "a")
    log = log + '[%s]: stored "%s"\n' % (datetime.now(), message) 
    file1.write(log)
    file1.close()

start()