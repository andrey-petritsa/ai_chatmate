from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout


class MessageWidget(QWidget):
    def __init__(self, message):
        super().__init__()

        self.text_label = self.__get_text_label(message)
        layout = QHBoxLayout()
        if message['position'] == 'right':
            layout.setContentsMargins(100, 0, 0, 0)
        layout.addWidget(self.text_label)

        self.setLayout(layout)

    def __get_text_label(self, message):
        text_label = QLabel(message['name'] + '\n' + message['text'])
        text_label.setWordWrap(True)
        text_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        text_label.setStyleSheet("color: white; font-size: 12px;")
        return text_label