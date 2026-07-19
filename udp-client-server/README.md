# UDP Client-Server: New Generation Slang Translation
 
Client sends a new generation slang sentence to the server over UDP; server translates it to full sentence, and sends the result back.
 
**Concepts:** UDP sockets, client-server model
 
## Files
- `udp_server.py` — receives slang sentence, translates it, sends result
- `udp_client.py` — takes slang input, sends to server, prints result

## Run
```bash
python3 udp_server.py     # start first
python3 udp_client.py     # then run this, enter matrix when prompted
```
