import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter sentence: ")
client.sendto(message.encode(), ("", 9000))
data, addr = client.recvfrom(1024)
print("Translated sentence:", data.decode())
client.close()