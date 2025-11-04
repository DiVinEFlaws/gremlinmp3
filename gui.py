import tkinter as tk

def main():
    root = tk.Tk()
    root.title("File Navigator")
    root.geometry("600x400")
    #initalize all the elements of the gui here
    # --- your widgets and layout will go here ---

    root.mainloop()

def moveup():
    print("navigating up")
def movedown():
    print("navigating down")
def upDirectory():
    print("moving up a directory")
def enterDirectory():
    print("entering a directory or executing a file")

if __name__ == "__main__":
    print("Starting the GUI application...")
    main()
