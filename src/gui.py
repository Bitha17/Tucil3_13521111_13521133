import customtkinter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk
import os 
# import main as main
import astar
import ucs
import graph as g
import copy
import visualize as v
import readfile as r
from tkinter import filedialog

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # graph = g.Graph(0)
        # adj = []
        # coor = []

        # set background color
        App.configure(self,fg_color="#C1CEFE")
        self.geometry("1900x1200")
        self.title("Shortest Path")

        # top frame
        frame = customtkinter.CTkFrame(master=self,
                               width=1050,
                               height=125,
                               corner_radius=10,
                               fg_color = "#A0DDFF",
                               border_color="white",
                               border_width=1)
        frame.pack(padx=10, pady=10)

        text_var = tk.StringVar(value="Shortest Path with A* and UCS")
        label = customtkinter.CTkLabel(master=frame,
                                    textvariable=text_var,
                                    text_font=("MV Boli",33),
                                    corner_radius=8)
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        # Frames
        frame1 = customtkinter.CTkFrame(self, fg_color="#7189FF", relief="solid", width=300)
        frame1.pack(fill="both",side="left", padx=25, pady=80)

        frame2 = customtkinter.CTkFrame(self, corner_radius=10, fg_color="#7189FF")
        frame2.pack(side="left",padx=25, pady=60)

        frame3 = customtkinter.CTkFrame(self, fg_color="#7189FF", relief="solid",width=300, height=500)
        frame3.pack(fill="both",side="left",padx=25, pady=50)

        frame4 = customtkinter.CTkFrame(self, fg_color="#7189FF", relief="solid",width=300, height=500)
        frame4.pack(fill="both",side="left",padx=25, pady=50)

        label_astar= customtkinter.CTkLabel(master=frame3, 
                                            textvariable=tk.StringVar(value="A*"),
                                            text_font=("MV Boli",15),
                                            corner_radius=50)
        label_astar.place(x=70)

        label_ucs= customtkinter.CTkLabel(master=frame4, 
                                            textvariable=tk.StringVar(value="UCS"),
                                            text_font=("MV Boli",15),
                                            corner_radius=50)
        label_ucs.place(x=70)

        def select_file():
            file_path = filedialog.askopenfilename()
            global graph
            global adj
            global coor
            graph, adj, coor = r.read_file(file_path)
            # Create a Figure object and add a subplot to it
            self.fig = Figure(figsize=(5, 5), dpi=50)
            self.ax = self.fig.add_subplot(111)
            v.visualize1(graph, adj, coor, self.ax)
            # Create a canvas for the Figure and add it to the GUI
            self.canvas = FigureCanvasTkAgg(self.fig, master=frame1)
            self.canvas.get_tk_widget().place(x=39, y=20)

        # Create the button
        select_file_button = customtkinter.CTkButton(frame1, text="Select File", width = 100, height = 32, border_width = 1, fg_color="#758EC2", command=select_file)
        select_file_button.place(x=100, y=280)

        def calculate():
            start_name = input_field1.get()
            end_name = input_field2.get()

            graph_temp = copy.deepcopy(graph)

            start = g.Node(-1,'',-1,-1)
            end = g.Node(-1,'',-1,-1)
            for node in graph_temp.nodes:
                if node.name == start_name:
                    start = node
                if node.name == end_name:
                    end = node

            if start not in graph_temp.nodes or end not in graph_temp.nodes:
                label_error= customtkinter.CTkLabel(master=frame2, 
                                            textvariable=tk.StringVar(value="Invalid start or end"),
                                            text_font=("MV Boli",10),
                                            corner_radius=8)
            else:
                label_error= customtkinter.CTkLabel(master=frame2,textvariable=tk.StringVar(value=""))
                
                path2, dist2 = ucs.ucs(start,end)

                # Create a Figure object and add a subplot to it
                self.fig = Figure(figsize=(5, 5), dpi=50)
                self.ax = self.fig.add_subplot(111)
                v.visualize2(graph, path2, adj, coor,self.ax)
                # Create a canvas for the Figure and add it to the GUI
                self.canvas = FigureCanvasTkAgg(self.fig, master=frame4)
                self.canvas.get_tk_widget().place(x=39, y=50)

                if path2 is not None:
                    ans = "Path: "
                    for node in path2:
                        ans += node.name
                    ans += "\n"
                    ans += ("distance = " + str(dist2))
                    res2 = tk.StringVar(value=ans)
                    res_label2 = customtkinter.CTkLabel(master=frame4,
                                                    textvariable=res2,
                                                    text_font=("MV Boli",10),
                                                    corner_radius=8, 
                                                    width=300)
                else:
                    res2 = tk.StringVar(value="No path found")
                    res_label2 = customtkinter.CTkLabel(master=frame4,
                                                    textvariable=res2,
                                                    text_font=("MV Boli",22),
                                                    corner_radius=8, 
                                                    width=300)
                res_label2.place(y=350)

                graph_temp = copy.deepcopy(graph)

                for node in graph_temp.nodes:
                    if node.name == start_name:
                        start = node
                    if node.name == end_name:
                        end = node
                
                path1, dist1 = astar.astar(start, end)

                # Create a Figure object and add a subplot to it
                self.fig = Figure(figsize=(5, 5), dpi=50)
                self.ax = self.fig.add_subplot(111)
                v.visualize2(graph, path1, adj, coor,self.ax)
                # Create a canvas for the Figure and add it to the GUI
                self.canvas = FigureCanvasTkAgg(self.fig, master=frame3)
                self.canvas.get_tk_widget().place(x=39, y=50)

                if path1 is not None:
                    ans = "Path: "
                    for node in path1:
                        ans += node.name
                    ans += "\n"
                    ans += ("distance = " + str(dist1))
                    res = tk.StringVar(value=ans)
                    res_label = customtkinter.CTkLabel(master=frame3,
                                                    textvariable=res,
                                                    text_font=("MV Boli",10),
                                                    corner_radius=8, 
                                                    width=300)
                else:
                    res = tk.StringVar(value="No path found")
                    res_label = customtkinter.CTkLabel(master=frame3,
                                                    textvariable=res,
                                                    text_font=("MV Boli",22),
                                                    corner_radius=8, 
                                                    width=300)
                res_label.place(y=350)

            label_error.grid(column=0, row=5)


        # Create an input field
        text1 = tk.StringVar(value="Start Node")
        label1 = customtkinter.CTkLabel(master=frame2,
                                    textvariable=text1,
                                    text_font=("MV Boli",15),
                                    corner_radius=8)
        label1.grid(row=0, column=0)
        input_field1 = customtkinter.CTkEntry(frame2)
        input_field1.grid(pady=10,padx=10,row=1,column=0)

        text2 = tk.StringVar(value="End Node")
        label2 = customtkinter.CTkLabel(master=frame2,
                                    textvariable=text2,
                                    text_font=("MV Boli",15),
                                    corner_radius=8)
        label2.grid(row=2, column=0)
        input_field2 = customtkinter.CTkEntry(frame2)
        input_field2.grid(pady=10,padx=10,row=3,column=0)

        # Create a button to get the input value
        button = customtkinter.CTkButton(frame2, text="Confirm", width=100, height=32, border_width=1, fg_color="#758EC2",command=calculate)
        button.grid(pady=20,padx=10,row=4,column=0)




if __name__ == '__main__':
    app = App()
    app.mainloop()
