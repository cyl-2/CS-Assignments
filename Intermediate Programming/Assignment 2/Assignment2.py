'''
Student Name: Chen Yu Lin
'''

from tkinter import *

class Draw(object):
    def __init__(self):
        self._root = Tk()
        tk = self._root

        # LABELS 
        self._selectionLabel = Label(tk, text="Current Selection", font=('Calibri 13 bold')).place(x=10, y=350)
        self._selectionColor = Label(tk, text="Color: ").place(x=10, y=400)
        self._colorSelected = Label(tk, text="Black")
        self._colorSelected.place(x=80, y=400)

        self._selectionShape = Label(self._root, text="Shape: ").place(x=10, y=450)
        self._shapeSelected =  Label(tk, text="Line")
        self._shapeSelected.place(x=80, y=450)

        # SHAPE BUTTONS
        self._shapeLabel = Label(tk, text="Pick a shape!").place(x=10, y=40)
        self._shape1_button = Button(tk, text='Rectangle', height = 1, width = 10, padx=5, pady=10, command=lambda: self.choose_shape('rectangle')).grid(row=0, column=0)
        self._shape2_button = Button(tk, text='Oval', height = 1, width = 10, padx=5, pady=10, command=lambda: self.choose_shape('oval')).grid(row=0, column=1)
        self._shape3_button = Button(tk, text='Line', height = 1, width = 10, padx=5, pady=10, command=lambda: self.choose_shape('line')).grid(row=0, column=2)
         
        # COLOR BUTTONS
        self._colorLabel = Label(tk, text="Pick a color!").place(x=10, y=210)
        self._color1_button = Button(tk, text='red', height = 1, width = 10, padx=5, pady=10, command=lambda: self.choose_color('red')).grid(row=1, column=0)
        self._color2_button = Button(tk, text='blue', height = 1, width = 10, padx=5, pady=10, command=lambda: self.choose_color('blue')).grid(row=1, column=1)
        self._color3_button = Button(tk, text='yellow', height = 1, width = 10, padx=5, pady=10, command=lambda: self.choose_color('yellow')).grid(row=1, column=2)

        # THE CANVAS FOR DRAWING
        self._canvas = Canvas(tk, bg='white', width=800, height=600)
        self._canvas.grid(column=3, row = 0, rowspan=4)

        self.start()
        tk.mainloop()

    def start(self):
        self._color = 'black' # a default color
        self._shape = 'line' # a default 'shape'
        self._canvas.bind('<Button-1>', self.click) 
        
    def choose_color(self, color):
        self._color = color
        self._colorSelected["text"] = color
    
    def choose_shape(self, shape):
        self._shape = shape
        self._shapeSelected["text"] = shape

    def click(self, event):
        global num_clicks, x1, y1, x2, y2

        if num_clicks == 0:
            x1 = event.x
            y1 = event.y
            num_clicks = 1
        else:
            x2 = event.x
            y2 = event.y
            self.draw()
            num_clicks=0

    def draw(self):
        if self._shape == 'oval':
            self._canvas.create_oval(x1, y1, x2, y2, outline = self._color, fill = self._color)

        if self._shape == 'rectangle':
            self._canvas.create_rectangle(x1, y1, x2, y2, outline = self._color, fill = self._color)
        
        if self._shape == 'line':
            self._canvas.create_line(x1, y1, x2, y2, fill = self._color, width = 3)

if __name__ == '__main__':
    num_clicks = 0
    Draw()