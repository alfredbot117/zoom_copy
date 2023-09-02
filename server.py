import socket 
import threading

HEADER = 64
PORT = 
SERVER = 'ip'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

in_breakout = {}

usernames = {}

def handle_client(conn, addr):

    print(f"[NEW CONNECTION] {addr} connected.")
    print("waiting for user")
    
    user = conn.recv(HEADER).decode(FORMAT)#waits for client to enter username
    
    usernames[user] = conn
    
    print(f"{user} connected")
    
    for users in usernames:
        print(users)

    
    connected = True
    while connected:
        
        print("waiting for user message")
        msg = conn.recv(HEADER).decode(FORMAT)

        if msg == "breakout":

            student = (usernames[user]).recv(HEADER).decode(FORMAT)

            in_breakout[user] = conn #puts host on break out list
            in_breakout[student] = usernames[student] #puts student in break out list

            status = True

            (in_breakout[student]).send(msg.encode(FORMAT))
            

            while status:
                breakout_msg = conn.recv(HEADER).decode(FORMAT)
                (in_breakout[student]).send(breakout_msg.encode(FORMAT))

        print(f"from {user}")

        for bstudent in in_breakout:
            print(f"this person is {bstudent}")
            if bstudent != user:
                print(bstudent)
                print(f"this person is a {bstudent}")
                (in_breakout[bstudent]).send(msg.encode(FORMAT))
                

        if user not in in_breakout:
            for users in usernames:   
                if users != user:            
                    (usernames[users]).send(msg.encode(FORMAT))


        

        print(f"{user} sent: {msg}")



            

                    
                    



            
        if msg == "exit":
            connected = False




    conn.close()
        

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        


print("running")
start()
