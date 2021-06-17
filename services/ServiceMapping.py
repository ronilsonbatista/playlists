import requests

class ServiceHandler:
    endpoint = ""
    payload = {}

    def get(self, **kwargs):
        req = requests.get(self.endpoint, params=self.payload)
        return req.json()


class BookServiceHandler(ServiceHandler):
    endpoint = "http://localhost:12300/api/book"

    def __init__(self, **kwargs):
        self.endpoint = f"{self.endpoint}"

if __name__ == "__main__":
    csh = BookServiceHandler()
    print(csh.get())