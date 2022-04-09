''' 
The client connects to the server. 
The client is asked for a username to identify the client in the chatroom, then the client joins the chat.
The client can chat to any other connected clients that are connected to the same server.
All clients can see the messages that are sent in the chat. 
The messages are sent to be handled by the server.
'''

from socket import *
from threading import *

# Create a TCP socket connection
sock = socket(AF_INET, SOCK_STREAM)
print('connecting to server at %s port %s' % (gethostname(), str(10000)))
sock.connect((gethostname(), 10000))

# Ask user to create a username to identify them
username = input("Type in your username: ")

# Requesting for the users' usernames
def request_username():
    while True:
        try:
            message = sock.recv(1024).decode()          # receives a request message from the server side
            if message == 'username':                   # if the message is the string "username"
                sock.send(username.encode())            # then send the human-inputted username back to the server
            else:
                print(message)
        except:
            print("ERROR!")
            sock.close()                                # connection closes if an error occurrs
            break

# Sending messages to other clients + server
def send_message():
    while True:
        message = '{}: {}'.format(username, input(''))  
        sock.send(message.encode())

# Threads for performing 2 tasks at the same time
request_username_thread = Thread(target=request_username)
request_username_thread.start()

send_message_thread = Thread(target=send_message)
send_message_thread.start()