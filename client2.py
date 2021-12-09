import socket
import json

ip_server = '127.0.0.1' 
port_server = 54321

dic = {'ID Prateleira': '', 
        'ID Funcao': '',
        'Parametro 1': '',
        'Parametro 2': ''}

print('Comunicação com servidor de prateleiras')
print('0 - Inclusão de uma nova prateleira')
print('1 - Remoção de uma prateleira')
print('2 - Alteração do identificador de uma prateleira')
print('3 - Inclusão de novo valor do sensor da prateleira')
print('4 - Apresentação do último valor de sensor recebido')
print('5 - Apresentação do número de prateleiras cadastradas')
print('6 - Apresentação de todo o conteúdo armazenado')
print('7 - Exclusão de todo o conteúdo')

dic['ID Funcao'] = input('Entre com o valor da funcao para ser executada: ')
if dic['ID Funcao'] != 'quit':
    dic['ID Prateleira'] = input('Entre com o ID da prateleira de origem: ')
    if dic['ID Funcao'] not in ('5','6','7'):
        dic['Parametro 1'] = dic['ID Prateleira']
        if dic['ID Funcao'] == '2':
            dic['Parametro 2'] = input('Entre com o novo ID da prateleira: ')
        elif dic['ID Funcao'] == '3':
            dic['Parametro 2'] = input('Entre com o novo valor de sensor: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
    socket_client.connect((ip_server, port_server))
    socket_client.sendall(str.encode(json.dumps(dic)))
    data = socket_client.recv(1024)
    data_str = data.decode()
    print(data_str)
    
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
#     res = socket_client.recv(1024)
#     port_server = res.decode()
#     print('port server ->', port_server)