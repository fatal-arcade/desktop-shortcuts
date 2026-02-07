from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QMenu, QFormLayout

from widgets import *

class Waypoint(Application):

    testmenu : QWidget

    def __init__(self):
        super().__init__()
        self.__testmenu__()

    def __testmenu__(self):
        pass

    def run(self):
        self.main_window.show()
        self.application.exec()
