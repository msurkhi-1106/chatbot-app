import os
import select
import sys
import auto_flush
from agent import Agent
from message_handler import MessageHandler

from ipc.ipc_pipe import IPCPipe

socket_address = sys.argv[1]

agent = Agent()
message_handler = MessageHandler(agent)

pipe = IPCPipe(socket_address, message_handler)