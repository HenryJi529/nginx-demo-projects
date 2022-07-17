import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8000))
s.listen(5)
print("Server started...")

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientSocket.send(bytes("""HTTP/1.1 200 OK
Content-Type: text/html\n
Hello World
""", "utf-8"))
    clientSocket.close()