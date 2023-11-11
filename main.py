import tkinter
from random import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
import numpy as np
import random


def on_canvas_configure(event):
    # Update the scroll region to match the size of the inner frame
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))
if __name__ == '__main__':
    root = tkinter.Tk();
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.title("Intel Project")
    root.configure(bg='#fdfcfa')
    # creating a main frame
    main_frame = Frame(root,bg="red")
    main_frame.pack(fill=BOTH, expand=1, pady=10)
    # creating canvas
    my_canvas = Canvas(main_frame, bg="pink")

    my_canvas.pack(fill=BOTH, side=LEFT, expand=1)
    # adding scrollbar
    my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scroll.pack(side=RIGHT, fill=Y)
    # configure the canvas
    #my_canvas.focus_set()
    my_canvas.configure(yscrollcommand=my_scroll.set)
    my_canvas.bind('<Configure>', on_canvas_configure)
    #my_canvas.bind("<Up>", lambda event: my_canvas.yview_scroll(-1, "units"))
    #my_canvas.bind("<Down>", lambda event: my_canvas.yview_scroll(1, "units"))



    # for graoh1
    g1 = Image.open("graph1.png")
    g1_resize = g1.resize((400, 400))
    banner_g1 = ImageTk.PhotoImage(g1_resize)
    # graph2
    g2 = Image.open("graph2.png")
    g2_resize = g2.resize((400, 400))
    banner_g2 = ImageTk.PhotoImage(g2_resize)
    # graph3
    g3 = Image.open("graph3.png")
    g3_resize = g3.resize((400, 400))
    banner_g3 = ImageTk.PhotoImage(g3_resize)
    # graoh4
    g4 = Image.open("graph4.png")
    g4_resize = g4.resize((400, 400))
    banner_g4 = ImageTk.PhotoImage(g4_resize)
    # graoh5
    g5 = Image.open("graph5.png")
    g5_resize = g5.resize((400, 400))
    banner_g5 = ImageTk.PhotoImage(g5_resize)
    # graoh6
    g6 = Image.open("graph6.png")
    g6_resize = g6.resize((400, 400))
    banner_g6 = ImageTk.PhotoImage(g6_resize)
    #graph7 for novelty
    g7 = Image.open("graph3.png")
    g7_resize = g7.resize((500, 500))
    banner_g7 = ImageTk.PhotoImage(g7_resize)

    scale_value = DoubleVar()


    # functions
    def print_scale_value():
        print("Scale value:", str(scale.get()))


    def on_radio_button_change():
        if var1.get() == "Error Percentage":
            scale.place(x=110, y=115)
            print("Error or Latency:", var1.get())

        else:
            print("Error or Latency:", var1.get())
            scale.place_forget()


    def encryption_value():
        encryption_selected = encryption.get()
        print("Encryption Selected: ", encryption_selected)


    # for graphs
    def graph():
        if (var1.get() == "Error Percentage" and encryption.get() == "AES"):
            label7 = Label(frame5, image=banner_g1, bd=0)
            label7.place(x=90, y=50)
        elif (var1.get() == "Error Percentage" and encryption.get() == "Kyber"):
            label7 = Label(frame5, image=banner_g2, bd=0)
            label7.place(x=90, y=50)
        elif ((var1.get() == "Error Percentage" and encryption.get() == "Delithium")):
            label7 = Label(frame5, image=banner_g3, bd=0)
            label7.place(x=9, y=50)
        elif ((var1.get() == "Latency" and encryption.get() == "AES")):
            label7 = Label(frame5, image=banner_g4, bd=0)
            label7.place(x=90, y=50)
        elif ((var1.get() == "Latency" and encryption.get() == "Kyber")):
            label7 = Label(frame5, image=banner_g5, bd=0)
            label7.place(x=90, y=50)
        else:
            label7 = Label(frame5, image=banner_g6, bd=0)
            label7.place(x=90, y=50)
        #for novelty

        label8=Label(frame6,image=banner_g7,bd=0)
        label8.place(x=1200,y=50)


    def answer():
        # rp = int(r.get())
        rp = random.randint(1, 10)
        my_font3 = customtkinter.CTkFont(family="Arial", size=30)
        if rp % 2 == 0:
            print("Success")
            answer = customtkinter.CTkLabel(frame4, text="Success!", fg_color="#50C878", width=150, font=my_font3,
                                            text_color="black")
            answer.place(x=300, y=365)
            graph()


        else:
            print("Failure")
            answer = customtkinter.CTkLabel(frame4, text="Failure!", fg_color="red", width=150, font=my_font3,
                                            text_color="white")
            answer.place(x=300, y=365)


    def start():
        print_scale_value()  # printing error percentage
        label4 = Label(frame4, text="Key Generated:", font=('Arial 30'), fg='black', bg="white")
        label4.place(x=20, y=35)
        # randomkeygeneration
        r = random.randint(100000, 200000)
        label5 = Label(frame4, text=r, font=('Arial 30'), fg='black', bg="white")
        label5.place(x=300, y=35)
        print("Key Generated:", r)

        # authenticate button
        b2 = customtkinter.CTkButton(frame4, width=150, height=8, text="Authenticate", border_width=1, hover=True,
                                     fg_color="black",
                                     font=my_font_button, border_spacing=10, anchor="center", corner_radius=5,
                                     hover_color="grey", text_color="white", command=answer).place(x=180, y=200)
        # result
        label6 = Label(frame4, text="Result:", font=('Arial 30'), fg='black', bg="white")
        label6.place(x=90, y=365)
    # another frame in canvas

    # frame1 for heading
    frame1 = Frame(my_canvas, height=170, width=width, bg="white",highlightbackground="#E9B840", highlightthickness=4)
    frame1.place(x=0, y=0,anchor='nw')

    # for heading
    label1 = Label(frame1, text="CONTENT MANAGEMENT SCHEME", font=('Arial 50 bold'), fg="black", bg="white");
    label1.place(x=470, y=35)

    # for logo image
    image1 = Image.open("logo.png")
    banner1 = ImageTk.PhotoImage(image1)
    labelh = Label(frame1, image=banner1, bd=0)
    labelh.place(x=690, y=110)

    # frame2 for description
    frame2 = Frame(my_canvas, height=180, width=width, bg="white",highlightbackground="#2D67B0", highlightthickness=4)
    frame2.place(x=0, y=170)

    # frame3 for inputs
    frame3 = Frame(my_canvas, height=500, width=width / 3, bg="white", highlightbackground="#E9B840", highlightthickness=4)
    frame3.place(x=0, y=350)

    # frame4 for output
    frame4 = Frame(my_canvas, height=500, width=width / 3, bg="white", highlightbackground="#E9B840", highlightthickness=4)
    frame4.place(x=576, y=350)

    # frame5 for graphs
    frame5 = Frame(my_canvas, height=500, width=width / 3, bg="white", highlightbackground="#E9B840", highlightthickness=4)
    frame5.place(x=1152, y=350)

    # frame6 for novelties
    frame6 = Frame(my_canvas, height=600, width=width, bg="white", highlightbackground="#2D67B0", highlightthickness=4)
    frame6.place(x=0, y=850)

    # for authors
    a1 = Label(frame1, text="Authors:", font=('Arial 20 bold'), fg="black", bg="white")
    a1.place(x=1560, y=10)
    a2 = Label(frame1, text="Dr Bernand Cambou", font=('Arial 20 bold'), fg="black", bg="white")
    a2.place(x=1500, y=35)
    a3 = Label(frame1, text="Saloni Jain", font=('Arial 20 bold'), fg="black", bg="white")
    a3.place(x=1550, y=60)
    a4 = Label(frame1, text="Ashwija", font=('Arial 20 bold'), fg="black", bg="white")
    a4.place(x=1570, y=85)
    a5 = Label(frame1, text="Amisha Bagri", font=('Arial 20 bold'), fg="black", bg="white")
    a5.place(x=1535, y=110)

    # for input values
    var1 = StringVar(frame3, "Error Percentage")
    r1 = Radiobutton(frame3, text="Error Percentage", variable=var1, value="Error Percentage", fg="black",
                     font=('Arial 30'), bg="white", command=on_radio_button_change)
    r1.place(x=20, y=35)
    r2 = Radiobutton(frame3, text="Latency", variable=var1, value="Latency", bg="white", fg="black", font=('Arial 30'),
                     command=on_radio_button_change)
    r2.place(x=350, y=35)

    scale = Scale(frame3, from_=0, to=20, orient=HORIZONTAL, troughcolor="#fdfcfa", variable=scale_value,
                  length=300, width=20)
    scale.place(x=110, y=115)

    label3 = Label(frame3, text="Encryption:", font=('timesnewroman 30'), fg='black', bg="#fdfcfa")
    label3.place(x=35, y=200)

    # encryption values
    my_font1 = customtkinter.CTkFont(family='timesnewroman', size=30)
    encryption = StringVar()
    radiobutton3 = customtkinter.CTkRadioButton(frame3, text="AES", variable=encryption, value="AES", font=my_font1,
                                                text_color="black", bg_color="white", command=encryption_value)
    radiobutton3.place(x=250, y=208)
    radiobutton4 = customtkinter.CTkRadioButton(frame3, text="Kyber", variable=encryption, value=2, font=my_font1,
                                                text_color="black", bg_color="white", command=encryption_value)
    radiobutton4.place(x=250, y=260)
    radiobutton5 = customtkinter.CTkRadioButton(frame3, text="Delithium", variable=encryption, value=3, font=my_font1,
                                                text_color="black", bg_color="white", command=encryption_value)
    radiobutton5.place(x=250, y=312)

    # start button
    my_font_button = customtkinter.CTkFont(family='Arial', size=30, weight='bold')
    b1 = customtkinter.CTkButton(frame3, width=150, height=8, text="Start", border_width=1, hover=True,
                                 fg_color="black",
                                 font=my_font_button, border_spacing=10, anchor="center", corner_radius=5,
                                 hover_color="grey", text_color="white", command=start).place(x=200, y=410)

    my_canvas.update_idletasks()
    # adding new frame to window in thta canvas
    my_canvas.create_window((0, 0), window=frame1, anchor='nw')
    my_canvas.create_window((0, 170), window=frame2, anchor='nw')
    my_canvas.create_window((0, 350), window=frame3, anchor='nw')
    my_canvas.create_window((576, 350), window=frame4, anchor='nw')
    my_canvas.create_window((1152, 350), window=frame5, anchor='nw')
    my_canvas.create_window((0, 850), window=frame6, anchor='nw')









    # button

    root.mainloop()
