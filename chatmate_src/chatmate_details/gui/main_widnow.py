from PyQt6.QtWidgets import QWidget, QHBoxLayout

from chatmate_details.gui.girl_list_widget import GirlListWidget
from chatmate_details.gui.qt_utils import QtUtils


class MainWindow(QWidget):
    def __init__(self, chats_info_view):
        super().__init__()
        self.setGeometry(100, 100, 400, 500)
        QtUtils.center(self)

        girls_list = GirlListWidget(chats_info_view)
        main_layout = QHBoxLayout()
        main_layout.addWidget(girls_list)
        self.setLayout(main_layout)