import tkinter as tk


class PanelBackground:
    def __init__(self,root):
        self.root = root
        root.title("A simple GUI")
        root.geometry("600x400")
        root.configure(background="green")


        self.python_image= tk.PhotoImage(file="test_image.png")
        self.label_image = tk.Label(root,image=self.python_image)
        self.label_image.pack()

        self.label = tk.Label(root, text="",bg="blue",fg ="red",font=("Helvetica", 16))
        self.label.pack()

        self.button = tk.Button(root, text="Button", command=self.print_text, bg="white",fg ="blue")
        self.button.pack()

    def print_text(self):
        self.label.config(text="Hello World")

if __name__ == '__main__':
    root1 = tk.Tk()
    panel1 = PanelBackground(root1)
    root1.mainloop()

