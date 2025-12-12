from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from chatmate_details.gui.message_widget import MessageWidget


class MessageListWidget(QScrollArea):
    def __init__(self, messages):
        super().__init__()
        self.setWidgetResizable(True)

        container = QWidget()
        layout = QVBoxLayout(container)

        for message in messages:
            layout.addWidget(MessageWidget(message))

        layout.addStretch()
        self.setWidget(container)
        self.setMinimumHeight(600)
        self.setMaximumWidth(600)
