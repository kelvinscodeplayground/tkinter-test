import os
from importlib.resources import as_file, files
from pathlib import Path


def get_abs_file_path(relative_path) -> str:
    """
    Get the absolute file path based on the relative path provided.

    This function calculates the absolute path by considering the location of the current script file
    and navigating up two directories before appending the relative path. If the relative path starts with a leading
    slash, it will be removed to ensure correct path joining.

    Eg:
        - /assets/icons/tools.png -> /home/user/Document/app/assets/icons/tools.png
        - ../assets/icons/tools.png -> /home/user/Document/assets/icons/tools.png
        - assets/icons/tools.png -> /home/user/Document/app/assets/icons/tools.png

    Args:
        relative_path (str): The relative file path.
    """

    try:
        # Try using importlib.resources (works in installed packages)
        asset_files = files("tkinter_test").joinpath("assets")
        resource_path = asset_files.joinpath(relative_path)

        # Convert to actual filesystem path
        with as_file(resource_path) as path:
            return str(path)
    except FileNotFoundError, TypeError:
        # Fallback for development (loose files)
        script_dir = Path(__file__).parent.parent
        abs_path = script_dir / "assets" / relative_path
        return str(abs_path.resolve())


def create_path(path: list[str] | str) -> str:
    """
    Create path objects from a list of string or string.

    It will concat the list of strings into a single path string if a list is provided, or return the string by
    replacing the slashes with the os specific separator if a string is provided.
    """

    if isinstance(path, list):
        return os.path.join(*path)
    elif isinstance(path, str):
        os_saperator = os.path.sep
        return path.replace("/", os_saperator).replace("\\", os_saperator)
