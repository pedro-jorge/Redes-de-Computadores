import argparse
from client import *
from server import *

def print_and_get_input() -> str:
    print(f'\nDigite uma das palavras a seguir para ter a sua tradução em inglês:\n\n' +
          f'  ####################################################################################\n'
          f'  # cliente        ||   comutador          ||   conexāo      ||   endereço IP        #\n' +
          f'  # endereço MAC   ||   enlace             ||   hospedeiro   ||   largura de banda   #\n' +
          f'  # navegador      ||   porta de entrada   ||   protocolo    ||                      #\n' +
          f'  # redes          ||   roteador           ||   servidor     ||                      #\n' +
          f'  ####################################################################################\n')
    text = input('Entre com a palavra a ser traduzida ("close" para sair): ')

    return text

def start_client_udp(port: int, host: str='localhost'):
    #port = 1711
    client = ClientUDP(host, port)
    print(client)

    while True:
        text = print_and_get_input()

        if text == 'close':
            break
        client.send_message(text)
        response = client.receive_message()

        if response != '0':
            print(f'A tradução da palavra "{text}" é "{response}"')
        else:
            print(f'A palavra não foi encontrada no dicionário.')

    client.close()


def start_server_udp(port: int, host: str='localhost'):
    #port = 1711
    print('Iniciando servidor UDP...')
    server = ServerUDP(host, port)
    print(server)
    server.start_listening()


def start_client_tcp(port: int, host: str='localhost'):
    #print(client)

    while True:
        client = ClientTCP(host, port)
        text = print_and_get_input()

        if text == 'close':
            break
        client.send_message(text)
        response = client.receive_message()

        if response != '0':
            print(f'A tradução da palavra "{text}" é "{response}"')
        else:
            print(f'A palavra não foi encontrada no dicionário.')

        client.close()


def start_server_tcp(port: int, host: str='localhost'):
    port = 1710
    print('Iniciando servidor TCP...')
    server = ServerTCP(host, port)
    print(server)
    server.start_listening()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    choices = {
        'client_udp': start_client_udp,
        'server_udp': start_server_udp,
        'client_tcp': start_client_tcp,
        'server_tcp': start_server_tcp
    }
    parser.add_argument('function', choices=choices, help='Either to start a client or a server.')
    parser.add_argument('--port', type=int, default=1710, help='Which port to use, default=1710.')
    args = parser.parse_args()

    function = choices[args.function]
    function(args.port)
