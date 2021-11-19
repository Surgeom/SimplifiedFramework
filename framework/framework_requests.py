# GET
class GetRequests:
    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split("&")
            for item in params:
                k, v = item.split("=")
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        query_string = environ["QUERY_STRING"]
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


# POST
class PostRequests:
    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split("&")
            for item in params:
                k, v = item.split("=")
                result[k] = v
        return result

    def get_wsgi_input_data(self, environ) -> bytes:
        content_len_data = environ["CONTENT_LENGTH"]
        content_len_data = int(content_len_data) if content_len_data else 0
        data = environ['wsgi.input'].read(content_len_data) if content_len_data > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode('utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
