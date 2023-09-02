# zoom_copy
Simple zoom replication made with python using sockets.

How to use:

inside the file. fill in the ip and port. This only works locally, so all clients must be in the same ip.
Do the same with client.py

Start the server first. This will show all the messages being sent.

py server.py

Each person that wants to join the chat room must start client.py.

py client.py

Users will enter a name. The chatroom will start only after the host joins (enter 'Host' as name to enter as host).
if the host wants to start a breakout room with a user, type 'breakout'. It will then ask to enter the user you want to have a breakout room with.
