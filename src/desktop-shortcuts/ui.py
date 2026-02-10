# ui.py
import sys
import config
from state import app_state
from desktop import *

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QLineEdit,
    QComboBox, QCheckBox, QFileDialog,
    QHBoxLayout, QVBoxLayout, QFormLayout, QMessageBox
)

# ------------------------------------------------------------------
# widget helpers
# ------------------------------------------------------------------

def create_button(text, w=None, h=None, func=None):
    btn = QPushButton(text)
    if func:
        btn.clicked.connect(func)
    if w: btn.setFixedWidth(w)
    if h: btn.setFixedHeight(h)
    return btn

def create_image(path, size=128):
    lbl = QLabel()
    lbl.setFixedSize(QSize(size, size))
    lbl.setAlignment(Qt.AlignCenter)
    lbl.setScaledContents(True)
    lbl.setPixmap(QPixmap(path))
    return lbl

def create_input(placeholder, tooltip=None):
    le = QLineEdit()
    le.setPlaceholderText(placeholder)
    if tooltip:
        le.setToolTip(tooltip)
    return le

# ------------------------------------------------------------------
# main window
# ------------------------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(config.app_title)
        self.setWindowIcon(QIcon(config.icon_app))
        self.setFixedSize(*config.win_size)

        # CENTRAL WIDGET + MAIN VERTICAL LAYOUT
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 5, 10, 10)
        main_layout.setSpacing(5)

        # -------------------- UPPER PANEL --------------------
        upper_widget = QWidget()
        upper_layout = QHBoxLayout(upper_widget)
        upper_layout.setAlignment(Qt.AlignTop)
        upper_layout.setSpacing(20)

        # LEFT COLUMN (icon)
        self.icon_label = create_image(config.icon_app)
        app_state["icon"] = config.icon_app
        icon_btn = create_button("Change Icon", 128, 32, self.choose_icon)

        left_col = QVBoxLayout()
        left_col.setSpacing(32)
        left_col.addWidget(self.icon_label)
        left_col.addWidget(icon_btn)
        left_col.addStretch()

        left_widget = QWidget()
        left_widget.setLayout(left_col)
        left_widget.setFixedWidth(160)

        # RIGHT COLUMN (checkboxes)
        checkbox_widget = QWidget()
        checkbox_layout = QVBoxLayout(checkbox_widget)
        checkbox_layout.setAlignment(Qt.AlignTop)
        checkbox_layout.setSpacing(8)  # slightly tighter spacing inside panel

        # Style the checkbox area to appear as a single panel
        checkbox_widget.setStyleSheet(f"""
            background-color: {config.css_secondary_color};
            border-radius: 10px;
            padding: 10px;
        """)

        upper_options = [
            ("Create in application menu", "ShowInMenu", True),
            ("Run in Terminal", "Terminal", False),
            ("Disable Launcher", "Hidden", False),
            ("Do not show in menus", "NoDisplay", False),
            ("Show startup notification", "StartupNotify", True)
        ]

        self.upper_checkboxes = {}
        for label, key, default in upper_options:
            cb = QCheckBox(label)
            cb.setChecked(default)
            cb.setToolTip(config.checkbox_tooltips.get(key, ""))
            cb.stateChanged.connect(lambda state, k=key: app_state.__setitem__(k, bool(state)))
            checkbox_layout.addWidget(cb)
            self.upper_checkboxes[key] = cb

        upper_layout.addWidget(left_widget)
        upper_layout.addWidget(checkbox_widget)
        main_layout.addWidget(upper_widget)

        # -------------------- LOWER PANEL (entry form) --------------------
        lower_widget = QWidget()
        lower_layout = QVBoxLayout(lower_widget)
        lower_layout.setAlignment(Qt.AlignTop)
        lower_layout.setSpacing(8)

        # INPUT FIELDS WITH TOOLTIP FROM CONFIG
        self.name_input = create_input("Application name", tooltip=config.input_tooltips.get("name"))
        self.exec_input = create_input("Executable path", tooltip=config.input_tooltips.get("exec"))
        self.cmnt_input = create_input("Tooltip description (optional)", tooltip=config.input_tooltips.get("comment"))
        self.kwrd_input = create_input("Menu search terms", tooltip=config.input_tooltips.get("keywords"))
        self.cats_input  = QComboBox()
        self.cats_input.addItems(config.list_category)
        self.cats_input.setToolTip(config.input_tooltips.get("category"))

        # Bind inputs to app_state
        self.name_input.textChanged.connect(lambda v: app_state.__setitem__("name", v))
        self.exec_input.textChanged.connect(lambda v: app_state.__setitem__("exec", v))
        self.cmnt_input.textChanged.connect(lambda v: app_state.__setitem__("comment", v))
        self.cats_input.currentTextChanged.connect(lambda v: app_state.__setitem__("category", v))
        self.kwrd_input.textChanged.connect(lambda v: app_state.__setitem__("keywords", v))

        # EXEC ROW WITH BROWSE BUTTON
        exec_browse_btn = create_button("Browse", 80, 24, self.browse_exec)
        exec_row_widget = QWidget()
        exec_row_layout = QHBoxLayout(exec_row_widget)
        exec_row_layout.setContentsMargins(0, 0, 0, 0)
        exec_row_layout.setSpacing(5)
        exec_row_layout.addWidget(self.exec_input)
        exec_row_layout.addWidget(exec_browse_btn)

        # FORM LAYOUT
        form = QFormLayout()
        form.setSpacing(12)  # spacing between rows
        form.addRow("Name:", self.name_input)
        form.addRow("Exec:", exec_row_widget)
        form.addRow("Comment:", self.cmnt_input)
        form.addRow("Keywords:", self.kwrd_input)
        form.addRow("Category:", self.cats_input)

        form_widget = QWidget()
        form_widget.setLayout(form)
        lower_layout.addWidget(form_widget)
        lower_layout.addStretch()
        main_layout.addWidget(lower_widget)

        # -------------------- CREATE / CLEAR BUTTONS --------------------
        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 10, 0, 10)
        button_layout.setSpacing(15)
        button_layout.setAlignment(Qt.AlignCenter)

        button_width = 160
        button_height = 32
        clear_btn = create_button("Clear / Reset Form", button_width, button_height, self.clear_form)
        create_shortcut_btn = create_button("Create Shortcut", button_width, button_height, self.create_shortcut)

        button_layout.addWidget(clear_btn)
        button_layout.addWidget(create_shortcut_btn)
        main_layout.addWidget(button_widget)

    # -------------------- ICON FILE DIALOG --------------------
    def choose_icon(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Choose Icon", config.dir_user, config.filter_images
        )
        if path:
            app_state["icon"] = path
            self.icon_label.setPixmap(QPixmap(path))

    # -------------------- EXECUTABLE BROWSER --------------------
    def browse_exec(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Executable", config.dir_user, config.filter_exec
        )
        if path:
            self.exec_input.setText(path)

    # -------------------- CREATE SHORTCUT HANDLER --------------------
    def create_shortcut(self):
        desktop_dir  = get_desktop_dir()
        desktop_path = generate_desktop_entry_file(app_state, desktop_dir)

        # Also create in application menu if ShowInMenu is checked
        if app_state.get("ShowInMenu", True):
            applications_dir = get_applications_dir()
            generate_desktop_entry_file(app_state, applications_dir)

        # Confirmation popup
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Shortcut Created")
        msg_box.setText(f"The desktop shortcut has been created successfully:\n\n{desktop_path}")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

        print("Shortcut creation triggered.")
        print("Current state:", app_state)

    # -------------------- CLEAR FORM HANDLER --------------------
    def clear_form(self):
        self.name_input.clear()
        self.exec_input.clear()
        self.cmnt_input.clear()
        self.kwrd_input.clear()
        self.cats_input.setCurrentIndex(0)

        for key, cb in self.upper_checkboxes.items():
            default_state = True if key in ["ShowInMenu", "StartupNotify"] else False
            cb.setChecked(default_state)

        self.icon_label.setPixmap(QPixmap(config.icon_app))
        app_state.clear()
        app_state.update({
            "icon": config.icon_app,
            "ShowInMenu": True,
            "Terminal": False,
            "Hidden": False,
            "NoDisplay": False,
            "StartupNotify": True
        })

# ------------------------------------------------------------------
# application instance
# ------------------------------------------------------------------
application = QApplication(sys.argv)
application.setApplicationName(config.app_name)
application.setApplicationVersion(config.app_version)

main_window = MainWindow()
main_window.show()
