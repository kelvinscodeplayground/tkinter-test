from tkinter import Tk


class MainWindow:
    __window_size = (640, 480)

    app: Tk

    def __init__(self):
        self.app = Tk()
        self.app.title("My Tkinter App")
        self.app.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}")
        self.__center_window()

    def mainloop(self):
        self.app.mainloop()

    # Private methods
    def __center_window(self):
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width // 2) - (self.__window_size[0] // 2)
        y = (screen_height // 2) - (self.__window_size[1] // 2)
        self.app.geometry(f"+{x}+{y}")
