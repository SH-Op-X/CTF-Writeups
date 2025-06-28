# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: main.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from xianyu_decrypt import load_and_decrypt_xianyu

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fish Player - 鱼音乐🐟')
        self.resize(600, 400)
        self.player = QMediaPlayer(self)
        self.open_button = QPushButton('打开 .xianyu 文件')
        self.open_button.clicked.connect(self.open_xianyu)
        self.cover_label = QLabel('专辑封面展示')
        self.cover_label.setScaledContents(True)
        self.cover_label.setFixedSize(300, 300)
        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        layout.addWidget(self.cover_label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_xianyu(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择 .xianyu 文件', '', 'Xianyu Files (*.xianyu)')
        if not file_path:
            return
        try:
            info = load_and_decrypt_xianyu(file_path)
            meta = info['meta']
            cover_path = info['cover_path']
            audio_path = info['audio_path']
            if cover_path and os.path.exists(cover_path):
                pixmap = QPixmap(cover_path)
                self.cover_label.setPixmap(pixmap)
            else:
                self.cover_label.setText('无封面')
            url = QUrl.fromLocalFile(audio_path)
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            name = meta.get('name', '未知')
            artist = meta.get('artist', '未知歌手')
            fl4g = meta.get('fl4g', 'where_is_the_flag?')
            FLAG = meta.get('')
            QMessageBox.information(self, '🐟音乐提示您', f'正在播放：{name}\n歌手：{artist}\nfl4g:{fl4g}\nFLAG:{FLAG}')
        except Exception as e:
            QMessageBox.critical(self, '错误', str(e))

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()