import tkinter as tk
import tkinter.font as tkFont
import math

class App:
    def __init__(self, root):
        #setting title
        root.title("AREA CAKCULATOR")
        #setting window size
        width=416
        height=277
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_510=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_510["font"] = ft
        GLabel_510["fg"] = "#333333"
        GLabel_510["justify"] = "left"
        GLabel_510["text"] = "Enter length"
        GLabel_510.place(x=10,y=10,width=70,height=25)

        GLabel_585=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_585["font"] = ft
        GLabel_585["fg"] = "#333333"
        GLabel_585["justify"] = "left"
        GLabel_585["text"] = "Enter breadth"
        GLabel_585.place(x=10,y=50,width=84,height=30)

        txt_len=tk.Entry(root)
        txt_len["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_len["font"] = ft
        txt_len["fg"] = "#333333"
        txt_len["justify"] = "center"
        txt_len["text"] = ""
        txt_len.place(x=100,y=10,width=90,height=30)

        txt_brd=tk.Entry(root)
        txt_brd["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_brd["font"] = ft
        txt_brd["fg"] = "#333333"
        txt_brd["justify"] = "center"
        txt_brd["text"] = ""
        txt_brd.place(x=100,y=50,width=90,height=30)

        cmd_rectarea=tk.Button(root)
        cmd_rectarea["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        cmd_rectarea["font"] = ft
        cmd_rectarea["fg"] = "#000000"
        cmd_rectarea["justify"] = "center"
        cmd_rectarea["text"] = "Rect  area"
        cmd_rectarea.place(x=10,y=90,width=70,height=25)
        cmd_rectarea["command"] = self.rect

        GLabel_462=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_462["font"] = ft
        GLabel_462["fg"] = "#333333"
        GLabel_462["justify"] = "center"
        GLabel_462["text"] = "Enter radius"
        GLabel_462.place(x=200,y=10,width=70,height=25)

        txt_rad=tk.Entry(root)
        txt_rad["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_rad["font"] = ft
        txt_rad["fg"] = "#333333"
        txt_rad["justify"] = "center"
        txt_rad["text"] = ""
        txt_rad.place(x=280,y=10,width=90,height=30)

        cmd_cirarea=tk.Button(root)
        cmd_cirarea["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        cmd_cirarea["font"] = ft
        cmd_cirarea["fg"] = "#000000"
        cmd_cirarea["justify"] = "center"
        cmd_cirarea["text"] = "Circle area"
        cmd_cirarea.place(x=200,y=90,width=70,height=25)
        cmd_cirarea["command"] = self.circle

        GLabel_919=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_919["font"] = ft
        GLabel_919["fg"] = "#333333"
        GLabel_919["justify"] = "left"
        GLabel_919["text"] = "Enter side"
        GLabel_919.place(x=10,y=140,width=70,height=25)

        txt_side=tk.Entry(root)
        txt_side["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_side["font"] = ft
        txt_side["fg"] = "#333333"
        txt_side["justify"] = "center"
        txt_side["text"] = ""
        txt_side.place(x=100,y=140,width=90,height=30)

        cmd_sqarea=tk.Button(root)
        cmd_sqarea["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        cmd_sqarea["font"] = ft
        cmd_sqarea["fg"] = "#393d49"
        cmd_sqarea["justify"] = "center"
        cmd_sqarea["text"] = "Square area"
        cmd_sqarea.place(x=10,y=180,width=80,height=30)
        cmd_sqarea["command"] = self.square

        GLabel_883=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_883["font"] = ft
        GLabel_883["fg"] = "#333333"
        GLabel_883["justify"] = "center"
        GLabel_883["text"] = "Enter base"
        GLabel_883.place(x=210,y=130,width=70,height=25)

        GLabel_764=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_764["font"] = ft
        GLabel_764["fg"] = "#333333"
        GLabel_764["justify"] = "center"
        GLabel_764["text"] = "Enter height"
        GLabel_764.place(x=210,y=170,width=70,height=25)

        txt_base=tk.Entry(root)
        txt_base["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_base["font"] = ft
        txt_base["fg"] = "#333333"
        txt_base["justify"] = "center"
        txt_base["text"] = ""
        txt_base.place(x=290,y=130,width=90,height=30)

        txt_height=tk.Entry(root)
        txt_height["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_height["font"] = ft
        txt_height["fg"] = "#333333"
        txt_height["justify"] = "center"
        txt_height["text"] = ""
        txt_height.place(x=290,y=170,width=90,height=30)

        cmd_triarea=tk.Button(root)
        cmd_triarea["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        cmd_triarea["font"] = ft
        cmd_triarea["fg"] = "#000000"
        cmd_triarea["justify"] = "center"
        cmd_triarea["text"] = "Tri area"
        cmd_triarea.place(x=210,y=200,width=70,height=25)
        cmd_triarea["command"] = self.tri

        result_label=tk.Label(root)
        result_label["bg"] = "#f7f2f2"
        ft = tkFont.Font(family='Times',size=10)
        result_label["font"] = ft
        result_label["fg"] = "#333333"
        result_label["justify"] = "center"
        result_label["text"] = ""
        result_label.place(x=120,y=230,width=70,height=25)
    def rect(self):
        l=float(input("enter breadth:"))
        b=float(input("enter breadth:"))
        a=2*(l+b)
        self.result_label.config(text="Result: " + str(result))

    def square():
        a=float(input("enter side:"))
        c=a**2
        print(c)

    def circle():
        r=float(input("enter radius:"))
        c=math.pi*r*r
        print(c)

    def tri():
        l=float(input("enter base:"))
        b=float(input("enter height:"))
        a=0.5*l*b
        print(a)




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
