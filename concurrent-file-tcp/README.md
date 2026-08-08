# Concurrent File Server

Client requests a file by name from the server over TCP; server reads the file and returns its content along with the handling process's PID. Each client connection is handled in a separate process.

**Concepts:** TCP sockets, multiprocessing, file I/O

## Files
- `concurrent_server.py` — listens for connections, spawns a new process per client, reads and returns requested file content
- `concurrent_client.py` — sends a filename to the server and prints the response

## Run
```bash
python3 concurrent_server.py     # start first
python3 concurrent_client.py     # then run this, enter a filename to fetch
```