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
        self.__setup_slots()

    # private methods
    def __center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.__WINDOW_SIZE[0]) // 2
        y = (screen_height - self.__WINDOW_SIZE[1]) // 2
        self.geometry(f"{self.__WINDOW_SIZE[0]}x{self.__WINDOW_SIZE[1]}+{x}+{y}")
        self.resizable(False, False)

    def __setup_slots(self):
        for button in self.__ui.digit_buttons:
            button.configure(command=lambda b=button: self.__on_digit_button_click(b))

        self.__ui.zero_button.configure(
            command=lambda b=self.__ui.zero_button: self.__on_digit_button_click(b)
        )

        for op_btn in self.__ui.operation_buttons:
            op_btn.configure(
                command=lambda b=op_btn: self.__on_operation_button_click(b)
            )

        self.__ui.clear_button.configure(command=self.__on_clear_button_click)
        self.__ui.period_button.configure(command=self.__on_period_button_click)
        self.__ui.backspace_button.configure(command=self.__on_backspace_button_click)
        self.__ui.percent_button.configure(command=self.__on_percent_button_click)

    # slots
    def __on_digit_button_click(self, button: ctk.CTkButton):
        current_text = self.__ui.number_line.get()
        input_text = button.cget("text")

        # return direicty if current text is empty or is 0
        if current_text == "0" and (input_text == "0" or input_text == "."):
            return  # Prevent multiple leading zeros

        new_text = current_text + button.cget("text")
        should_replace = (
            current_text == "0" and input_text != "."
        ) or current_text == "Error"

        if should_replace:
            new_text = input_text

        self.__ui.number_line.delete(0, ctk.END)
        self.__ui.number_line.insert(0, new_text)

    def __on_operation_button_click(self, button: ctk.CTkButton):
        current_text = self.__ui.number_line.get()
        input_text = button.cget("text")

        if input_text == "=":
            try:
                result = eval(current_text)
                self.__ui.number_line.delete(0, ctk.END)
                self.__ui.number_line.insert(0, str(result))
            except Exception:
                self.__ui.number_line.delete(0, ctk.END)
                self.__ui.number_line.insert(0, "Error")
        else:
            if current_text[-1] in CalculatorWindowUI.OPERATIONS:
                # Replace the last operation with the new one
                new_text = current_text[:-1] + input_text
            else:
                new_text = current_text + input_text

            self.__ui.number_line.delete(0, ctk.END)
            self.__ui.number_line.insert(0, new_text)

    def __on_percent_button_click(self):
        pass

    def __on_period_button_click(self):
        current_text = self.__ui.number_line.get()

        # Prevent multiple periods in the current number
        if "." in current_text.split()[-1]:
            return

        new_text = current_text + "."
        self.__ui.number_line.delete(0, ctk.END)
        self.__ui.number_line.insert(0, new_text)

    def __on_clear_button_click(self):
        self.__ui.number_line.delete(0, ctk.END)
        self.__ui.number_line.insert(0, "0")

    def __on_backspace_button_click(self):
        current_text = self.__ui.number_line.get()
        if len(current_text) > 1:
            new_text = current_text[:-1]
        else:
            new_text = "0"

        self.__ui.number_line.delete(0, ctk.END)
        self.__ui.number_line.insert(0, new_text)
