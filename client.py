
import socket
import threading


HEADER = 64
PORT = 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '' #ip
ADDR = (SERVER, PORT)

breakout = False

breakoutrec = (-1)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


print("enter your name")
username = input()

user = username.encode(FORMAT)
client.send(user)


    
def send(msg):  
            
    
    

    
    
    if msg == "breakout":
        client.send(msg.encode(FORMAT))
        status = True
        
        
        print("Enter student name")
        student = input()
        client.send(student.encode(FORMAT))
        while status:
            breakout_msg = input()
            client.send(breakout_msg.encode(FORMAT))

    else:
        client.send(msg.encode(FORMAT))




y = ''

def rec():
    while True:
        msg = client.recv(HEADER).decode(FORMAT)

        print(f"{msg} from rec")


def start():
    thread = threading.Thread(target=rec)
    thread.start()


start()

   
while y != 'exit':
    y = input()
    send(y)

    




send(DISCONNECT_MESSAGE)