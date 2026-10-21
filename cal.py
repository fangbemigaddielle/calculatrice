
import tkinter as tk
import re

# Main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("340x470")
root.resizable(False, False)
root.configure(bg="#172033")

expression = ""
display_text = tk.StringVar(value="0")


def press(value):
    global expression

    if value == "C":
        expression = ""
        display_text.set("0")

    elif value == "⌫":
        expression = expression[:-1]
        display_text.set(expression or "0")

    elif value == "=":
        try:
            # Only allow numbers and calculator operators
            if not expression or not re.fullmatch(
                r"[0-9+\-*/().% ]+", expression
            ):
                raise ValueError("Invalid expression")

            result = eval(expression, {"__builtins__": {}}, {})

            if isinstance(result, complex):
                raise ValueError("Invalid result")

            expression = str(result)
            display_text.set(expression)

        except Exception:
            expression = ""
            display_text.set("Error")

    else:
        if display_text.get() in ("Error", "Cannot divide by zero"):
            expression = ""

        expression += value
        display_text.set(expression)


# Display
display = tk.Label(
    root,
    textvariable=display_text,
    font=("Arial", 24),
    bg="#0B1220",
    fg="white",
    anchor="e",
    padx=12
)
display.pack(fill="both", padx=12, pady=16, ipady=18)

# Calculator buttons
buttons = [
    ["C", "(", ")", "⌫"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["="]
]

button_frame = tk.Frame(root, bg="#172033")
button_frame.pack(fill="both", expand=True, padx=10, pady=4)

for row_index, row in enumerate(buttons):
    button_frame.rowconfigure(row_index, weight=1)

    for col_index, value in enumerate(row):
        button_frame.columnconfigure(col_index, weight=1)

        if value == "=":
            col_span = 4
            button_column = 0
            color = "#2563EB"
        else:
            col_span = 1
            button_column = col_index
            color = (
                "#334155"
                if value in ["C", "(", ")", "⌫", "/", "*", "-", "+", "%"]
                else "#243047"
            )

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            relief="flat",
            bd=0,
            command=lambda v=value: press(v)
        )

        button.grid(
            row=row_index,
            column=button_column,
            columnspan=col_span,
            sticky="nsew",
            padx=4,
            pady=4
        )

root.mainloop()
