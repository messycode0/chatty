import socket

HOST = 'localhost'                  # replace with the IP address of your computer
PORT = 8000                        # replace with the port number your server is listening on

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send a message to the server
# message = 'Hello, server!'
# client_socket.sendall(message.encode('utf-8'))

while True:
    message = input('Enter a message: ')
    client_socket.sendall(message.encode('utf-8'))
    if message == 'exit':
        break

# Receive a response from the server
response = client_socket.recv(1024).decode('utf-8')
print(f'Received response: {response}')

# Close the socket connection
client_socket.close()
