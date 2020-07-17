import tkinter as tk
import math
import parser

result = 0

class Calculator(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator GUI")
        self.master.resizable(0,0)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        # Screen Number
        self.screen_number = tk.StringVar(self)
        # Screen
        self.screen = tk.Entry(self, textvariable=self.screen_number)
        self.screen.config(background="black", fg="red", justify="right", font=('Calibri',25) )
        # First row
        # Button %
        self.button_mod = tk.Button(self, height=3, width=10, text="%",
            command=lambda:self.pulse_symbol("%"))
        # Button CE
        self.button_ce = tk.Button(self, height=3, width=10, text="CE",
            command=lambda:self.clear_display())
        # Button delete
        self.button_delete = tk.Button(self, height=3, width=23, text="Backspace",
            command=lambda:self.undo())

        # Second row
        # Button 1/x
        self.button_one = tk.Button(self, height=3, width=10, text="(",
            command=lambda:self.pulse_symbol("("))
        # Button x*22
        self.button_square = tk.Button(self, height=3, width=10, text=")",
            command=lambda:self.pulse_symbol(")"))
        # Button square root
        self.button_square_root = tk.Button(self, height=3, width=10, text="^2",
            command=lambda:self.pulse_symbol("^2"))
        # Button division
        self.button_division = tk.Button(self, height=3, width=10, text="÷",
            command=lambda:self.pulse_symbol("/"))

        # third row
        # Button 7
        self.button_7 = tk.Button(self, height=3, width=10, text="7",
            command=lambda:self.pulse_number("7"))
        # Button 8
        self.button_8 = tk.Button(self, height=3, width=10, text="8",
            command=lambda:self.pulse_number("8"))
        # Button 9
        self.button_9 = tk.Button(self, height=3, width=10, text="9",
            command=lambda:self.pulse_number("9"))
        # Button multiplicate
        self.button_multiplicate = tk.Button(self, height=3, width=10, text="x",
            command=lambda:self.pulse_symbol("*"))

        # fourth row
        # Button 4
        self.button_4 = tk.Button(self, height=3, width=10, text="4",
            command=lambda:self.pulse_number("4"))
        # Button 5
        self.button_5 = tk.Button(self, height=3, width=10, text="5",
            command=lambda:self.pulse_number("5"))
        # Button 6
        self.button_6 = tk.Button(self, height=3, width=10, text="6",
            command=lambda:self.pulse_number("6"))
        # Button subtraction
        self.button_subtraction = tk.Button(self, height=3, width=10, text="-",
            command=lambda:self.pulse_symbol("-"))

        # fifth row
        # Button 1
        self.button_1 = tk.Button(self, height=3, width=10, text="1",
            command=lambda:self.pulse_number("1"))
        # Button 2
        self.button_2 = tk.Button(self, height=3, width=10, text="2",
            command=lambda:self.pulse_number("2"))
        # Button 3
        self.button_3 = tk.Button(self, height=3, width=10, text="3",
            command=lambda:self.pulse_number("3"))
        # Button plus
        self.button_plus = tk.Button(self, height=3, width=10, text="+",
            command=lambda:self.pulse_symbol("+"))

        # six row
        # Button +/- (signal)
        self.button_signal = tk.Button(self, height=3, width=10, text="ANS",
            command=lambda:self.ans())

        # Button 0
        self.button_zero = tk.Button(self, height=3, width=10, text="0",
            command=lambda:self.pulse_number("0"))
        # Button .
        self.button_spot = tk.Button(self, height=3, width=10, text=".",
            command=lambda:self.pulse_symbol("."))
        # Button equals
        self.button_equal = tk.Button(self, height=3, width=10, text="=",
            command=lambda:self.calculate())

    def make_grid(self):
        # Screen
        self.screen.grid(row = 1, column=1, padx=10, pady=10, columnspan=4)
        # First row
        self.button_mod.grid(row = 2, column=1)
        self.button_ce.grid(row = 2, column=2)
        self.button_delete.grid(row = 2, column=3,columnspan=2)
        # Second row
        self.button_one.grid(row = 3, column=1)
        self.button_square.grid(row = 3, column=2)
        self.button_square_root.grid(row = 3, column=3)
        self.button_division.grid(row = 3, column=4)
        # Third row
        self.button_7.grid(row = 4, column=1)
        self.button_8.grid(row = 4, column=2)
        self.button_9.grid(row = 4, column=3)
        self.button_multiplicate.grid(row = 4, column=4)
        # fourth row
        self.button_4.grid(row = 5, column=1)
        self.button_5.grid(row = 5, column=2)
        self.button_6.grid(row = 5, column=3)
        self.button_subtraction.grid(row = 5, column=4)
        # fifth row
        self.button_1.grid(row = 6, column=1)
        self.button_2.grid(row = 6, column=2)
        self.button_3.grid(row = 6, column=3)
        self.button_plus.grid(row= 6, column=4)
        # sixth row
        self.button_signal.grid(row = 7, column=1)
        self.button_zero.grid(row = 7,column=2)
        self.button_spot.grid(row = 7, column=3)
        self.button_equal.grid(row= 7, column=4)


    def pulse_number(self, number):
        self.screen_number.set(self.screen_number.get() + number)

    def pulse_symbol(self, symbol):
        self.screen_number.set(self.screen_number.get() + symbol)

    def clear_display(self):
        self.screen_number.set("")

    def undo(self):
        list = self.screen_number.get()
        if len(list):
            new_list = list[:-1]
            self.screen_number.set(new_list)

    def calculate(self):
        global result
        screen_state = self.screen_number.get()
        try:
            math_expression = parser.expr(screen_state).compile()
            result = eval(math_expression)
            self.clear_display()
            self.screen_number.set(result)
        except expression as identifer:
            self.clear_display()
            self.screen_number.set("Error")

    def ans(self):
        global result
        self.screen_number.set(result)


















        #self.quit = tk.Button(self, text="QUIT", fg="red",
                            #command = self.master.destroy)
        #self.quit.pack(side="bottom")
