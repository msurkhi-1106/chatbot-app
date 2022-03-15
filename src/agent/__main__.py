import os
import select
import sys
from plugins.pos_tag import PosTag
from plugins.spellcheck import SpellCheck
import auto_flush
from agent import Agent
from message_handler import MessageHandler

from ipc.ipc_pipe import IPCPipe

socket_address = sys.argv[1]

plugins = [
    SpellCheck,
    PosTag
]

agent = Agent(plugins)
message_handler = MessageHandler(agent)

pipe = IPCPipe(socket_address, message_handler)