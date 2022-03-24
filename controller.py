import socketserver
import time
from multiprocessing import Queue
from typing import Any
from encode_decode import encode_dict, decode_dict
import numpy as np


class Controller(socketserver.BaseRequestHandler):
    """
    作为Controller，监视所有的detector
    """
    def __init__(self, request: Any, client_address: Any, server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.controller_state = {}   # 把所有detector的detector_state更新到自己的controller_state中

    def update_state_table(self, state_dict):
        """
        从detector接收到的state_dict，更新到self.controller_state中去
        :param state_dict: 从detector接收到的detector_state
        """
        # TODO
        pass

    def get_action(self):
        """
        根据当前的self.controller_state，对所有的detector进行控制
        """
        # TODO
        return {}

    def handle(self):
        conn = self.request
        interval = 0.5
        t = time.time()

        while True:
            # TODO 接收detector的状态信息
            recv_dict = decode_dict(conn.recv(115200))
            
            # TODO 更新controller_state
            self.update_state_table(recv_dict)
            send_dict = self.get_action()

            if time.time() - t >= interval:
                send_dict.update({'img': np.zeros(shape=(28, 28)).tolist()})
                t = time.time()
            conn.sendall(encode_dict(send_dict))


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), Controller)
    server.serve_forever()
