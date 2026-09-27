import socket
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 9000))
server.listen(5)
print("SERVER IS WAITING FOR CONNECTION...")

conn, addr = server.accept()
print("CONNECTED BY CLIENT:", addr)

data = pickle.loads(conn.recv(4096))
n, matrix = data

print("Received Matrix:\n")
for row in matrix:
    print(*row)

upper = True
lower = True
diagonal = True

for i in range(n):
    for j in range(n):
        if i > j and matrix[i][j] != 0:
            upper = False
        if i < j and matrix[i][j] != 0:
            lower = False
        if i != j and matrix[i][j] != 0:
            diagonal = False

if upper:
    result = "Upper Triangular Matrix"
elif lower:
    result = "Lower Triangular Matrix"
elif diagonal:
    result = "Diagonal Matrix"
else:
    result = "Normal Matrix"

print("SENDING RESULT TO CLIENT...")
conn.send(result.encode())
conn.close()
server.close()
