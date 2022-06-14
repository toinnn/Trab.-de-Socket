from socket import *
# import thread

server_Name = ""
server_Port = 12000

class server_skt():
     def __init__(self) -> None:
        self.skt_Server  = socket(AF_INET , SOCK_STREAM)
        self.skt_Server.bind(("" , server_Port))
        self.skt_Server.listen(1)
        print("Server Ligado")