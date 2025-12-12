from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QListWidgetItem

from chatmate_details import gui
from chatmate_details.gui.girl_item_widget import GirlItemWidget
from chatmate_details.gui.girl_chat_window import GirlChatWindow


class GirlListWidget(QListWidget):
    def __init__(self, chats_info_view):
        super().__init__()
        self.chats_info_view = chats_info_view
        self.itemClicked.connect(self.on_item_clicked)
        for chat_info_view in chats_info_view:
            self.add_girl(chat_info_view)

    def add_girl(self, chat_info_view):
        item = QListWidgetItem(self)
        widget = GirlItemWidget(chat_info_view)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)
        item.setData(Qt.ItemDataRole.UserRole, chat_info_view['name'])

    def on_item_clicked(self, item):
        main_window = self.parent()
        index = self.row(item)
        chat_info_view = self.chats_info_view[index]
        event = {
            'name': 'get_chat',
            'context': {
                'user_id': chat_info_view['id']
            }
        }
        chat = gui.event_controller.handle_event(event)
        self.chat_window = GirlChatWindow(chat)
        main_window.hide()
        self.chat_window.exec()
        main_window.show()