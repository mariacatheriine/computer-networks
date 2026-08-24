import socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2525))
server.listen(5)
print("SMTP server is listening...")
while True:
    conn, addr = server.accept()
    print("Connected: ", addr)
    conn.send(b"220 Simple SMTP Server\r\n")
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break
        print("Client: ", data)
        if data.upper().startswith("HELO"):
            conn.send(b"250 Hello\r\n")
        elif data.upper().startswith("MAIL FROM:"):
            conn.send(b"250 Sender accepted\r\n")
        elif data.upper().startswith("RCPT TO:"):
            conn.send(b"250 Recipient accepted\r\n")
        elif data.upper() == "DATA":
            conn.send(b"354 Start mail input; end with <END>\r\n")
            message = conn.recv(1024).decode().strip()
            print("\nEmail Message:")
            print(message)
            conn.send(b"250 Message accepted\r\n")
        elif data.upper() == "QUIT":
            conn.send(b"221 Bye\r\n")
            break
        else:
            conn.send(b"500 Command not recognized\r\n")
    conn.close()