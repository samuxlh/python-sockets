import socket
import json
import pandas as pd

ip_server = '127.0.0.1'  # Endereco IP do servidor
port_server = 12345      # Porta do servidor

# def lerArquivo():
#   df = pd.read_csv('./data.txt')
#   print(df)

def incluirPrateleira(id):
  print("Entrou na funcao 0")
  return True

def removerPrateleira(id):
  print('id is:', id);
  print("Entrou na funcao 1")
  return True

def alterarIdPrateleira(idAntigo, idNovo):
  df = pd.read_csv('./data.txt')
  print(df)
  return True

def setValorSensor(id, valorSensor):
  print("Entrou na funcao 3")
  return True

def ultimoValorSensor(id):
  print("Entrou na funcao 4")
  return True

def quantidadePrateleiras():
  print("Entrou na funcao 5")
  return False

def listaConteudo():
  print("Entrou na funcao 6")
  return True

def excluirConteudo():
  print("Entrou na funcao 7")
  return True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
  server_socket.bind((ip_server, port_server))
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
        
        idFuncao = dic['ID Funcao']
        status = True

        if idFuncao not in ('0','1','2','3','4','5','6','7','quit'):
            print("Funcao nao encontrada")
        else:
            if idFuncao == '0':
                status = incluirPrateleira(dic['Parametro 1'])
            elif idFuncao == '1':
                status = removerPrateleira(dic['Parametro 1'])
            elif idFuncao == '2':
                status = alterarIdPrateleira(dic['Parametro 1'], dic['Parametro 2'])
            elif idFuncao == '3':
                status = setValorSensor(dic['Parametro 1'], dic['Parametro 2'])
            elif idFuncao == '4':
                status = ultimoValorSensor(dic['Parametro 1'])
            elif idFuncao == '5':
                status = quantidadePrateleiras()
            elif idFuncao == '6':
                status = listaConteudo()
            elif idFuncao == '7':
                excluirConteudo()
            elif idFuncao == 'quit':
                loop = 0
            if(status):
                resposta = 'Operacao realizada com sucesso'
            else:
                resposta = 'Operacao falhou'

        conn.sendall(str.encode(resposta))
