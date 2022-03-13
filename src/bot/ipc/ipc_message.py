import json
import string
import uuid

class IPCMessage():
    type: str
    body: any
    id: str

    def __init__(self, type: str, body: any = None, id: str = str(uuid.uuid4())):
        self.type = type
        self.body = body
        self.id = id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)