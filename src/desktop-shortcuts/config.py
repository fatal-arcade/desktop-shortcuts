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
css_secondary_color = "#4a4a4a"
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
theme =' '.join([
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
filter_images       = 'Images(*.png *.svg *.xpm *.jpg *.jpeg)'
filter_shortcuts    = 'Shortcuts (*.desktop)'


# images and icons
# =============================================================================
icon_app = os.path.join(dir_assets, 'logo.png')
icon_image = os.path.join(dir_icons, 'image.png')
icon_search = os.path.join(dir_icons, 'search.png')


# window
# =============================================================================
win_max_size    = (500, 500)
win_min_size    = (500, 500)
win_size        = (500, 500)
