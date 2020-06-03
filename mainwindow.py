# coding: utf-8

from PyQt5.QtWidgets import QMainWindow

from Ui_mainwindow import Ui_MainWindow

from plib.camera import Camera, CameraControler
from plib.video import Video



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        camera = Camera(0)        
        camera.set_preview(self.v_video)
        self.camera_controler = CameraControler(camera)
        self.pb_start.clicked.connect(self._on_pb_start_clicked)

    def _on_pb_start_clicked(self):
        self.camera_controler.start()