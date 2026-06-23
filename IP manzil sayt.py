import socket

# Get the website address from the user
address = input("Enter the website address: ")

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the website
sock.connect((address, 80))  # Assuming the website is using HTTP on port 80

# Send a request to the website
request = "GET /HTTPS/ HTTP/1.1\r\nHost: " + address + "\r\n\r\n"
sock.send(request.encode())

# Receive and print the response
response = sock.recv(4096)
print(response.decode())

# Close the socket
sock.close()