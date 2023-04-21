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
        
        if message == 'connection132':
            print(f'New connection from {client_address[0]}:{client_address[1]}')
        elif message == 'exit':
            print(f'Client [{client_address[0]}:{client_address[1]}] has disconnected')
        elif message == 'e':
            print(f'Client [{client_address[0]}:{client_address[1]}] has disconnected and told the server to shutdown... bye')
            # tell all clients to disconnect
            client_socket.sendall("disconnect".encode('utf-8'))


            server_socket.close()

            exit(0)
        else:
            print(f'Received message [{client_address[0]}:{client_address[1]}]: {message}')
        

        # Echo the message back to the client
        client_socket.sendall(message.encode('utf-8'))

    # Close the client socket
    client_socket.close()
