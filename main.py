from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        with open("contacts.html", "r", encoding="utf-8") as file:
            page_content = file.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(page_content, "utf-8"))

    def do_POST(self):
        content_lenght = int(self.headers["Content-Length"])
        body = self.rfile.read(content_lenght)
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")