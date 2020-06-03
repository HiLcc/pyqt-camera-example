# coding； utf-8 

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap


class Video(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(64, 48)
        self.setScaledContents(True)

    def on_display(self, cv_image):
        if cv_image is not None:
            h, w, c = cv_image.shape
            qimage = QImage(cv_image.data, w, h, c*w, QImage.Format_RGB888)
            qpixmap = QPixmap.fromImage(qimage)
            self.setPixmap(qpixmap)
            # self.connectNotify(True)
