from socket import *
# import codecs
import webbrowser
# from lxml import html
from bs4 import BeautifulSoup as bs
import time
import os

server_Name = gethostbyname(gethostname())
server_Port = 12000

class client_skt() :
    def __init__(self) -> None:
        self.skt_Client  = socket(AF_INET , SOCK_STREAM)
        # print("skt : ",self.skt_Client)
    def connect(self , server_Name , server_Port ) -> None:
        # print("skt : ",self.skt_Client)
        self.skt_Client.connect((server_Name, server_Port))
    
    def send(self, data) -> None:
        self.skt_Client.send(data)

    def recv(self , buffer : int = 2048 ):
        return self.skt_Client.recv(buffer)

    def __html_object_handle(self, filename , file):
        new_response = file[1].decode('utf-8').replace("\r","")
        # print(new_response)
        # os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, "w")
        f.write(new_response)
        f.close()
        return new_response
    def __png_object_handle(self, filename , file):
        new_response = b"" #file[1]#.decode('utf-8').replace("\r","")
        # print(new_response)
        for i in file[1:]:
            new_response += i + b"\n\n"#.replace(b"\r" , b"")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, "wb")
        f.write(new_response[:-1])
        f.close()
        return new_response
    def __css_object_handle(self, filename , file):
        new_response = b"" #file[1]#.decode('utf-8').replace("\r","")
        # print(new_response)
        for i in file[1:]:
            new_response += i + b"\n\n"#.replace(b"\r" , b"")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, "wb")
        f.write(new_response[:-1])
        f.close()
        return new_response
    def __pyscript_object_handle(self, filename , file):
        new_response = b"" #file[1]#.decode('utf-8').replace("\r","")
        # print(new_response)
        for i in file[1:]:
            new_response += i + b"\n\n"#.replace(b"\r" , b"")

        # os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, "wb")
        f.write(new_response[:-1])
        f.close()
        return new_response

    def http_request(self,server_Name , server_Port , file = "index.html"):
        client.connect( server_Name , server_Port)
        request = f"GET /{file} HTTP/1.1\r\nHost:{server_Name}:{server_Port}\r\nConnection: keep-alive".encode()
        self.send(request)

        response = b''
        while True:
            recv = client.recv(1024)
            if not recv:
                break
            response += recv#.decode('utf-8') 
        client.skt_Client.close()
        self.skt_Client  = socket(AF_INET , SOCK_STREAM)
        
        # print(response)
        response = response.split(b"\n\n")
        # print(response[:2])
        print(len(response))
        print(response[0])
        
        # new_response = "<!DOCTYPE html>\n<html lang=\"en\">"
        # for i in response[2:]:
            # new_response += i
        if file.endswith(".html"):
            new_response = self.__html_object_handle( file , response)
        elif file.endswith(".png") or file.endswith(".gif") :
            new_response = self.__png_object_handle( file , response)
        elif file.endswith(".css")  :
            new_response = self.__css_object_handle( file , response)
        elif file.endswith(".py")  :
            new_response = self.__pyscript_object_handle( file , response)
        else:
            print("Formato de arquivo não suportado ainda")

        return new_response 

    def http_request_all(self,server_Name , server_Port , file = "index.html") :
        http = self.http_request(server_Name , server_Port)
        soup = bs( http , 'html.parser')
        # self.http_request(server_Name , server_Port ,
        img_src       = [ self.http_request(server_Name , server_Port , i["src"].replace("\\","/") ) for i in soup.find_all('img')]
        py_script_src = [ self.http_request(server_Name , server_Port , i["src"].replace("\\","/") ) for i in soup.find_all('py-script')]
        css_src       = [ self.http_request(server_Name , server_Port , "css/style.css".replace("\\","/") ) ]

        # print(img_src[2])
        # img = self.http_request(server_Name , server_Port , css_src[0])
        return http
        



client = client_skt()

# client.connect( server_Name , server_Port)
client.http_request_all(server_Name , server_Port , file = "index.html")

"""request = f"GET /index.html HTTP/1.1\r\nHost:{server_Name}:{server_Port}\r\nConnection: keep-alive".encode()
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
f = open("response.html", "w")
f.write(new_response)
f.close()"""
# soup = bs(new_response, 'html.parser')
# img_src = [i["src"] for i in soup.find_all('img')]
# py_script_src = [i["src"] for i in soup.find_all('py-script')]
# css_src = ["css//style.css"]

path = "C:/Users/limaa/PythonProjects/VsCodePython/UFC/Redes/Trab. de Socket/"
chrome_path = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
selenium_chrome_path = "C://tools//selenium//chromedriver.exe"


# driver.get("file://"+path+"response.html")
# print(img_src)
# print(py_script_src)
# print(css_src)


webbrowser.get(chrome_path).open(path+"index.html")

# client.skt_Client.close()