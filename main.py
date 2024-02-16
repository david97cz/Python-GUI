import tkinter as tk
from datetime import datetime

#define colors
color_background = "#57467B"
color_text = "#CAFE48"


class PanelBackground:
    def __init__(self,root):
        self.root = root
        #tkinter variable
        self.boolean_value1 = tk.BooleanVar()
        root.title("Boiler SCADA")
        root.geometry("600x400")
        root.configure(background="#7CB4B8")
        #root.resizable(False,False)

        # Create Frame
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        #Create canvas
        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.grid(row=0, column=1)

        #self.canvas_background = tk.Canvas(self.root, width=600, height=200, bg='gray')
        #self.canvas_background.pack()

        # Create Frame
        self.frame_indicator = tk.Frame(self.root, relief=tk.SUNKEN)
        self.frame_indicator.grid(row=1, column=1)




        #Load image (only .gif)
        self.python_image= tk.PhotoImage(file="boiler.gif")

        #Put image into the canvas
        self.canvas.create_image(0,0,anchor=tk.NW,image=self.python_image)

        #Draw circle into the canvas
        self.circle = self.canvas.create_oval(110, 110, 130, 130, outline="black", fill="blue", width=2)

        #Create label
        self.label = tk.Label(self.frame_indicator, text="Boiler is OFF",bg=color_background,fg =color_text,font=("Helvetica", 16), pady = 20)
        self.label.pack(side=tk.LEFT)

        #Create Button
        self.button = tk.Button(self.frame_indicator, text="Print Status", command=self.print_text, bg=color_background,fg =color_text,pady = 20,font=("Helvetica", 16))
        self.button.pack(side=tk.LEFT)

        self.check_button = tk.Checkbutton(self.frame,text='Boiler Switch',bg=color_background,fg =color_text,selectcolor="#57467B",variable = self.boolean_value1, onvalue=True, offvalue=False, command=self.boolean_indicator,pady = 20,font=("Helvetica", 16))
        self.check_button.pack(anchor = tk.W, padx = 10)

        #create Input Field
        self.entry = tk.Entry(self.frame,font=("Helvetica", 16))
        self.entry.pack(anchor = tk.W, padx = 10)

        #create Spin Box
        self.spin_box = tk.Spinbox(self.frame,from_=0, to=10,font=("Helvetica", 26),width=5,increment=0.5)
        self.spin_box.pack(anchor = tk.W, padx = 10)


    def print_text(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print('Read text: ', self.entry.get())
        print('Value: ',self.spin_box.get())
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


