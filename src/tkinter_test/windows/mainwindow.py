import tkinter as tk
from tkinter import ttk

from tkinter_test.utils import file_system as fs


class MainWindow(tk.Tk):
    __WINDOW_SIZE = (640, 480)
    __APP_ICON_PATH = fs.create_path("/icons/tools.png")

    __label: ttk.Label
    __button: ttk.Button

    def __init__(self):
        super().__init__()

        self.title("My Tkinter App")
        self.geometry(f"{self.__WINDOW_SIZE[0]}x{self.__WINDOW_SIZE[1]}")

        self.__setup()

    # Private methods
    def __setup(self):
        self.__initialize_ui()
        self.__center_window()
        self.__set_app_icon()

    def __initialize_ui(self):
        # initialize lablel, then set it to aligned left
        self.__label = ttk.Label(self, text="Hello, Tkinter!")
        self.__label.pack(side="top")

        self.__button = ttk.Button(
            self, text="Click Me!", command=self.__on_button_click
        )
        self.__button.pack(side="top")

    def __center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (self.__WINDOW_SIZE[0] // 2)
        y = (screen_height // 2) - (self.__WINDOW_SIZE[1] // 2)
        self.geometry(f"+{x}+{y}")

    def __set_app_icon(self):
        bitmap = tk.PhotoImage(file=fs.get_abs_file_path(self.__APP_ICON_PATH))
        self.wm_iconphoto(False, bitmap)

    # Event handlers
    def __on_button_click(self):
        self.__label.config(text="Button Clicked!")
