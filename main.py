from calculator import Calculator
import tkinter as tk

def main():
    root = tk.Tk()
    calculator = Calculator(master=root)
    calculator.make_grid()
    calculator.mainloop()

if __name__ == "__main__":
    main()
