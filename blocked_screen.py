import tkinter

class BlockedScreen:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Blocked Screen")
        self.root.geometry("400x300")
        self.root.configure(bg="red")

        label = tkinter.Label(self.root, text="Access Denied", font=("Arial", 24), bg="red", fg="white")
        label.pack(expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        pass  # Prevent closing the window

    def show(self):
        self.root.mainloop()