import os
import select

POLL_DELAY_MS = 10

class IPCPipe:
    def __init__(self, pipe_name_r, pipe_name_w):
        print("ye")
        try:
            print('try')
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

            print("NAH")
            os.close(self.fifo_r)

    def get_message(self):
        return os.read(self.fifo_r, 1024).decode('utf-8')

    def poll(self):
        try:
            poll = select.poll()
            poll.register(self.fifo_r, select.POLLIN)
            
            while True:
                if (self.fifo_r, select.POLLIN) in poll.poll(POLL_DELAY_MS):
                    msg = self.get_message()
                    print(msg)
                    os.write(self.fifo_w, "Hello brooo!".encode("utf-8"))

        finally:
            poll.unregister(self.fifo_r)
            os.close(self.fifo_r)

                

    