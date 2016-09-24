"""import and set up socket on IP and port #"""
from socket import *
clientSocket = socket( AF_INET ,  SOCK_STREAM  )
clientSocket.connect(('127.0.0.1', 3005))
"""set a boolean quit variable to detect quit command (NOTE the quit command will kill client and server"""
quit= False
"""continue asking for a message until we quit"""
while(not quit):
    data = None

    """get the input from the user"""
    input = raw_input('Command:')

    """"decode the input, just in case it wasnt utf-8 format, check if its quit, then kill client"""
    if(input.decode("utf-8") == 'quit'):
        quit = True
        print("Killing client and server!")
    clientSocket.send(input)

    """if quit, ignore. else, keep looping until we hear back from server"""
    while(data is None and quit is False):
        """recieve message"""
        data = clientSocket.recv(1024)

    """Print message from server"""
    print(data)