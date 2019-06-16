import socket
socket.setdefaulttimeout(3)

def check_ip_port(host,port):
    ip = socket.getaddrinfo(host, None)[0][4][0]
    if ':' in ip:
        inet = socket.AF_INET6
    else:
        inet = socket.AF_INET
    sock = socket.socket(inet)
    status = sock.connect_ex((ip,int(port)))
    sock.close()
    return status == 0

