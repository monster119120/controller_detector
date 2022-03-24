import socketserver
from typing import Any
from encode_decode import encode_dict, decode_dict


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
        conn.sendall(encode_dict({'i am controller': 0}))
        while True:
            # TODO 接收detector的状态信息
            recv_state_dict = decode_dict(conn.recv(115200))
            print(recv_state_dict)
            
            # TODO 更新controller_state
            self.update_state_table(recv_state_dict)
            
            action = self.get_action()
            conn.sendall(encode_dict(action))


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), Controller)
    server.serve_forever()
