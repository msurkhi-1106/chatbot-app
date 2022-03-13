import os
import select
import sys
import auto_flush

from ipc_pipe import IPCPipe

print(sys.argv)
pipe = IPCPipe(sys.argv[1], sys.argv[2])
pipe.poll()