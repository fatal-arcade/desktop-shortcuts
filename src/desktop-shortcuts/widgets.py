import sys
import config

from abc               import ABC, abstractmethod
from typing            import Any, Callable
from PySide6.QtGui     import QIcon, QPixmap, QCursor
from PySide6.QtCore    import QSize, Qt
from PySide6.QtWidgets import (
    QLineEdit,
    QPushButton,
    QFileDialog,
    QApplication,
    QMainWindow,
    QComboBox,
    QCheckBox,
    QStackedWidget,
    QLabel,
    QGridLayout,
    QWidget
)

# widgets
# =============================================================================
def create_button(caption:str='Button', width:int=None, height:int=None, func:Callable[...,Any]=None) -> QPushButton:

    def event_placeholder():
        print(f'{caption} is missing click event.')

    on_click = event_placeholder if func is None else func

    button = QPushButton(caption)
    button.clicked.connect(on_click)

    if width is not None:
        button.setFixedWidth(width)

    if height is not None:
        button.setFixedHeight(height)

    return button

def create_checkbox(caption:str='Checkbox', state:bool=False, func:Callable[...,Any]=None) -> QCheckBox:

    def event_placeholder():
        print(f'{caption} is missing state change event.')

    on_change = event_placeholder if func is None else func

    checkbox = QCheckBox()
    checkbox.setText(caption)
    checkbox.setChecked(state)
    checkbox.stateChanged.connect(on_change)
    return checkbox

def create_combobox(list_items:list[str]=None, func:Callable[...,Any]=None) -> QComboBox:

    items = [] if list_items is None else list_items

    def event_placeholder():
        print('Combobox is missing change event.')

    on_change = event_placeholder() if func is None else func

    combobox = QComboBox()
    combobox.addItems(items)
    combobox.setCurrentIndex(0)
    combobox.currentIndexChanged.connect(on_change)
    return combobox

def create_icon(image_path:str=None) -> QIcon:

    image = config.icon_app if image_path is None else image_path
    pxmap = QPixmap(image)
    icon  = QIcon(pxmap)
    return icon

def create_image(image_path:str=None, width:int=128, height:int=128) -> QLabel:

    image = config.icon_app if image_path is None else image_path

    label = QLabel()
    label.setScaledContents(True)
    label.setPixmap(
        QPixmap(image).scaled(
            QSize(width, height),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
    )
    label.setFixedSize(QSize(width, height))
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return label

def create_input(placeholder_text:str=None, enable_clear_button:bool=True) -> QLineEdit:

    placeholder = 'Enter Text' if placeholder_text is None else placeholder_text
    lineedit = QLineEdit(clearButtonEnabled=enable_clear_button)
    lineedit.setPlaceholderText(placeholder)
    return lineedit

def create_label(caption:str=None, width:int=128, height:int=32) -> QLabel:

    label = QLabel()
    label.setText(caption)
    label.setFixedSize(QSize(width, height))
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return label

def create_pixmap(image_path:str=None, width:int=128, height:int=128) -> QPixmap:

    image = config.icon_app if image_path is None else image_path
    pxmap = QPixmap(image)
    pxmap.scaled(
        QSize(width, height),
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation
    )
    return pxmap

# custom widgets
# =============================================================================
class FileBrowserInput(QWidget):

    input  : QLineEdit
    button : QPushButton

    def __init__(self, file_type:str=config.filter_all):

        super().__init__()

        def open_filesystem():
            qfdialog = QFileDialog()
            qfdialog.setWindowIcon(create_icon(config.icon_app))
            filepath = qfdialog.getOpenFileName(
                parent=None,
                caption="Select a File",
                dir=file_type,
                filter=config.filter_all
            )[0]

            if filepath:
                self.input.setText(filepath)

        self.input  = create_input('/path/to/file.example')
        self.button = create_button(
            width=32,
            caption=config.char_triple_bar,
            func=open_filesystem
        )

        layout = QGridLayout()
        layout.addWidget(self.input, 0, 0)
        layout.addWidget(self.button, 0, 1)
        self.setLayout(layout)
        self.setContentsMargins(0,0,0,0)

class FileBrowserImage(QWidget):

    image    : QLabel
    button   : QPushButton
    filepath : str

    def __init__(self, image_path:str=None, width:int=128, height:int=128):

        super().__init__()

        def open_filesystem():

            qfdialog = QFileDialog(self)
            qfdialog.setWindowIcon(create_icon(config.icon_app))
            filepath = qfdialog.getOpenFileName(
                parent=None,
                caption='Select Image for Desktop Icon',
                dir=config.dir_user,
                filter=config.filter_images
            )[0]

            if filepath:
                self.change_image(filepath)

        self.filepath = config.icon_image if image_path is None else image_path
        self.image    = create_image(self.filepath, width, height)
        self.button   = create_button('Change Icon', width, 32, open_filesystem)

        layout = QGridLayout()
        layout.setVerticalSpacing(0)
        layout.addWidget(self.image, 0, 0)
        layout.addWidget(self.button, 1, 0)
        self.setLayout(layout)
        self.setFixedWidth(width + 32)
        self.setFixedHeight(height + 64)

    def change_image(self, image_path:str):
        self.filepath = image_path
        self.image.setPixmap(QPixmap(image_path))

class DesktopEntryForm(QWidget):

    name_input: QLineEdit
    exec_input: FileBrowserInput

    def __init__(self):

        super().__init__()

        self.name_input = create_input('Enter Shortcut Name')
        self.exec_input = FileBrowserInput()

        layout = QGridLayout()
        layout.addWidget(create_label('App Name:'), 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(create_label('App Path:'), 1, 0)
        layout.addWidget(self.exec_input, 1, 1)
        self.setLayout(layout)



# application
# =============================================================================
class Application(ABC):

    application     : QApplication
    central_widget  : QStackedWidget
    main_window     : QMainWindow

    def __init__(self):

        # instantiate application (must be first operation)
        self.application = QApplication(sys.argv)
        self.application.setApplicationName(config.app_name)
        self.application.setApplicationVersion(config.app_version)

        # create central widget
        self.central_widget = QStackedWidget()
        self.central_widget.setCurrentIndex(0)

        # get window geometry dimensions (width, height) first, then ...
        max_size = QSize(*config.win_max_size)
        min_size = QSize(*config.win_min_size)
        size     = QSize(*config.win_size)

        # ... get active display geometry to calc window center position (x, y)
        pos = self.application.screenAt(QCursor.pos())
        geo = self.application.primaryScreen() if pos is None else pos
        geo = geo.geometry()

        # instantiate main window
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle(config.app_title)
        self.main_window.setWindowIcon(QIcon(QPixmap(config.icon_app)))
        self.main_window.setCentralWidget(self.central_widget)
        self.main_window.setMaximumSize(max_size)
        self.main_window.setMinimumSize(min_size)
        self.main_window.setGeometry(
            geo.x() + (geo.width()  - size.width())  // 2,
            geo.y() + (geo.height() - size.height()) // 2,
            size.width(),
            size.height()
        )

    @abstractmethod
    def run(self) -> None:
        pass



