import socket 
import threading
import time

bsize = 64
PORT = 50001

#SERVER = '10.0.0.212'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
toByte = 'utf-8'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

in_pvt = {} #will keep track of the pvt chat users

usernames = {} # will hold dictionary of all connections {"username" : socket connection}

waitingForHost = "True" # used to check if host is connected


def startClientThread(conn):

    global waitingForHost

    print("waiting for user")
    user = conn.recv(bsize).decode(toByte)#waits for client to enter username

####################
    # this while loop was added after due date
    # while(waitingForHost):
    #         if user == "Host":
    #             print("Host has joined room")
    #             waitingForHost = False
                
    #         else:

    #             time.sleep(5)
    #             print("waiting for host")
    # readymsg = "Host has started room"
    # conn.send(readymsg.encode(toByte))
        
    

    usernames[user] = conn

    print(f"User {user} has connected to the server.")
    
    
    
    print(f"{user} connected")
    
    


    
    connected = True
    while connected:
        
        print("waiting for user message")


        msg = (conn.recv(bsize).decode(toByte))



#############
        #if msg == "pvt" and user == "Host": #added after due

        if msg == "pvt":
            

            student = (usernames[user]).recv(bsize).decode(toByte)

            in_pvt[user] = conn #puts host on break out list
            in_pvt[student] = usernames[student] #puts student in break out list

            status = True

            (in_pvt[student]).send((msg + " started").encode(toByte))
            

            while status:
                breakout_msg = f"{user} sent: " + conn.recv(bsize).decode(toByte)
                (in_pvt[student]).send(breakout_msg.encode(toByte))


        for bstudent in in_pvt:
            
###############           
            #if bstudent != user and user in in_pvt: ##this if statement added after due date
            if bstudent != user:
                msg = f"{user} sent: " + msg
                (in_pvt[bstudent]).send(msg.encode(toByte))
                

        if user not in in_pvt:
            for users in usernames:   

####################                
                #if users != user and users not in in_pvt:#if statement added after due date
                if users != user:
                    print(msg)
                    this_msg = f"{user} sent: " + msg           
                    (usernames[users]).send(this_msg.encode(toByte))


        print(f"{user} sent: {msg}")

            
        if msg == "exit":
            connected = False

    conn.close()
        

def start():

    print("Server started!")
    while True: # loop will wait for connection 
        
        conn, addr = server.accept() #creates a socket and will wait till someone connects

        thread = threading.Thread(target=startClientThread, args=(conn,)) #sends socket to its own thread for messaging
        thread.start()
        
start()
