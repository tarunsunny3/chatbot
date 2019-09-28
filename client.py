import socket
host = "10.5.1.15"
port = 5000
client_socket = socket.socket()
client_socket.connect((host, port))
message = input(" -> ")
while message.lower().strip() != 'bye':
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    print("Received data from server: " + data)
    message = input(" -> ")
client_socket.close()
