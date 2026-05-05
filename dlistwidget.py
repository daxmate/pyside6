from PySide6.QtWidgets import QListWidget

class DListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addItem("Item 1")
        self.addItem("Item 2")
        self.addItem("Item 3")
        self.setWordWrap(True)
