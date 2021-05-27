from socket import * 
import time
from colorama import Fore

connection = socket(AF_INET, SOCK_STREAM)
connection.bind(("192.168.0.34", 1313))
connection.listen(1)
print(Fore.BLUE + "Server is running on  >>>>   192.168.0.34:1313")

while True: 
    client, address = connection.accept()
    print(Fore.YELLOW + "Client connected on >>>>  "+str(address))
    message = Fore.RED + "Corrent Time --->>>>   "+str(time.ctime())
    client.send(message.encode())
connection.close()