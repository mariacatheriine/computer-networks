import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))
filename = input("Enter filename: ")
client.send(filename.encode())
response = client.recv(4096).decode()
print("Response from server:\n", response)
client.close()