import requests
from PyQt6.QtCore import Qt, QByteArray
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout


class GirlItemWidget(QWidget):
    def __init__(self, chat_info_view):
        super().__init__()
        
        layout = QHBoxLayout()
        layout.addWidget(self._create_avatar_label(chat_info_view))
        layout.addWidget(QLabel(chat_info_view['name']))
        layout.addWidget(self.__create_message_hint_label(chat_info_view))
        layout.addWidget(QLabel(chat_info_view['is_answered_status_icon']))

        layout.addStretch()
        
        self.setLayout(layout)

    def _create_avatar_label(self, chat_info_view):
        size = 200
        avatar_label = QLabel()
        avatar_label.setFixedSize(size, size)

        if 'avatar_url' in chat_info_view and chat_info_view['avatar_url']:
            response = requests.get(chat_info_view['avatar_url'])
            image_data = QByteArray(response.content)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap = pixmap.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio)
        else:
            pixmap = QPixmap(size, size)
            pixmap.fill(QColor(0, 100, 0))

        avatar_label.setPixmap(pixmap)
        return avatar_label

    def __create_message_hint_label(self, chat_info_view):
        label = QLabel(chat_info_view['last_message_hint'])
        return label