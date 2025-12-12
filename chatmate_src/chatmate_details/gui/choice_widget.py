from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QHBoxLayout, QRadioButton, QTextEdit


class ChoiceWidget(QWidget):
    def __init__(self, options):
        self.options = options
        super().__init__()

        main_layout = QVBoxLayout()
        self.button_group = QButtonGroup()

        for option in options:
            option_widget = QWidget()
            option_widget.setLayout(self.__get_option_layout(option))
            main_layout.addWidget(option_widget)

        self.button_group.buttonClicked.connect(self.on_button_clicked)
        self.setLayout(main_layout)

    def __get_option_layout(self, option):
        radio = QRadioButton()
        self.button_group.addButton(radio, self.options.index(option))
        text_edit = self.__get_text_edit(option)
        option_layout = QHBoxLayout()
        option_layout.addWidget(radio)
        option_layout.addWidget(text_edit)
        return option_layout

    def __get_text_edit(self, option):
        text_edit = QTextEdit()
        text_edit.setPlainText(option)
        text_edit.setMinimumWidth(200)
        text_edit.setMaximumHeight(100)
        text_edit.setReadOnly(True)
        return text_edit

    def on_button_clicked(self, button):
        index = self.button_group.id(button)
        self.parent().message_input.setPlainText(self.options[index])
