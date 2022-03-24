import socket
import time
import multiprocessing
from multiprocessing import Process
from encode_decode import encode_dict, decode_dict


class Detector:
    """
    单个detector
    """
    def __init__(self, index):
        self.detector_state = {}    # detector_state记录了当前单个detector的各种信息
        self.detector_state.update({'detector_id': index})

    def update_state(self):
        """
        更新self.detector_state
        """
        # TODO
        return

    def run(self):
        sk = socket.socket()
        sk.connect(('127.0.0.1', 8009))
        
        while True:
            # TODO 接收controller的控制信号
            msg = decode_dict(sk.recv(115200))
            print(msg)
            
            # TODO 更新自己的状态信息
            self.update_state()
            
            # TODO 返回当前状态信息
            sk.send(encode_dict(self.detector_state))
            time.sleep(2)
        
        sk.close()


def detector_run(detector):
    detector.run()


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    detector_num = 3
    detectors = [Process(target=detector_run, args=(Detector(i),)) for i in range(detector_num)]
    
    for detector in detectors:
        detector.start()
    
    for detector in detectors:
        detector.join()



