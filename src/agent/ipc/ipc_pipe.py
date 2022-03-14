import json
import os
import select
from ipc.ipc_message_handler import IPCMessageHandler

from ipc.ipc_message import IPCMessage

POLL_DELAY_MS = 10

class IPCPipe:
    def __init__(self, pipe_name_r, pipe_name_w):
        try:
            self.fifo_r = os.open(pipe_name_r, os.O_RDONLY, os.O_NONBLOCK)
            print('Read pipe ready')
            while True:
                try:
                    self.fifo_w = os.open(pipe_name_w, os.O_WRONLY)
                    print('Write pipe ready')
                    break
                except Exception as ex:
                    print(ex)
                    pass
        except:
            os.close(self.fifo_r)

    def get_message(self) -> IPCMessage:
        return IPCMessage.deserialize(os.read(self.fifo_r, 64000)) 

    def send_message(self, type: int, body: str = None, id: str = None):
        os.write(self.fifo_w, IPCMessage(type, body, id).serialize())

    def poll(self, message_handler: IPCMessageHandler):
        try:
            poll = select.poll()
            poll.register(self.fifo_r, select.POLLIN)
            
            while True:
                if (self.fifo_r, select.POLLIN) in poll.poll(POLL_DELAY_MS):
                    msg = self.get_message()
                    message_handler.handle_message(self, msg)

        finally:
            poll.unregister(self.fifo_r)
            os.close(self.fifo_r)