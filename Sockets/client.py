import abc
from socket import *


class Client:
    def __init__(self, host: str, port: int):
        self.HOST = host
        self.PORT = port
        self.MAX_BYTES = 1024

    @abc.abstractmethod
    def send_message(self, text: str) -> bool:
        return None

    @abc.abstractmethod
    def receive_message(self) -> str:
        return None

    @abc.abstractmethod
    def __str__(self) -> str:
        return None

class ClientUDP(Client):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.sock = socket(AF_INET, SOCK_DGRAM)

    def send_message(self, text: str) -> bool:
        text_bytes = text.encode()
        self.sock.sendto(text_bytes, (self.HOST, self.PORT))
        return True

    def receive_message(self) -> str:
        translated_word_bytes, address = self.sock.recvfrom(self.MAX_BYTES)
        translated_word = translated_word_bytes.decode()
        return translated_word

    def close(self) -> bool:
        self.sock.close()
        return True

    def __str__(self) -> str:
        return f'UDP Client assigned to {self.sock.getsockname()}'


class ClientTCP(Client):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))

    def send_message(self, text: str) -> bool:
        try:
            self.sock.connect((self.HOST, self.PORT))
        except:
            pass

        self.sock.sendall(text.encode())
        return True

    @abc.abstractmethod
    def receive_message(self) -> str:
        translated_word = self.sock.recv(self.MAX_BYTES)
        return translated_word.decode()

    def close(self):
        self.sock.close()

    def __str__(self) -> str:
        return f'TCP Client assigned to {self.sock.getsockname()}'
