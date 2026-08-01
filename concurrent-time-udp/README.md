# UDP Concurrent Time Server 

Client sends a request to the server over UDP; server responds with the current date and time. Server handles each incoming request in a separate thread.

**Concepts:** UDP sockets, multithreading, client-server model

## Files
- `concurrent_server.py` — listens for requests, sends back current server time, stops on "stop" message
- `concurrent_client.py` — sends a message to the server and prints the returned time

## Run
```bash
python3 concurrent_server.py     # start first
python3 concurrent_client.py     # then run this, enter a message or "stop"
```