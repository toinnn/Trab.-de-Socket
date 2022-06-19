from socket import *
# import thread

server_Name = gethostbyname(gethostname())
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


client = client_skt()
client.connect( server_Name , server_Port)
request = f"GET /index.html HTTP/1.1\r\nHost:{server_Name}:{server_Port}\r\nConnection: keep-alive".encode()
client.send(request)

response = ''
while True:
    recv = client.recv(1024)
    if not recv:
        break
    response += recv.decode('utf-8') 

# print(response)
response = response.split("\r")
new_response = "<!DOCTYPE html>\n<html lang=\"en\">"
for i in response[2:]:
    new_response += i
print(new_response)
client.skt_Client.close()