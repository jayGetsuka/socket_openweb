import socket
import webbrowser

my_ip = 'IP Address'
port = 5000
while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.bind((my_ip, port))
    server.listen(1)

    print("waiting for client....")

    client, addr = server.accept()
    print("Connect From: ", str(addr))

    data = client.recv(1024).decode('utf-8')
    print("Message From client: ", data)

    try:
        webbrowser.open(str(data))
        send_text = data
    except:
        send_text = "Somethings Error..."

        
    client.send(send_text.encode('utf-8'))
    client.close()
    