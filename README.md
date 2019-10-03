# Lab #1: Simple UDP and TCP socket programs
## By Abhilash Munnangi

## Assignment 

The goal of this assignment is to write TCP client and server program so that the client sends a sentence to the server, and the server separates the 
sentence by space bar and returns a list of the lengths of the words separated. Special characters, such as a period or apostrophe are included in the count. 
The Process then is repeated for a UDP Client and Server program. To simplify things, Client and Server-side files are all done by the same computer. The user 
merely needs to replace the serverName based on their computer’s hostname or IPAddress.


## Examples
### Example #1 (Note that the period is counted)

Input::
I’m a student at SJSU.

Output::
3,1,7,2,5

Sentences that are blank return nothing and multiple spaces face the same criteria 

### Example # 2 (Multiple Spaces)
**Note md files do not support multiple spaces so
I added *(multiple spaces in between)* to indicate that the input
can have many spaces in between inputs or *(multiple blanks in between)* to indicate mutliple blank lines** 

Input::
I’m   *(multiple spaces in between)*       a   ()  *(multiple spaces in between)*         student      at  *(multiple spaces in between)*          SJSU.

Output::
3,1,7,2,5

## How to Run 

### 1.UDP
Run UDPserver.py (either through IDE or through terminal)
If need be,replace the serverPort number to a different free port number. Then,run UDPclient.py (through same methods as above)
Replace servername to either your IPAddress or to hostname
*If you replaced the server Port in UDPserver.py, then do the same in this file*

### 2. TCP
Very similar to UDP

Run TCPserver.py (same way as UDP)
If need be,replace the serverPort number to a different free port number.
Run TCPclient.py (through same methods as above)
Replace servername to either your IPAddress or to hostname
*If you replaced the server Port in UDPserver.py, then do the same in this file*
### 3. testcases.txt file
For both UDP and TCP, be sure that testcases.txt is in the same folder. 
So that the file can be opened from either client file.


## Test and Edge cases 
I had all my TestCase Files in a file called *testcases.txt*. I included several custom sentences for an edge case,  List 13 of 
Harvard Lines (https://en.wikipedia.org/wiki/Harvard_sentences), and a passage from Hamlet by William Shakesphere (Act 2 Scene 2). *I tried to include lines from difference sources to diversify my input.* 

Since the two server files have the same functionality, with different approaches and protocols, I used the same test cases for both. 
 

I have several particular edge cases.

### Edge Case #1 (Multiple Spaces)
Input::

One Two Three

One *(multiple spaces in between)*        Two  *(multiple spaces in between)*             Three

Expected Output:

3, 3, 5

3, 3, 5


### Edge Case #2 (Single Blank Line, in between two sentences)
Single blank line is inserted between the two lines
Input::

Above Sentence has many Spaces

Above Sentence is Blank


Returns ::

5, 8, 3, 4, 6

5, 8, 2, 5


### Edge Case #3 (Many Blanks in between two sentences)

Input::

Move the vat over the hot fire.

*(Multiple Blanks in between)*

Above 2 lines are blank is



Output::

4, 3, 3, 4, 3, 3, 5

*(same number of blanks in between)* 

5, 1, 5, 3, 5, 2



## File descriptions

### UDPserver.py

This file represents the server-side of the UDP transport protocol. 
UdpServer first binds a socket and a port number(which is the “door” between transmitting datagrams. The socket has the parameter “SOCK_DGRAM” to 
indicate that it will receive datagrams from clients who follow the UDP protocol. The server uses .decode() to convert the bye stream into a string. 
Once the socket has been bound, the server is in an infinite while look, waiting to receive packets from the client, in this case, is from  UDPclient.py.

Once the sentence has been received, it uses the .split() function to convert the sentence into a list of words, by spaces. 
Then, a for loop counts traverses and find the length of the element in the list and appending it to the answer.

Finally, it uses the .strip() function to remove the brackets from the sentence and then cases the iterated list into a string. Then, the modified sentence is sent back to the client. 

### UDPclient.py

This is the client-side of the UDP transport protocol. Creates a port from the client-side, then a socket, 
which also has the “ SOCK_DGRAM”   and sents it read each line from testcases.txt. Then it encodes the sentences (converts the string into bytes) 
and then sends it to the server name. Once it receives the line, then it is printed. This process is repeated until the file ends. Once the file is 
read, the clientSocket and file closes.

### TCPserver.py

TCPserver.py  has many similarities to UDPserver.py but has a few key differences. Firstly, the TCP socket created has SOCK_STREAM as a parameter, 
which means it accepts TCP datagrams only. The .listen() function has a parameter of 1, specifying the maximum numbers of connections it can handle. 
Then, unlike the UDP server, closes the connection to enable other clients to use it. Aside from that, the file has the same logic to convert sentences as UDPserver.py

###TCPclient.py 

TCPclient.py also has many similarities to UDPclient.py but has a few key differences. A different port number, to enable the user to test the UDP files concurrently. 
The socket created has SOCK_STREAM as a parameter, which means that the connection is reserved. So that means that once a sentence is read, the client has to 
close and reopen the socket in order to send another sentence as there can only be one connection at a time in TCP.