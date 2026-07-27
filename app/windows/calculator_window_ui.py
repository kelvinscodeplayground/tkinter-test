import customtkinter as ctk


class CalculatorWindowUI:
    OPERATIONS = ["/", "*", "-", "+", "="]

    number_line: ctk.CTkEntry
    number_pad: ctk.CTkFrame
    digit_buttons: list[ctk.CTkButton]
    operation_buttons: list[ctk.CTkButton]
    zero_button: ctk.CTkButton
    equal_button: ctk.CTkButton
    period_button: ctk.CTkButton
    backspace_button: ctk.CTkButton
    clear_button: ctk.CTkButton
    percent_button: ctk.CTkButton

    def __init__(self, window: ctk.CTk):
        self.digit_buttons = []
        self.operation_buttons = []

        self.__setup_ui(window)

    def __setup_ui(self, window: ctk.CTk):
        self.number_line = ctk.CTkEntry(
            window, font=("Arial", 50), justify="right", height=100
        )
        self.number_line.insert(0, "0")
        self.number_line.pack(side="top", fill="x", padx=10, pady=10)

        self.__setup_number_pad(window)

    def __setup_number_pad(self, window: ctk.CTk):
        font = ("Arial", 30)
        self.number_pad = ctk.CTkFrame(window)

        for i in range(4):
            self.number_pad.grid_columnconfigure(i, weight=1)

        for j in range(5):
            self.number_pad.grid_rowconfigure(j, weight=1)

        self.number_pad.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        for i in range(3):
            for j in range(3):
                digit = i * 3 + j + 1
                button = ctk.CTkButton(
                    self.number_pad,
                    text=str(digit),
                    font=font,
                )
                # add numbers in reverse order, so 1 is at the bottom left and 9 is at the top right
                button.grid(row=3 - i, column=j, sticky="nsew", padx=5, pady=5)
                self.digit_buttons.append(button)

        # Add the 0 button
        self.zero_button = ctk.CTkButton(
            self.number_pad,
            text="0",
            font=font,
        )
        self.zero_button.grid(
            row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5
        )

        # Add the period button
        self.period_button = ctk.CTkButton(
            self.number_pad,
            text=".",
            font=font,
        )
        self.period_button.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

        # Add the opps button
        for idx, op in enumerate(self.OPERATIONS):
            button = ctk.CTkButton(
                self.number_pad,
                text=op,
                # different colour if op is equal sign
                fg_color="orange" if op == "=" else None,
                font=font,
            )
            button.grid(
                row=idx,
                column=3,
                sticky="nsew",
                padx=5,
                pady=5,
            )
            self.operation_buttons.append(button)

        self.backspace_button = ctk.CTkButton(
            self.number_pad,
            text="⌫",
            font=font,
        )
        self.backspace_button.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.clear_button = ctk.CTkButton(
            self.number_pad,
            text="C",
            font=font,
        )
        self.clear_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.percent_button = ctk.CTkButton(
            self.number_pad,
            text="%",
            font=font,
        )
        self.percent_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
