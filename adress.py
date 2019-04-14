#pyhton program to get IP address
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("your computer name is :"+hostname)
print("your computer IP Address is :"+IPAddr)
