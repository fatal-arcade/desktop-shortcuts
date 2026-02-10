import sys
from ui import application, main_window

def launch():
    main_window.show()
    sys.exit(application.exec())

if __name__ == "__main__":
    launch()