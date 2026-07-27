import customtkinter as ctk

from app.windows.calculator_window_ui import CalculatorWindowUI


class CalculatorWindow(ctk.CTk):
    __WINDOW_SIZE = (400, 600)

    __ui: CalculatorWindowUI

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry(f"{self.__WINDOW_SIZE[0]}x{self.__WINDOW_SIZE[1]}")
        self.__center_window()

        self.__ui = CalculatorWindowUI(self)

        for button in self.__ui.digit_buttons:
            button.configure(command=lambda b=button: self.__on_digit_button_click(b))

    # private methods
    def __center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.__WINDOW_SIZE[0]) // 2
        y = (screen_height - self.__WINDOW_SIZE[1]) // 2
        self.geometry(f"{self.__WINDOW_SIZE[0]}x{self.__WINDOW_SIZE[1]}+{x}+{y}")
        self.resizable(False, False)

    # slots
    def __on_digit_button_click(self, button: ctk.CTkButton):
        current_text = self.__ui.number_line.get()
        new_text = current_text + button.cget("text")
        self.__ui.number_line.delete(0, ctk.END)
        self.__ui.number_line.insert(0, new_text)
