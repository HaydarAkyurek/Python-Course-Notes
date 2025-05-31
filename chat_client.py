import socket  # Import the socket library

# Client configuration
PORT = 12345  # The server's port number
SERVER = socket.gethostbyname(socket.gethostname())  # Get the server's IP (assumes same machine)
ADDRESS = (SERVER, PORT)  # Combine server IP and port
FORMAT = "utf-8"  # Encoding format
BYTESIZE = 1024  # Buffer size for receiving data
DISCONNECT_MESSAGE = "quit"  # Keyword to disconnect from the server

# Create a TCP socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(ADDRESS)  # Connect to the server
    print(f"Connected to server at {ADDRESS}")  # Confirm connection

    while True:
        message = client.recv(BYTESIZE).decode(FORMAT)  # Receive message from server

        if message == DISCONNECT_MESSAGE:  # Check if server wants to disconnect
            print("Server requested disconnection. Disconnecting...")  # Notify user
            client.send(DISCONNECT_MESSAGE.encode(FORMAT))  # Acknowledge
            break  # Exit loop
        else:
            print(f"Server: {message}")  # Show message from server
            user_message = input("You: ")  # Prompt user for input
            client.send(user_message.encode(FORMAT))  # Send message to server

except ConnectionRefusedError:
    print("Connection failed. Is the server running?")  # Handle error if server is down
except KeyboardInterrupt:
    print("\nManual interruption. Closing client...")  # Handle Ctrl+C
    client.send(DISCONNECT_MESSAGE.encode(FORMAT))  # Inform server
finally:
    client.close()  # Always close socket
    print("Client socket closed.")  # Notify user
