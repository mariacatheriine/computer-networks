import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input("Enter a message (or stop): ")
    if message.lower() == "stop":
        client.sendto(message.encode(), ('localhost', 1234))
        break
    client.sendto(message.encode(), ('localhost', 1234))
    data, addr = client.recvfrom(1024)
    print("Current Server Time: ", data.decode())
client.close()