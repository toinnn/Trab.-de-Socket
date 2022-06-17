from socket import *
import threading

server_Name = gethostbyname(gethostname())
server_Port = 12000
# addr = ()
print(server_Name)
class server_skt():
    def __init__(self) -> None:
        self.skt_Server  = socket(AF_INET , SOCK_STREAM)
        self.skt_Server.bind((server_Name , server_Port))
        self.skt_Server.listen(1)
        print("Server Ligado")
    
    def handle_request(self , connection , addr):
        print("[NOVA Conexão..]")
        # global conexoes
        # name = False

        while True :
            msg = connection.recv(1024).decode('utf-8')
            if msg :
                cmd_request = msg.split(' ')
                method = cmd_request[0]
                args = cmd_request[1:]
                print('Client request ',args)
                try :
                    for i in args:
                        file = open(i,"rb")
                        response = file.read()
                        file.close()

                        header = 'HTTP/1.1 200 OK\n'
                        if i.endswith(".png"):
                            header += f"Content-Type: image/png"+"\n\n"
                        elif i.endswith(".gif") :
                            header += f"Content-Type: image/gif"+"\n\n"
                        elif i.endswith(".css") :
                            header += f"Content-Type: text/css"+"\n\n"
                        else:
                            header += f"Content-Type: text/html"+"\n\n"

                except Exception as e:
                    header   = 'HTTP/1.1 404 Not Found\n\n'
                    response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')

                final_response  = header.encode('utf-8')
                final_response += response
                connection.send(final_response)
                connection.close()
                return

    def start_server(self):
        listen()
        print("[Server Ouvindo...]")
        while True:
            client = accept()
            td = threading.Thread(target = self.handle_request , args=client)