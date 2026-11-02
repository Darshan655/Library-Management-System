"""
Library Management System - Web Application Server
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from library import Library

# Initialize the library with sample books
library = Library()
library.add_book(101, "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book(102, "To Kill a Mockingbird", "Harper Lee")
library.add_book(103, "1984", "George Orwell")

class LibraryHTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/" or path == "/health":
            self._send_json({
                "service": "Library Management System",
                "status": "Running",
                "version": "1.0.0",
                "endpoints": [
                    "/",
                    "/books",
                    "/search?q=<title_or_keyword>",
                    "/health"
                ]
            })
        elif path == "/books":
            books = [{
                "book_id": b.book_id,
                "title": b.title,
                "author": b.author,
                "available": b.available
            } for b in library.list_books()]
            self._send_json({"count": len(books), "books": books})
        elif path == "/search":
            q = query.get("q", [""])[0]
            matched = library.search_by_title(q)
            results = [{
                "book_id": b.book_id,
                "title": b.title,
                "author": b.author,
                "available": b.available
            } for b in matched]
            self._send_json({"query": q, "count": len(results), "results": results})
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

    def log_message(self, format, *args):
        print(f"[Library Server] {self.address_string()} - {format % args}")

def run(host="0.0.0.0", port=5000):
    server = HTTPServer((host, port), LibraryHTTPRequestHandler)
    print(f"Library Management Server running at http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("Server stopped.")

if __name__ == "__main__":
    run()
