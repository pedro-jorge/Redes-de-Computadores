import abc
from socket import *


class Server:
    def __init__(self, host: str, port: int):
        self.HOST = host
        self.PORT = port
        self.MAX_BYTES = 2048
        self.words_dict = {
            'rede': 'network',
            'roteador': 'router',
            'comutador': 'switch',
            'protocolo': 'protocol',
            'cliente': 'client',
            'servidor': 'server',
            'hospedeiro': 'host',
            'endereco IP': 'IP address',
            'navegador': 'browser',
            'conexão': 'connection or link',  ##
            'enlace': 'link',
            'endereço MAC': 'MAC address',
            'largura de banda': 'bandwidth',
            'porta de entrada': 'gateway'
        }

    def translate(self, word: str) -> str:
        if word.lower() in self.words_dict.keys():
            return self.words_dict[word.lower()]
        return '0'

    @abc.abstractmethod
    def start_listening(self):
        return None

    @abc.abstractmethod
    def __str__(self) -> str:
        return None

class ServerUDP(Server):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((host, port))
        self.start_listening()

    def start_listening(self):
        while True:
            text_bytes, client_address = self.sock.recvfrom(self.MAX_BYTES)
            text = text_bytes.decode()
            translated_text = self.translate(text)
            self.sock.sendto(translated_text.encode(), client_address)

    def __str__(self) -> str:
        return f'UDP Server listening at {self.sock.getsockname()}'


class ServerTCP(Server):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.MAX_BYTES = 1024
        self.sock = socket(AF_INET, SOCK_STREAM)

        print(f'Servidor rodando na porta {port}')

        self.sock.bind((host, port))
        self.sock.listen(5)
        self.start_listening()

    def start_listening(self):
        while True:
            conn, address = self.sock.accept()
            text_bytes = conn.recv(self.MAX_BYTES)
            text = text_bytes.decode()
            translated_text = self.translate(text)
            conn.sendall(translated_text.encode())
            conn.close()

    def __str__(self) -> str:
        return f'TCP Server listening at {self.sock.getsockname()}'
