from socket import *
# import thread

server_Name = ""
server_Port = 12000

class client_skt() :
    def __init__(self) -> None:
        self.skt_Client  = socket(AF_INET , SOCK_STREAM)
    
    def connect(self , server_Name , server_Port ) -> None:
        self.skt_Client.connect((server_Name, server_Port))
    
    def send(self, data) -> None:
        self.skt_Client.send(data)

    def recv(self , buffer : int = 2048 ):
        return self.skt_Client.recv(buffer)


# tcp.bind()