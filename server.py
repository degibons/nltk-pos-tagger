from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json
from app import tag

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'text': 'Send me english text via POST to tag (just like this one).'}).encode())
        
    # POST echoes the message adding a JSON field
    def do_POST(self):           
        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(length)
        fields = parse_qs(str(field_data,"UTF-8"))
        
        text = fields['text'][0]
        tagged_text = tag(text)

        jsonResult = json.dumps({
            'tagged_text': tagged_text
        })
        
        # send the message back
        self._set_headers()
        self.wfile.write(jsonResult.encode())
        
def run(server_class=HTTPServer, handler_class=Server, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()