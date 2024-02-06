import tkinter as tk
from datetime import datetime


class PanelBackground:
    def __init__(self,root):
        self.root = root
        #tkinter variable
        self.boolean_value1 = tk.BooleanVar()
        root.title("Boiler SCADA")
        root.geometry("600x400")
        root.configure(background="#7CB4B8")

        #Create canvas
        self.canvas = tk.Canvas(self.root, width=600, height=200, bg='white')
        self.canvas.pack()

        #Load image (only .gif)
        self.python_image= tk.PhotoImage(file="boiler.gif")

        #Put image into the canvas
        self.canvas.create_image(0,0,anchor=tk.NW,image=self.python_image)

        #Draw circle into the canvas
        self.circle = self.canvas.create_oval(110, 110, 130, 130, outline="black", fill="blue", width=2)

        #Create label
        self.label = tk.Label(self.root, text="Boiler is OFF",bg="#57467B",fg ="#CAFE48",font=("Helvetica", 16))
        self.label.pack()

        #Create Button
        self.button = tk.Button(self.root, text="Print Status", command=self.print_text, bg="#57467B",fg ="#CAFE48")
        self.button.pack()

        self.check_button = tk.Checkbutton(self.root,text='Boiler Switch',bg="#57467B",fg ="#CAFE48",selectcolor="#57467B",variable = self.boolean_value1, onvalue=True, offvalue=False, command=self.boolean_indicator)
        self.check_button.pack()

    def print_text(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        if self.boolean_value1.get() == True:
            print("Boiler is ON")
        elif self.boolean_value1.get() == False:
            print("Boiler is OFF")
        print("__________________")


    def boolean_indicator(self):
        if self.boolean_value1.get() == True:
            self.canvas.itemconfig(self.circle, fill='red')
            self.label.config(text="Boiler is ON")
        elif self.boolean_value1.get() == False:
            self.canvas.itemconfig(self.circle, fill='blue')
            self.label.config(text="Boiler is OFF")

if __name__ == '__main__':
    root1 = tk.Tk()
    panel1 = PanelBackground(root1)
    root1.mainloop()



