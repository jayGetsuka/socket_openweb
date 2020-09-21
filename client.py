import socket
server_ip = 'IP Address'
port = 5000

while True:
    data = input("Message to server (example: https://www.???.com/ or namewebsite ): ")
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((server_ip,port))

    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print("Message From server: ", data_server)
    server.close()
