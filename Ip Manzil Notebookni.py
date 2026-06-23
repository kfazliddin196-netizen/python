import socket
h = socket.gethostname()
ip_address = socket.gethostbyname(h)
print("Sizning IP manzilingiz:", ip_address)