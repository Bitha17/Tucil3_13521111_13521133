import customtkinter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk
import os 
# import main as main
import astar
import visualize as v
import readfile as r
from tkinter import filedialog

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set background color
        App.configure(self,fg_color="#C1CEFE")
        self.geometry("1100x650")
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
        frame1 = customtkinter.CTkFrame(self, corner_radius=10, fg_color="#7189FF")
        frame1.pack(pady=0,padx=70,side="left")

        frame2 = customtkinter.CTkFrame(self, corner_radius=10, fg_color="#7189FF")
        frame2.pack(pady=0,padx=40,side="left")

        frame3 = customtkinter.CTkFrame(self, corner_radius=10, fg_color="#7189FF")
        frame3.pack(pady=0,padx=40,side="left")

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
            self.canvas.get_tk_widget().grid(row=0,column=0, padx=10, pady=10)

        # Create the button
        select_file_button = customtkinter.CTkButton(frame1, text="Select File", width = 100, height = 32, border_width = 1, fg_color="#758EC2", command=select_file)
        select_file_button.grid(padx=50,pady=50, row=1,column=0)

        def calculate():
            start_name = input_field1.get()
            end_name = input_field2.get()

            for node in graph.nodes:
                if node.name == start_name:
                    start = node
                if node.name == end_name:
                    end = node

            path, dist = astar.astar(start, end)

            # Create a Figure object and add a subplot to it
            self.fig = Figure(figsize=(5, 5), dpi=50)
            self.ax = self.fig.add_subplot(111)
            v.visualize2(graph, path, adj, coor,self.ax)
            # Create a canvas for the Figure and add it to the GUI
            self.canvas = FigureCanvasTkAgg(self.fig, master=frame3)
            self.canvas.get_tk_widget().grid(row=0,column=0, padx=10, pady=10)

            if path is not None:
                ans = "Path: "
                for node in path:
                    ans += node.name
                ans += "\n"
                ans += ("distance = " + str(dist))
                res = tk.StringVar(value=ans)
                res_label = customtkinter.CTkLabel(master=frame3,
                                                textvariable=res,
                                                text_font=("MV Boli",10),
                                                corner_radius=8)
            else:
                res = tk.StringVar(value="No path found")
                res_label = customtkinter.CTkLabel(master=frame3,
                                                textvariable=res,
                                                text_font=("MV Boli",15),
                                                corner_radius=15)

            res_label.grid(row=1, column=0,padx=30)

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
