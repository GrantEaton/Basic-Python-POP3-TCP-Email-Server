"""import socket"""
from socket import *

"""set up server for client to connect to"""
s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 3005))
s.listen(1)
conn, addr = s.accept()
print 'Connection address:', addr

"""create array of messages to be populated, along with Quit bool"""
messages = []
quit = False

"""create messages class for easy toString and expandability"""
class Message:
    """Message class"""
    """constructor"""
    def __init__(self, frm, subj, msg):
        self.frm = frm
        self.subject = subj
        self.message = msg

    """toString"""
    def toString(self):
        return "From: %s \n Subject: %s \n Message: %s \n" % (
            self.frm, self.subject, self.message)

"""read in all the messages and populate the messages array"""
def readInMessages(fileName):

    """open file"""
    file = open(fileName, 'r')

    """iterate through lines in file"""
    for line in file:
        if not line.strip():
            break;
            """split the line into three vars (from, subj, body), then create a Message for each"""
        else:
            lineList = line.split("$$")
            message = Message(lineList[0], lineList[1], lineList[2])
            messages.append(message)

"""read in messages from file"""
readInMessages('emailDB.txt')

"""to be called with list command, iterate through all messages and send the toString to the client"""
def listMessages():
    toSend = ""
    for message in messages:
        toSend += message.toString() + "\n"
    conn.send(toSend)

"""to be called with retr X command, find the message at index, send to client"""
def retrieveMessage(index):
    conn.send(messages[index].toString())

"""continue to look for messages until we want to quit"""
while not quit:

    """get data from client. check if its a valid command, if not, reject it and explain why"""
    data = conn.recv(1024)
    """list command"""
    if data.decode("utf-8") == 'list':
        listMessages()
        """retr command """
    elif 'retr' in data.decode("utf-8"):
        info = data.split(' ')
        retrieveMessage(int(info[1])-1)
        """quit command"""
    elif data.decode("utf-8") == 'quit':
        quit = True
        """Print error"""
    else:
        conn.send("Please enter a valid POP3 command (retr x, list, or quit)")


"""kill connection"""
conn.close()