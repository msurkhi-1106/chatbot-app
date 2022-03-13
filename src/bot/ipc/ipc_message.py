import json

class IPCMessage():
    type: str
    body: any

    def __init__(self, type: str, body: any = None):
        self.type = type
        self.body = body

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)