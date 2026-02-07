from PySide6.QtWidgets import QHBoxLayout

from widgets import *

class Waypoint(Application):

    testmenu : QWidget

    def __init__(self):
        super().__init__()
        self.__testmenu__()


    def __testmenu__(self):
        img_input = FileBrowserImage()
        app_input = DesktopEntryForm()
        layout = QHBoxLayout()
        layout.addWidget(img_input)
        layout.addWidget(app_input)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.testmenu = QWidget()
        self.testmenu.setLayout(layout)
        self.central_widget.setCurrentIndex(0)
        self.central_widget.addWidget(self.testmenu)



    def run(self):
        self.main_window.show()
        self.application.exec()
