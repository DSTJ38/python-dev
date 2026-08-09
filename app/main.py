from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

server = ThreadingHTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)

print("Python container running at http://localhost:8000")
server.serve_forever()
