import tkinter as tk

from app.utils import file_system as fs


class MainWindow:
    __window_size = (640, 480)
    __app_icon_path = fs.create_path("/assets/icons/tools.png")

    app: tk.Tk

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("My Tkinter App")
        self.app.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}")
        self.__center_window()
        self.__set_app_icon()

    def mainloop(self):
        self.app.mainloop()

    # Private methods
    def __center_window(self):
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width // 2) - (self.__window_size[0] // 2)
        y = (screen_height // 2) - (self.__window_size[1] // 2)
        self.app.geometry(f"+{x}+{y}")

    def __set_app_icon(self):
        try:
            print(
                f"Setting app icon from: {fs.get_abs_file_path(self.__app_icon_path)}"
            )
            bitmap = tk.PhotoImage(file=fs.get_abs_file_path(self.__app_icon_path))
            self.app.wm_iconphoto(False, bitmap)
        except Exception as e:
            print(f"Error setting app icon: {e}")
