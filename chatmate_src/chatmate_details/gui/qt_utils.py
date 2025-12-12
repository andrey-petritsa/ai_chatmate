from PyQt6.QtCore import QRect, QPoint


class QtUtils:
    @classmethod
    def center(cls, widget):
        screen = widget.screen().geometry()
        window_size = widget.geometry()
        center_point = screen.center()
        new_rect = QRect(QPoint(0, 0), window_size.size())
        new_rect.moveCenter(center_point)
        widget.setGeometry(new_rect)