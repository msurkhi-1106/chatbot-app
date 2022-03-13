import os
import select
import sys
import auto_flush
from agent import Agent
from message_handler import MessageHandler

from ipc.ipc_pipe import IPCPipe

path_fifo_r = sys.argv[1] #read pipe path
path_fifo_w = sys.argv[2] #write pipe path

agent = Agent()
message_handler = MessageHandler(agent)

pipe = IPCPipe(path_fifo_r, path_fifo_w)
pipe.poll(message_handler)