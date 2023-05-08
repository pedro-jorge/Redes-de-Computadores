from socket import *


class Client:
    def __init__(self, host: str, port: int):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.host = host
        self.port = port
        self.MAX_BYTES = 65535

    def send_message(self, text: str) -> bool:
        data = text.encode('ascii')
        self.sock.sendto(data, (self.host, self.port))
        return True

    def receive_message(self) -> dict:
        data, address = self.sock.recvfrom(self.MAX_BYTES)
        text = data.decode('ascii')
        return {
            'address': address,
            'text': text
        }

    def __str__(self):
        return f'Client assigned to {self.sock.getsockname()}'
