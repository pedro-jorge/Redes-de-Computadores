from socket import *


class Server:
    def __init__(self, host: str, port: int):
        self.MAX_BYTES = 65535
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((host, port))
        self.start_listening()

    def start_listening(self):
        while True:
            data, address = self.sock.recvfrom(self.MAX_BYTES)
            text = data.decode('ascii')
            print(f'Message from client at {address}: {text}')
            text = f'{len(data)} bytes received.'
            data = text.encode('ascii')
            self.sock.sendto(data, address)

    def __str__(self):
        return f'Listening at {self.sock.getsockname()}'
