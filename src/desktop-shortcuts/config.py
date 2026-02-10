import os


# application
# =============================================================================
app_name    = 'Desktop Shortcuts'
app_author  = 'Fatal Arcade'
app_version = '1.0.0'
app_title   = ' v'.join([app_name, app_version])


# characters and symbols
# =============================================================================
char_arrow_up    = '▲'
char_arrow_down  = '▼'
char_ellipses    = '…'
char_triple_bar  = '☰'
char_win_close   = '✕'
char_win_expand  = '□'
char_win_iconify = '−'


# css elements
# =============================================================================
css_primary_color   = "#2e2e2e"
css_secondary_color = 'rgba(200, 200, 200, 0.15)'  #"#4a4a4a"
css_highlight_color = "#5a5a5a"
css_accent_color    = "#666"
css_font_family     = 'Sans-Serif'
css_font_weight     = 'bold'
css_font_color      = '#ccc'
css_font_size       = '14px'
css_border_radius   = '16px'
css_border_style    = 'none'
css_border_width    = '0px'


# css theme
# =============================================================================
css_stylesheet =' '.join([
    'QWidget {',
        f'background-color: #2E2E2E;'
        f'color: white;',

    '} QPushButton {',
        f'background-color: #4A4A4A;' 
        f'border: 1px solid #666;'
    
    '} QPushButton:hover {' 
        f'background-color: #5A5A5A;'
    
    '} QPushButton:pressed {',
        f'background-color: #4A4A4A;' 
        f'border: 1px solid #666;'
    
    '} QPushButton:disabled {',
        f'background-color: #4A4A4A;' 
        f'border: 1px solid #666;'
    
    '} QLineEdit {',
        f'background-color: #4A4A4A;' 
        f'border: 1px solid #666;'
    
    '} QLineEdit:focus {' 
        f'background-color: #5A5A5A;'
    '}'
])


# desktop entry combo lists
# =============================================================================
list_category   = [
    '',
    'AudioVideo',
    'Audio',
    'Video',
    'Development',
    'Education',
    'Game',
    'Graphics',
    'Network',
    'Office',
    'Science',
    'Settings',
    'System',
    'Utility'
]
list_entry_type = [
    'Application',
    'Link',
    'Directory'
]


# directories
# =============================================================================
dir_src     = os.path.dirname(os.path.abspath(__file__))
dir_root    = os.path.dirname(os.path.dirname(dir_src))
dir_assets  = os.path.join(dir_src, 'assets')
dir_icons   = os.path.join(dir_assets, 'icons')
dir_user    = os.path.expanduser('~')
dir_desktop = os.path.join(dir_user, 'Desktop')


# file type search filters
# =============================================================================
filter_all          = 'All Files (*)'
filter_exec         = 'Executables (*.AppImage *.deb *.flatpak *.sh);;All Files (*)'
filter_images       = 'Images(*.png *.svg *.xpm *.jpg *.jpeg)'
filter_shortcuts    = 'Shortcuts (*.desktop)'


# images and icons
# =============================================================================
icon_app = os.path.join(dir_assets, 'logo.png')
icon_image = os.path.join(dir_icons, 'image.png')
icon_search = os.path.join(dir_icons, 'search.png')


# tooltips
# =============================================================================
checkbox_tooltips = {
    "ShowInMenu":       "If checked, the shortcut will appear in the application menu.",
    "Terminal":         "If checked, the application will run inside a terminal window.",
    "Hidden":           "If checked, the launcher will be hidden from menus but still callable.",
    "NoDisplay":        "If checked, the shortcut will not appear in menus or search.",
    "StartupNotify":    "If checked, the system will show a startup notification when launched."
}

input_tooltips = {
    "icon_label":           "This is the icon that will be used for your desktop shortcut.",
    "icon_button":          "Click to choose a custom icon for the shortcut.",
    "name":                 "Enter the display name for your shortcut.",
    "exec":                 "Enter the path to the executable or click 'Browse'.",
    "exec_button":          "Open a file dialog to select the executable.",
    "comment":              "Optional: Add a tooltip or description for the shortcut.",
    "keywords":             "Optional: Enter search terms to help locate the shortcut in menus.",
    "category":             "Select the category for your shortcut.",
    "create_checkbox":      "Check to enable this option for the shortcut.",
    "create_button":        "Click to create the desktop shortcut.",
    "clear_button":         "Click to reset all fields to default values."
}


# window
# =============================================================================
win_max_size    = (500, 500)
win_min_size    = (500, 500)
win_size        = (500, 500)
