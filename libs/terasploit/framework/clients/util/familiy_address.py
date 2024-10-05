import socket

class AddrFam:
    
    @staticmethod
    def get(family) -> socket:
        AF = {
            'AF_UNSPEC' : socket.AF_UNSPEC,
            'AF_UNIX' : socket.AF_UNIX,
            'AF_INET' : socket.AF_INET,
            'AF_AX25' : socket.AF_AX25,
            'AF_IPX' : socket.AF_IPX,
            'AF_APPLETALK' : socket.AF_APPLETALK,
            'AF_NETROM' : socket.AF_NETROM,
            'AF_BRIDGE' : socket.AF_BRIDGE,
            'AF_ATMPVC' : socket.AF_ATMPVC,
            'AF_X25' : socket.AF_X25,
            'AF_INET6' : socket.AF_INET6,
            'AF_ROSE' : socket.AF_ROSE,
            'AF_NETBEUI' : socket.AF_NETBEUI,
            'AF_SECURITY' : socket.AF_SECURITY,
            'AF_KEY' : socket.AF_KEY,
            'AF_NETLINK' : socket.AF_NETLINK,
            'AF_ROUTE' : socket.AF_ROUTE,
            'AF_PACKET' : socket.AF_PACKET,
            'AF_ASH' : socket.AF_ASH,
            'AF_ECONET' : socket.AF_ECONET,
            'AF_ATMSVC' : socket.AF_ATMSVC,
            'AF_RDS' : socket.AF_RDS,
            'AF_SNA' : socket.AF_SNA,
            'AF_IRDA' : socket.AF_IRDA,
            'AF_PPPOX' : socket.AF_PPPOX,
            'AF_WANPIPE' : socket.AF_WANPIPE,
            'AF_LLC' : socket.AF_LLC,
            'AF_CAN' : socket.AF_CAN,
            'AF_TIPC' : socket.AF_TIPC,
            'AF_BLUETOOTH' : socket.AF_BLUETOOTH,
            'AF_ALG' : socket.AF_ALG,
            'AF_VSOCK' : socket.AF_VSOCK,
            'AF_QIPCRTR' : socket.AF_QIPCRTR
        }
        return AF[family.upper()]