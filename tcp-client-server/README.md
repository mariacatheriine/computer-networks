# TCP Client-Server: Matrix Type Classification
 
Client sends a square matrix to the server over TCP; server classifies it as Upper Triangular, Lower Triangular, Diagonal, or Normal, and sends the result back.
 
**Concepts:** TCP sockets, client-server model, serialization with `pickle`
 
## Files
- `tcp_server.py` — receives matrix, classifies it, sends result
- `tcp_client.py` — takes matrix input, sends to server, prints result

## Run
```bash
python3 tcp_server.py     # start first
python3 tcp_client.py     # then run this, enter matrix when prompted
```
