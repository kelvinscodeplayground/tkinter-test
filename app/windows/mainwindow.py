import tkinter as tk

from app.utils import file_system as fs


class MainWindow:
    __WINDOW_SIZE = (640, 480)
    __APP_ICON_PATH = fs.create_path("/assets/icons/tools.png")

    __window: tk.Tk
    __label: tk.Label

    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("My Tkinter App")
        self.__window.geometry(f"{self.__WINDOW_SIZE[0]}x{self.__WINDOW_SIZE[1]}")

        self.__setup()

    def mainloop(self):
        self.__window.mainloop()

    # Private methods
    def __setup(self):
        self.__initialize_ui()
        self.__center_window()
        self.__set_app_icon()

    def __initialize_ui(self):
        # initialize lablel, then set it to aligned left
        self.__label = tk.Label(
            self.__window, text="Hello, Tkinter!", anchor="w", justify="left"
        )
        self.__label.pack(side="left", anchor="nw", fill="x")

    def __center_window(self):
        screen_width = self.__window.winfo_screenwidth()
        screen_height = self.__window.winfo_screenheight()
        x = (screen_width // 2) - (self.__WINDOW_SIZE[0] // 2)
        y = (screen_height // 2) - (self.__WINDOW_SIZE[1] // 2)
        self.__window.geometry(f"+{x}+{y}")

    def __set_app_icon(self):
        bitmap = tk.PhotoImage(file=fs.get_abs_file_path(self.__APP_ICON_PATH))
        self.__window.wm_iconphoto(False, bitmap)
