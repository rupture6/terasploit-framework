import socket

class SockType:
    def get(kind) -> socket:
        ST = {
            'SOCK_STREAM' : socket.SOCK_STREAM,
            'SOCK_DGRAM' : socket.SOCK_DGRAM,
            'SOCK_RAW' : socket.SOCK_RAW,
            'SOCK_RDM' : socket.SOCK_RDM,
            'SOCK_SEQPACKET' : socket.SOCK_SEQPACKET,
            'SOCK_NONBLOCK' : socket.SOCK_NONBLOCK,
            'SOCK_CLOEXEC' : socket.SOCK_CLOEXEC,
        }
        return ST[kind.upper()]