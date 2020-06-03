# coding: utf-8


import cv2 
import numpy as np

from PyQt5.QtCore import QObject, QThread, pyqtSignal

CAMERA_NOMERA      = (0)
CAMERA_READ_FAILD  = (1)
CAMERA_WITHOUT_CAP = (2)
CAMERA_WITHOUT_DEV = (3) 
CAMEAR_EXIT        = (4)


class Camera(QObject):
    send_frame = pyqtSignal(np.ndarray)
    send_code = pyqtSignal(int)

    def __init__(self, dev_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dev_id = dev_id
        self.cap = None
        self.activatable = True
        self.interval = 30
        self.preview_list = set()

    def work(self):
        self.cap = cv2.VideoCapture(self.dev_id)
        while self.activatable:
            if self.cap is not None and self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    self.send_frame.emit(frame)
                else:
                    self.end_code.emit(CAMERA_READ_FAILD)
            else:
                self.send_code.emit(CAMERA_WITHOUT_CAP)
            QThread.msleep(self.interval)
        self.send_code.emit(CAMEAR_EXIT)

    def set_preview(self, pre_view):
        self.preview_list.add(pre_view)
        self.send_frame.connect(pre_view.on_display)

    def del_preview(self, pre_view):
        self.send_frame.disconnect(pre_view)
        self.preview_list.discard(pre_view)

    def set_status(self, code):
        pass

    def __del__(self):
        self.activatable=False


class CameraControler(QObject):

    def __init__(self, camera, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.thread = QThread()
        self.camera = camera
        self.camera.moveToThread(self.thread)
        self.thread.started.connect(self.camera.work)
        self.thread.finished.connect(self.camera.deleteLater)

    def __del__(self):
        self.thread.quit()
        self.thread.wait()
    
    def start(self):
        if not self.thread.isRunning():
            self.thread.start()


  


    
