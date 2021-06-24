import requests
import sys, json

class ServiceHandler:
    endpoint = ""
    payload = {}

    def get(self, **kwargs):
        req = requests.post(self.endpoint, params=self.payload)
    
        print("reeep", self.endpoint)
        return req.json()

class BookServiceHandler(ServiceHandler):
    endpoint = "http://localhost:12300/api/lista/livros"

    def __init__(self, **kwargs):
        self.endpoint = f"{self.endpoint}"

if __name__ == "__main__":
    csh = BookServiceHandler()
    print(csh.get())

