import os


def get_desktop_dir():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    try:
        with open(os.path.expanduser("~/.config/user-dirs.dirs"), "r") as f:
            for line in f:
                if line.startswith("XDG_DESKTOP_DIR"):
                    path = line.split("=")[1].strip().strip('"')
                    path = path.replace("$HOME", os.path.expanduser("~"))
                    return path
    except FileNotFoundError:
        pass
    return desktop


def get_applications_dir():
    """Return standard user applications dir for .desktop files."""
    path = os.path.join(os.path.expanduser("~"), ".local", "share", "applications")
    os.makedirs(path, exist_ok=True)
    return path


def generate_desktop_entry_file(state: dict, path: str) -> str:
    """
    Writes a .desktop file to the specified path using the app state.
    Returns the full path of the created file.
    """
    # Ensure boolean fields are lowercase 'true'/'false'
    bool_map = lambda val: 'true' if val else 'false'

    lines = [
        "[Desktop Entry]",
        "Version=1.0",
        "Type=Application",
        f"Name={state.get('name', '')}",
        f"Comment={state.get('comment', '')}",
        f"Exec={state.get('exec', '')}",
        f"Icon={state.get('icon', '')}",
        f"Categories={state.get('category', 'Utility')};",
        f"Terminal={bool_map(state.get('Terminal', False))}",
        f"Hidden={bool_map(state.get('Hidden', False))}",
        f"NoDisplay={bool_map(state.get('NoDisplay', False))}",
        f"StartupNotify={bool_map(state.get('StartupNotify', True))}"
    ]

    # Ensure filename ends with .desktop
    filename = state.get('name', 'application').replace(" ", "_") + ".desktop"
    full_path = os.path.join(path, filename)

    with open(full_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    # Make file executable
    os.chmod(full_path, 0o755)
    return full_path
