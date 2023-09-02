
import socket
import threading


bsize = 64
PORT = 50001
toByte = 'utf-8'


#SERVER = '10.0.0.212' #ip
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

breakout = False

breakoutrec = (-1)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


print("enter your name")
username = input()

user = username.encode(toByte)
client.send(user)


    
def send(msg):  
    #if the msg is pvt, it will ask for user to go into pvt with.        
    
    

    
    #  
###########    
    #if msg == "pvt" and username == "Host": #this was added after due
    if msg == "pvt":
        client.send(msg.encode(toByte))
        status = True
        
        
        print("Enter student name")
        student = input()
        client.send(student.encode(toByte))
        while status:
            breakout_msg = input()
            client.send(breakout_msg.encode(toByte))

    else:
        client.send(msg.encode(toByte))



y = ''

def rec():
    while True:
        msg = client.recv(bsize).decode(toByte)
        print(f"{msg}")


def start():
    print("thread started")
    thread = threading.Thread(target=rec)
    thread.start()


start()

   
while y != 'exit':
    y = input()
    send(y)

    
