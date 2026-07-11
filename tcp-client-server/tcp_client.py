import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("", 9000))

n = int(input("Enter the order of matrix: "))
matrix = [[0 for j in range(n)] for i in range(n)]
matrix_type = input("Enter the type of matrix (upper, lower, diagonal,normal): ")

if matrix_type == "upper":
    for i in range(n):
        for j in range(n):
            if j >= i:
                matrix[i][j] = int(input("Enter element: "))
            else:
                matrix[i][j] = 0
elif matrix_type == "lower":
    for i in range(n):
        for j in range(n):
            if j <= i:
                matrix[i][j] = int(input("Enter element: "))
            else:
                matrix[i][j] = 0
elif matrix_type == "diagonal":
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = int(input("Enter element: "))
            else:
                matrix[i][j] = 0
else:
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(input("Enter element: "))

print("Matrix:\n")
for row in matrix:
    print(*row)

data = (n, matrix)
client.send(pickle.dumps(data))

result = client.recv(1024).decode()
print("Matrix Type: ", result)

client.close()