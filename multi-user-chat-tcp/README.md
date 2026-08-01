# Multi-Client Chat Application

Multiple clients connect to a TCP server and exchange messages; the server broadcasts each incoming message to all other connected clients using threads.

**Concepts:** TCP sockets, multithreading, broadcast messaging

## Files
- `mc_server.py` — accepts multiple client connections, broadcasts messages to all clients except the sender
- `mc_client.py` — connects to server, sends messages, and listens for incoming messages in a separate thread

## Run
```bash
python3 mc_server.py     # start first
python3 mc_client.py     # run in multiple terminals to simulate multiple clients
```

Type a message and press Enter to send. Type `exit` to disconnect.