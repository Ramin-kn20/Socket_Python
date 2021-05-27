from socket import *
from colorama import Fore

connection = socket(AF_INET, SOCK_STREAM)

connection.bind(("192.168.0.34", 1214))
connection.listen(1)

print(Fore.LIGHTGREEN_EX + "********** Server is running **********\n")

client , address = connection.accept()
print(Fore.MAGENTA + "Client connect with IP : " + str(address))

while True:
    message = input(Fore.YELLOW + "# ")
    message = Fore.BLUE + (">>> " + message  )
    client.send(message.encode())
    recive = client.recv(1024)
    print(recive.decode())


client.close()