import pyrogram.client as cl
from pyrogram.api import functions
import textwrap
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlparse,parse_qs
class HelloRequestHandler(BaseHTTPRequestHandler):





    global client,api_id,api_hash
    client = cl.Client(session_name="authSesion")
#client.send(functions.auth.ResetAuthorizations(126646))
    client.start()


    api_id=181231;
    api_hash="5a04c93c08f345a9574c8bdcfbe0de9b";



    #client.send(functions.auth.SendCode(phoneNumber,api_id,api_hash,True,True))

    def do_GET(self):

        if str(self.path).startswith('/test'):
            parsed = urlparse(self.path)
            pn=parse_qs(parsed.query)['pn']

            #comm
            code = cl.Client.sc.SendCode(pn[0], api_id, api_hash, True, True);

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(pn[0].encode('utf-8'))



server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()