# SPDX-FileCopyrightText: 2023-present Filip Strajnar <filip.strajnar@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0

import socket
from typing import Callable


def tcp_listener(handler: Callable[[socket.socket], None],
                 address: str = "127.0.0.1",
                 port: int = 80,
                 requests_queued: int = 10):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((address, port))
    serversocket.listen(requests_queued)
    while True:
        (client_socket, _) = serversocket.accept()
        handler(client_socket)


def udp_listener(handler: Callable[[socket.socket], None],
                 address: str = "127.0.0.1",
                 port: int = 80):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((address, port))
    while True:
        handler(sock)
