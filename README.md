# Basic-Python-POP3-TCP-Email-Server


This is a basic Python POP3 TCP email server. It can only do three commands: retr, list and quit, but can be easily expanded upon.

TO RUN IN TERMINAL: 
(note i havent tested these exact commands thanks to my windows computer, but you should be able to run this with basic linux experience).

1. download the full repo as a zip.
2. unzip files to directory you want (MAKE SURE THE EMAILDB.TXT FILE GOES IN THIS DIRECTORY)
3. cd into your directory with the files 
	ex. cd users/documents/"directoryIWant"
4. Make sure python is installed with python -v (you should get a version, if not, google how to install python.)
5. type "python PythonTCPServer.py" in the terminal
	-The script should run and get "stuck" (its in a while loop waiting for a client message)
6. type "python TCPClient.py"
	- you should get "Command:" in the prompt. this meants it working and your connected to the server.
7. skip to step "using the basic server"



TO RUN IN PYCHARM OR ANY OTHER IDE

1. download the full repo as a zip.
2. unzip files to your IDE's workspace directory or drag and drop it into a new project.
	*NOTE: (MAKE SURE THE EMAILDB.TXT FILE GOES IN THIS DIRECTORY)
3. open up the files in the IDE
4. run PythonTCPServer.py
5. run TCPClient.py
	- you should get "Command:" in the prompt. this meants it working and your connected to the server.
6. skip to step "using the basic server"


USING THE BASIC SERVER:
 	-you can use 3 commands right now: list, retr X, and quit
	-retr x: type "retr x" with "x" being a number 1-10. this will send the client the email at that index.
	-list: type "list". this will send the client all the emails in the Database
	-quit: this will kill the client and the server

expanding upon the code: you can easily add new commands based on the POP3 sytax in the server code.

Enjoy and Learn!
