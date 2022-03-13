from agent import Agent
from ipc.ipc_message import IPCMessage
from ipc.ipc_pipe import IPCPipe
from ipc.ipc_message_handler import IPCMessageHandler

class MessageHandler(IPCMessageHandler):
    def __init__(self, agent: Agent):
        self.agent = agent

    def handle_message(self, ipc_pipe: IPCPipe, message: IPCMessage):
        if (message.type == "agent-query"):
            ipc_pipe.send_message(IPCMessage("agent-response", "heyyy"))