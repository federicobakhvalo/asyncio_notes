import asyncio
import socket


class ConnectedSocket:
    def __init__(self, server_socket: socket):
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self):
        print('Вход в контекстный мененджер')
        loop = asyncio.get_event_loop()
        connection, adress = await loop.sock_accept(self._server_socket)
        self._connection = connection
        return self._connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('Выход из контекстного мененджера')
        self._connection.close()
        print('Подключение закрыто')


async def main():
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as connection:
        data=await loop.sock_recv(connection,1024)
        print(data)

asyncio.run(main())
