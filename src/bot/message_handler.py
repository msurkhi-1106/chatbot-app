from agent import Agent
from ipc.ipc_message import IPCMessage
from ipc.ipc_pipe import IPCPipe
from ipc.ipc_message_handler import IPCMessageHandler

class MessageHandler(IPCMessageHandler):
    def __init__(self, agent: Agent):
        self.agent = agent

    def handle_message(self, ipc_pipe: IPCPipe, message: IPCMessage):
        if (message.type == 1): # AGENT_QUERY
            ipc_pipe.send_message(IPCMessage(0, "heyyy", message.id))