import socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
print("PACKET CAPTURING STARTED...")
while True:
    packet, addr = s.recvfrom(65565)
    print("Packet received from: ", addr)
    print("Packet length: ", len(packet))
    print(packet)