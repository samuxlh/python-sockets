import socket
import json

ip_server = '127.0.0.1'  # Endereco IP do servidor
port_server_local = 54321 # Porta local client
port_server = 12345 # Porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((ip_server, port_server_local))
    server_socket.listen()
    print('Servidor ligado!')
    loop = 1
    while loop == 1:
        conn, addr = server_socket.accept()
        with conn:
            print('Cliente conectado: ', addr)
            data = conn.recv(1024)
            dic = json.loads(data.decode())
            print('Mensagem recebida: ', dic)
            print(dic['ID Funcao'])
                        
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
                socket_client.connect((ip_server, port_server))
                socket_client.sendall(data)
                data = socket_client.recv(1024)
                data_str = data.decode()
                conn.sendall(str.encode(data_str))
                
            if dic['ID Funcao'] == 2:
                if dic['Parametro 1'] == '1':
                    conn.sendall(str.encode(port_server))
