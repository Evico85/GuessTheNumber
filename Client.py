import socket

#Variables for Client Communication
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "Client is DISCONNECTED!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

#Socket for the Client
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect(ADDR)

#Function for send Messages to Server:
def send(txt):
    text = txt.encode(FORMAT)
    txt_length = len(text)
    send_length = str(txt_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    Client.send(send_length)
    Client.send(text)
    print(Client.recv(2048))

send("Hi!")

send(DISCONNECT_MSG)