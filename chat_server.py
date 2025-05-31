import socket             # Import the socket library for networking
import threading          # Import threading to handle multiple clients simultaneously

# Server configuration
PORT = 12345              # Port number the server will listen on
SERVER = socket.gethostbyname(socket.gethostname())  # Get the IP address of the current machine
ADDRESS = (SERVER, PORT)  # Combine IP and port into one address tuple
FORMAT = "utf-8"          # Encoding format for messages
BYTESIZE = 1024           # Maximum number of bytes to receive at once
DISCONNECT_MESSAGE = "quit"  # Message to indicate disconnection

# Create a TCP socket (SOCK_STREAM = TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the address (IP, port)
server.bind(ADDRESS)

# Function to handle each connected client
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")  # Log connection
    client_socket.send("You are connected to the server.".encode(FORMAT))  # Welcome message

    connected = True  # Connection state
    while connected:
        try:
            message = client_socket.recv(BYTESIZE).decode(FORMAT)  # Receive message
            if message == DISCONNECT_MESSAGE:  # Check for quit signal
                print(f"[DISCONNECTED] {client_address} disconnected.")  # Log disconnection
                client_socket.send(DISCONNECT_MESSAGE.encode(FORMAT))  # Acknowledge quit
                connected = False  # End loop
            else:
                print(f"[{client_address}] {message}")  # Print client message
                response = input("Server: ")  # Input response from server operator
                client_socket.send(response.encode(FORMAT))  # Send response to client
        except ConnectionResetError:
            print(f"[ERROR] Connection with {client_address} lost unexpectedly.")  # Handle errors
            break

    client_socket.close()  # Close client socket

# Start listening for clients
server.listen()  # Begin listening for connections
print(f"[STARTED] Server is running on {SERVER}:{PORT}")  # Print server status

# Accept clients in a loop
try:
    while True:
        client_socket, client_address = server.accept()  # Accept new connection
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))  # Start thread
        thread.start()  # Begin client handler
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # Show connection count
except KeyboardInterrupt:
    print("\n[SHUTDOWN] Server is shutting down...")  # Handle Ctrl+C clean shutdown
finally:
    server.close()  # Ensure socket is closed
