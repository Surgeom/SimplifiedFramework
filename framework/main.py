from .framework_requests import GetRequests, PostRequests
import quopri


class PageNotFound404:
    def __call__(self,*args,**kwargs):
        return '404 WHAT', '404 PAGE not found'


class SimWsgiFW:
    def __init__(self, routes_obj):
        self.routes_list = routes_obj

    def __call__(self, environ, start_response):
        # get url
        path = environ['PATH_INFO']
        # request
        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == "POST":
            data = PostRequests().get_request_params(environ)
            request["data"] = self.decode_value(data)
            # print(method)
            # print(request["data"])
        if method == "GET":
            requests_params = GetRequests.get_request_params(environ)
            request["request_params"] = requests_params
            print(method)
            print(request["request_params"])

        # add /
        if not path.endswith('/'):
            path = f'{path}/'
        # get controller
        if path in self.routes_list:
            view = self.routes_list[path]()
        else:
            view = PageNotFound404()
        # start controller
        view(request)
        code, body = view()
        start_response(code, [('Content-type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace("%", "=").replace("+", " "), "utf-8")
            val_decode_str = quopri.decodestring(val).decode("utf-8")
            new_data[k] = val_decode_str
        return new_data
