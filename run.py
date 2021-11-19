from wsgiref.simple_server import make_server
from framework.main import SimWsgiFW
from urls import routes

app = SimWsgiFW(routes)

with make_server("", 8000, app) as httpd:
    print("startserver")
    httpd.serve_forever()
