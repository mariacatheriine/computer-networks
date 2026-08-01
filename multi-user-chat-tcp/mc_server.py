import socket, threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9022))
server.listen()
clients = []
print("SERVER IS WAITING...")
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                if client in clients:
                    clients.remove(client)
                client.close()
def handle(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            broadcast(data, client)
        except Exception as e:
            print("ERROR:", e)
            break
    if client in clients:
        clients.remove(client)
    client.close()
while True:
    client, addr = server.accept()
    print("CONNECTED: ", addr)
    clients.append(client)
    threading.Thread(target = handle, args = (client,), daemon = True).start()