from socket import *
# import ssl
# import codecs
import webbrowser
# from lxml import html
from bs4 import BeautifulSoup as bs
import time
import os

server_Name = gethostbyname(gethostname())
server_Port = 80

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
        new_response = b"" 
        for i in file[1:]:
            new_response += i + b"\n\n"#.replace(b"\r" , b"")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, "wb")
        f.write(new_response[:-1])
        f.close()
        return new_response
    def __css_object_handle(self, filename , file):
        new_response = b"" 
        for i in file[1:]:
            new_response += i + b"\n\n"#.replace(b"\r" , b"")

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, "wb")
        f.write(new_response[:-1])
        f.close()
        return new_response
    def __pyscript_object_handle(self, filename , file):
        new_response = b"" 
        for i in file[1:]:
            new_response += i + b"\n\n"#.replace(b"\r" , b"")

        if len(filename.split("/")) > 1 :
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        f = open(filename, "wb")
        f.write(new_response[:-1])
        f.close()
        return new_response
    def __outside_object_handle(self, filename , file):
        """filename = filename.replace("https://" , "")
        filename = filename.split("/")
        new_filename = ""
        print("Filename : " , filename)
        for i in filename[1:]:
            new_filename += "/"+ i
        new_filename = new_filename[1:]"""
        new_response = b"" #file[1]#.decode('utf-8').replace("\r","")
        # print(new_response)
        for i in file[1:]:
            new_response += i + b"\n\n"#.replace(b"\r" , b"")

        if len(filename.split("/")) > 1 :
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        f = open(filename, "wb")
        f.write(new_response[:-1])
        f.close()
        print("Deu certo lá fora")
        return new_response

    def http_request(self,server_Name , server_Port , file = "index.html"):
        self.connect( server_Name , server_Port)
        print("file atual é o " , file)
        if file.startswith("http://"):
            pass
            # file = file.replace("https://" , "")
            # file = file.split("/")
            # host = file[0]
            # file_name = ""
            # for i in file[1:] :
            #     file_name += "/" + i
            # file = file_name
            # print("host : " , host ,"\nfile : " , file)

            # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            # s = socket(AF_INET, SOCK_STREAM)
            # self.skt_Client = context.wrap_socket(s, server_hostname=host)
            # self.skt_Client.connect((host, 443))

            # request = f"GET /{file} HTTP/1.1\r\nHost:{host}\r\nConnection: keep-alive".encode()
        else :
            request = f"GET /{file} HTTP/1.1\r\nHost:{server_Name}:{server_Port}\r\nConnection: keep-alive".encode()
        self.send(request)

        response = b''
        while True:
            recv = self.recv(1024)
            if not recv:
                break
            response += recv#.decode('utf-8') 
        self.skt_Client.close()
        self.skt_Client  = socket(AF_INET , SOCK_STREAM)
        
        # print(response)
        response = response.split(b"\n\n")
        print(len(response))
        # print(response[0])
        
        
        if file.startswith("https://") or file.startswith("http://") :
            print("Entrou no https://")
            new_response = self.__outside_object_handle( file , response)
        elif file.endswith(".html"):
            new_response = self.__html_object_handle( file , response)
        elif file.endswith(".png") or file.endswith(".gif") :
            new_response = self.__png_object_handle( file , response)
        elif file.endswith(".css")  :
            new_response = self.__css_object_handle( file , response)
        elif file.endswith(".py") or file.endswith(".js")  :
            new_response = self.__pyscript_object_handle( file , response)
        else:
            print("Formato de arquivo não suportado ainda")

        return new_response 

    def http_request_all(self,server_Name , server_Port , file = "index.html") :
        http = self.http_request(server_Name , server_Port)
        soup = bs( http , 'html.parser')
        
        img_src       = [ self.http_request(server_Name , server_Port , i["src"].replace("\\","/") ) for i in soup.find_all('img')]
        py_script_src = [ self.http_request(server_Name , server_Port , i["src"].replace("\\","/") ) for i in soup.find_all('py-script')]
        link_src      = [ self.http_request(server_Name , server_Port , i["href"].replace("\\","/")) for i in soup.find_all("link")]
        script_src    = [ self.http_request(server_Name , server_Port , i["src"].replace("\\","/") ) for i in soup.find_all("script")]
        py_script_src +=[self.http_request(server_Name , server_Port , "pyscript/pyscript.py")]
        img_src       +=[self.http_request(server_Name , server_Port , "images/game-over.png")]
        
        # print(script_src)
        # img = self.http_request(server_Name , server_Port , css_src[0])
        return http
        



client = client_skt()

# client.connect( server_Name , server_Port)
client.http_request_all(server_Name , server_Port , file = "index.html")


path = "C:/Users/limaa/PythonProjects/VsCodePython/UFC/Redes/Trab. de Socket/"
chrome_path = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
selenium_chrome_path = "C://tools//selenium//chromedriver.exe"


# driver.get("file://"+path+"response.html")
# print(img_src)
# print(py_script_src)
# print(css_src)


webbrowser.get(chrome_path).open(path+"index.html")

# client.skt_Client.close()