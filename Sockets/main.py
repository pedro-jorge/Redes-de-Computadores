import argparse
from client import *
from server import *


def start_client(port: int, host='localhost'):
    client = Client(host, port)
    print(client)

    while True:
        text = input('Digite a string de entrada ("close" para fechar o cliente): ')
        if text == 'close':
            break
        client.send_message('luiza linda')
        response = client.receive_message()

        print(f'Resposta do servidor {response["address"]}: {response["text"]}')

def start_server(port: int, host='localhost'):
    print('Iniciando servidor...')
    server = Server(host, port)
    print(server)
    server.start_listening()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    choices = {
        'client': start_client,
        'server': start_server
    }
    parser.add_argument('function', choices=choices, help='Either to start a client or a server.')
    parser.add_argument('--port', type=int, default=1710, help='Which port to use, default=1710.')
    args = parser.parse_args()

    function = choices[args.function]
    function(args.port)
