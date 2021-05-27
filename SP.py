from socket import *

connection = socket(AF_INET, SOCK_STREAM)
connection.connect(("192.168.0.34", 1313))
print("Connected !!!!!")
data = connection.recv(1024)
print(data.decode())
connection.close()