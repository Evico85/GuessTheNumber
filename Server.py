import socket
from turtle import width
import pyfiglet
import threading
import random

#Banners Of the game
ascii_banner = pyfiglet.figlet_format("GUESS THE NUMBER!!" ,width=110)
goodbye_banner = pyfiglet.figlet_format("Thank You For Playing", font ="colossal" ,width = 210)
# Variables For Communication:
HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
DISCONNECT_MSG = "Client is DISCONNECTED!"
# To Be able to run This Server on any Host Without Change IP anytime..
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
# if you want to see your IP address of the server do: 
# print(SERVER)

#create socket for server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#Function for Communicate with Client
def get_client(connect,addr):
    print(f"[GOT CONNECTION FROM...] {addr}.")
    
    connected = True
    while connected:
        msg_length = connect.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            MSG = connect.recv(msg_length).decode(FORMAT)
            if MSG == DISCONNECT_MSG:
                connected = False 
            print(f"[{addr}] send: {MSG}")
            #main loop of the game after connection:
            print("Welcome to my game")
            name = input("Please Enter Your Name: ")
            print(f"Welcome to my game {name}\n")
            print("Rules:\n1) You need To Choose number between 1-20\n2) you cant Enter a letter or symbol cause you will get WRONG!\n3) you got only 3 tries and after that you lose")
            print("4) if you guessed the number You won!!")
            Selected_number = random.randint(1,20)
            Counter = 3
            #Check user input Function:
            def check_user_input(try_Guess):
                while True:
                    # if user wants to quit the game at ant time
                    if try_Guess == "q":
                        print("Goodbye!!")
                        print(DISCONNECT_MSG)
                        quit() 
                    #Chack if the input is a digit and if it does return it as int   
                    if str(try_Guess).isdigit():
                        return int(try_Guess)
                    else:
                        print("Not a Number..\nTry again")
                        try_Guess = input("Please Enter a Number: " + "[Enter q to quit] ")  
                        continue                
            while Counter != 0:
                Guess = input("Please Enter a Number: " + "[Enter q to quit] ")
                Guess = check_user_input(Guess)
                if Guess == Selected_number:
                    print("YOU WON!")
                    print("Bye..")
                    print(goodbye_banner)
                    break
                if Guess > Selected_number:
                    print("Your Guess is Too High..")
                    Counter = Counter - 1
                    print(f"You Got {Counter} tries left..")
                elif Guess < Selected_number:
                    print("Your Guess is Too low..")
                    Counter = Counter - 1
                    print(f"You Got {Counter} tries left..")
                if Counter == 0:
                    print("You lost :(")
                    print(goodbye_banner)
                    break   
    connect.close()

#Function for connection with Client
def start():
    server.listen()
    print(f"Server is listening on: {SERVER}")
    while True:
        connect,addr = server.accept()
        #after we got connection from Client we pass the Connection to get_client Function for Communication
        thread = threading.Thread(target=get_client, args=(connect,addr))
        thread.start()
        #To see How many connections we have i use this line:
        print(f"[ACTIVE CONNECTIONS:] {threading.active_count() -1}")


print(ascii_banner + "\nWelcome to my game!!")
start()
