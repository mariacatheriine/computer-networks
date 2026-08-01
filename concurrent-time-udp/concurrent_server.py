import socket, threading, time
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 1234))
print("SERVER IS WAITING...")
def handle_request(data, addr):
    message = data.decode()
    print(f"Received message from {addr}: {message}")
    if message.lower() == "stop":
        return
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    server.sendto(current_time.encode(), addr)
while True:
    data, addr = server.recvfrom(1024)
    threading.Thread(target=handle_request, args=(data, addr), daemon=True).start()
server.close()