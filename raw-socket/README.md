# Raw Socket Packet Sniffer

Captures raw TCP packets arriving on the network interface and prints the sender address, packet length, and raw byte content.

**Concepts:** Raw sockets, packet capture

## Files
- `raw_socket.py` — opens a raw TCP socket and continuously captures incoming packets

## Run
Raw sockets require root privileges:
```bash
sudo python3 raw_socket.py
```
