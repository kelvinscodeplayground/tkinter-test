import os


def get_abs_file_path(relative_path) -> str:
    """
    Get the absolute file path based on the relative path provided.

    This function calculates the absolute path by considering the location of the current script file
    and navigating up two directories before appending the relative path. If the relative path starts with a leading
    slash, it will be removed to ensure correct path joining.

    Eg:
        - /assets/icons/tools.png -> /home/user/Document/app/assets/icons/tools.png
        - ../assets/icons/tools.png -> /home/user/Document/app/assets/icons/tools.png

    Args:
        relative_path (str): The relative file path.
    """

    # Get the directory of the current script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Clean up the relative path to ensure it doesn't start with a leading slash
    relative_path = relative_path.lstrip("/\\")

    # Join the script directory with the relative path to get the absolute path
    abs_path = os.path.abspath(os.path.join(script_dir, "..", "..", relative_path))
    return abs_path


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
