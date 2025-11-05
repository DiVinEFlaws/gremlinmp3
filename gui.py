import tkinter as tk

def draw_arc(event):
    print("drawing an arc")

    # Clear the canvas before drawing again
    event.widget.delete("all")

    width = event.width
    height = event.height

    # Coordinates for right-side semi-circle
    x1, y1, x2, y2 = width / 2, 0, width, height
    event.widget.create_arc(x1, y1, x2, y2, start=90, extent=180, style=tk.ARC, width=3)

def move_up(event=None):
    print("navigating up")

def move_down(event=None):
    print("navigating down")

def up_directory(event=None):
    print("moving up a directory")

def enter_directory(event=None):
    print("entering a directory or executing a file")

def main():
    root = tk.Tk()
    root.title("File Navigator")
    root.geometry("480x320")

    canvas = tk.Canvas(root, width=480, height=320)
    canvas.pack(fill="both", expand=True)

    # Bind resizing to dynamic arc drawing
    canvas.bind("<Configure>", draw_arc)

    # Bind keyboard navigation
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)
    root.bind("<Left>", up_directory)
    root.bind("<Right>", enter_directory)

    root.mainloop()

if __name__ == "__main__":
    print("Starting the GUI application...")
    main()
