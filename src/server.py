import socket

HOST = 'localhost'  # the hostname or IP address of your computer
PORT = 8000        # the port number to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'Server is listening on {HOST}:{PORT}')

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()

    #print(f'New connection from {client_address[0]}:{client_address[1]}')

    # Handle messages from the client
    while True:
        # Receive a message from the client
        message = client_socket.recv(1024).decode('utf-8')
        
        if not message:
            # The client has disconnected
            break
        
        print(f'Received message [{client_address[0]}:{client_address[1]}]: {message}')

        # Echo the message back to the client
        client_socket.sendall("Hello, client!".encode('utf-8'))

    # Close the client socket
    client_socket.close()
