import socket 
import requests
import time 
import pyfiglet 
from datetime import datetime 
import sys  

GREEN = "\033[0;32m"
ascii_banner = pyfiglet.figlet_format("MAP PORT") # print banner
print(ascii_banner)
ip = input("-> Qual ip deseja buscar?\n-> ")

if ip == '':                #caso nao tenha ip 
    print("error")
    exit()
try:
    r = requests.get(ip)
    if r.status_code != 200:                #testando a conexao ao servidor 
        print("IP SEM CONEXAO")
    else:
        pass
except:
    pass

tam = input("Quantidade de portas que deseja buscar\n[EXAMPLE] [200(1-200)]\n-> Para um scan agressivo digite 'A'-> ") # digitar ate qual porta deseja buscar 
tamnum = int(tam)+1
if tam == 'A': #caso queira ele agressivo, vai buscar ate a porta 49151
    tamnum = 49151
    print("AGRESSIVE SCAN START")
time.sleep(2)

try:
    target = socket.gethostbyname(ip)                                               # conectando ao servidor e inicando varredura
    ascii_banner = pyfiglet.figlet_format("START PORT SCAN")
    print(ascii_banner)
    print("Iniciando busca...")                 
    print("Scanning started at: " + str(datetime.now()))
    for port in range(1,tamnum):                                                       #buscando as portas uma por uma 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) 
        result = s.connect_ex((target,port))                                    #portas encontradas
        hora = str(datetime.now())
        if result ==0:
            name = socket.getservbyport(port)
            ipp = socket.getaddrinfo(ip, port)
            print(GREEN,"-> TIME | {} | -> IP | {} | -> PORT OPEN | {} | -> SERVICE | {} |".format(hora,ipp,port,name))   #print caso ache a porta aberta
        s.close()

except KeyboardInterrupt:                                 # control c para parar o sistema
        print("\n Control + C ")
        sys.exit()  
except socket.gaierror:                                                    # caso nao acesse o host
        print("\n Nao foi possivel acessar o host")
        sys.exit()
except socket.error:                                                            # caso de erro ao se conectar
        print("\ Servidor 404 ERROR")
        sys.exit()
