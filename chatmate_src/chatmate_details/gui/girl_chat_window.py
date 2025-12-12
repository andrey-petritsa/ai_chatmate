from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt6.QtGui import QPixmap, QColor

from chatmate_details.gui.choice_widget import ChoiceWidget
from chatmate_details.gui.message_list_widget import MessageListWidget
from chatmate_details.gui.qt_utils import QtUtils
import chatmate_details.gui as gui


class GirlChatWindow(QDialog):
    def __init__(self, chat):
        super().__init__()
        self.chat = chat
        self.message_input = None
        self.options = []

        self.setLayout(self.__get_main_layout())

        self.setWindowTitle(f"Чат с {self.chat['name']}")
        self.setGeometry(100, 100, 500, 600)
        self.setMinimumWidth(1200)

    def showEvent(self, event):
        super().showEvent(event)
        QtUtils.center(self)

    def __get_main_layout(self):


        chat_layout = QVBoxLayout()
        chat_layout.addLayout(self.__get_header())
        chat_layout.addWidget(self.__get_message_list(self.chat['messages']))
        chat_layout.addLayout(self.__get_input_layout())

        chat_layout.addWidget(self.__get_back_button())

        options_layout = QVBoxLayout()
        options_layout.addWidget(self.__get_choice_widget())
        options_layout.addWidget(self.__get_update_options_button())
        self.options_layout =  options_layout

        main_layout = QHBoxLayout()
        main_layout.addLayout(chat_layout)
        main_layout.addLayout(options_layout)

        return main_layout

    def __get_message_list(self, messages):
        self.message_list = MessageListWidget(messages)
        return self.message_list

    def __get_choice_widget(self):
        self.choice_widget = ChoiceWidget(self.options)
        return self.choice_widget

    def __get_input_layout(self):
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.__get_message_input())
        input_layout.addWidget(self.__get_send_button())
        return input_layout

    def __get_back_button(self):
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.on_back_clicked)
        return back_button

    def __get_send_button(self):
        send_button = QPushButton("Отправить")
        send_button.setFixedWidth(100)
        send_button.clicked.connect(self.on_send_clicked)
        return send_button

    def __get_update_options_button(self):
        send_button = QPushButton("Обновить варианты ответов")
        send_button.clicked.connect(self.on_update_options_clicked)
        return send_button

    def __get_message_input(self):
        self.message_input = QTextEdit()
        self.message_input.setFixedHeight(60)
        self.message_input.setPlaceholderText("Введите сообщение...")
        return self.message_input

    def __get_header(self):
        header_layout = QHBoxLayout()
        avatar_label = self.__get_avatar_label()
        header_layout.addWidget(avatar_label)
        name_label = QLabel(self.chat['name'])
        name_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        header_layout.addWidget(name_label)
        header_layout.addStretch()
        return header_layout

    def __get_avatar_label(self):
        size = 70
        avatar_label = QLabel()
        avatar_label.setFixedSize(size, size)

        pixmap = QPixmap(size, size)
        pixmap.fill(QColor(0, 100, 0))  # Зеленый цвет как заглушка

        avatar_label.setPixmap(pixmap)
        return avatar_label

    def on_send_clicked(self):
        message_text = self.message_input.toPlainText().strip()
        send_message_event = {
            'name': 'send_message',
            'context': {
                'text': message_text, 'user_id': self.chat['id']
            }
        }
        gui.event_controller.handle_event(send_message_event)

        get_chat_event = {
            'name': 'get_chat',
            'context': {
                'user_id': self.chat['id']
            }
        }
        chat = gui.event_controller.handle_event(get_chat_event)
        self.chat = chat
        self.layout().removeWidget(self.message_list)
        message_list = self.__get_message_list(chat['messages'])
        self.layout().insertWidget(1, message_list)

        self.message_input.clear()

    def on_update_options_clicked(self):
        event = {
            'name': 'show_options',
            'context': {
                'chat': self.chat
            },
        }

        self.options = gui.event_controller.handle_event(event)

        if self.choice_widget:
            self.layout().removeWidget(self.choice_widget)

        self.choice_widget = ChoiceWidget(self.options)
        self.options_layout.insertWidget(self.layout().count() -1, self.choice_widget)
        

    def on_back_clicked(self):
        self.accept()