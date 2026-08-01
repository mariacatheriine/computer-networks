import socket, threading 
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 9022))
name = input("Enter your name: ")
def receive():
    while True:
        try:
            msg = c.recv(1024).
            if not msg:
                break
            print(msg.decode())
        except:
            break
threading.Thread(target = receive, daemon = True).start()
while True:
    msg = input()
    if msg.lower() == 'exit':
        break
    try:
        c.send(f"{name}: {msg}".encode())
    except:
        break
    c.close()