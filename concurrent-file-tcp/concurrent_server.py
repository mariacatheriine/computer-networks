import socket, multiprocessing, os
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(5)
print("SERVER IS LISTENING...")
def handle_client(conn, addr):
    print("Connected: ", addr)
    filename = conn.recv(1024).decode()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = f.read()
        message = f"Server PID: {os.getpid()}\nFile Content:\n{data}"
    else:
        message = f"Server PID: {os.getpid()}\nFile '{filename}' not found"
    conn.send(message.encode())
    conn.close()
while True:
    conn, addr = server.accept()
    p = multiprocessing.Process(target = handle_client, args = (conn, addr))
    p.start()
    conn.close()