from socket import *
from colorama import Fore
from pynotifier import Notification

connection = socket(AF_INET, SOCK_STREAM)

ip = input(Fore.YELLOW + "Server IP >>> ")
port = input(Fore.YELLOW + "Connection Port >>> ")

connection.connect((ip, int(port)))

# print(Fore.CYAN + "Connected !")
Notification(title='Connected !', description='Now you connect successfully to server', duration=5, urgency='normal').send()

while True:
    message = connection.recv(1024)
    print(message.decode())
    client = input(Fore.YELLOW + "# ")
    client = Fore.BLUE + (">>> " + client)
    connection.send(client.encode())

connection.close()