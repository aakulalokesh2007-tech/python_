import tkinter as tk

class RoundButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=100, height=100, bg_color="blue", fg_color="white", **kwargs):
        super().__init__(parent, width=width, height=height, highlightthickness=0, **kwargs)
        
        self.command = command
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        
        # Create the oval (round shape) button
        self.create_oval(2, 2, self.width, self.height, outline=self.bg_color, fill=self.bg_color, tags="button")
        
        # Add text in the middle of the button
        self.create_text(self.width//2, self.height//2, text=text, fill=self.fg_color, font=("Arial", 12), tags="button")
        
        # Bind the button click event
        self.tag_bind("button", "<ButtonPress-1>", self.on_click)

    def on_click(self, event):
        if self.command:
            self.command()

def on_button_click():
    print("Round button clicked!")

root = tk.Tk()
root.title("Round Button Example")

round_button = RoundButton(root, text="Click Me", command=on_button_click, width=100, height=100, bg_color="blue", fg_color="white")
round_button.pack(pady=20)

root.mainloop()
