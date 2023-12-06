import tkinter
from random import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
import numpy as np
import random
import webbrowser


from aboutus import aboutus

#for novelties


def main():
    root = tkinter.Tk();
    root.state('zoomed')
    width = root.winfo_width()
    # height = root.winfo_screenheight()
    # root.geometry("%dx%d" % (width, height))
    root.title("Intel Project")
    root.configure(bg='#f3f3f3')
    global frame2, frame3, frame4, frame5, frame6, scale_value
    frame2 = ttk.Frame(root, relief="ridge", borderwidth=5)
    frame3 = ttk.Frame(root, relief="ridge", borderwidth=5)
    frame4 = Frame(root, height=565, width=518, bg="#f3f3f3", highlightbackground="#0068b5", highlightthickness=4)
    frame5 = Frame(root, height=565, width=518, bg="#f3f3f3", highlightbackground="#0068b5", highlightthickness=4)
    frame6 = Frame(root, height=565, width=518, bg="#f3f3f3", highlightbackground="#0068b5", highlightthickness=4)
    #global variables
    encryption = StringVar()
    scale_value = DoubleVar()
    scale = Scale(frame4, from_=0, to=3, orient=HORIZONTAL, troughcolor="#fdfcfa", variable=scale_value,
                  length=300, width=20, resolution=0.1)

    var1 = StringVar()

    #for introduction frame
    def intro():
        # if frame4.winfo_exists():
        #     frame4.destroy()
        # if frame5.winfo_exists():
        #     frame5.destroy()
        # if frame6.winfo_exists():
        #     frame6.destroy()

        frame2.place(x=40, y=245, relwidth=0.95, relheight=0.68)
        heading_font = ("Arial", 38, "bold")
        heading_label = ttk.Label(frame2, text="What is this project about?", font=heading_font, foreground="#0068b5")
        heading_label.pack(pady=10)
        # for displaying the points
        intro_pts = """In this project, the primary objective is to design a reliable and lightweight 
                solution for securing the content of Intel's industrial IoT devices with Physical Unclonable Function (PUF). 

                The protocol introduces the use of commercially available SRAM PUF for initial key generation and key 
                recovery.
                Since PUFs are affected by environmental factors,they are prone to errors. 
                Therefore error correction code is used to correct the errors in the keys generated from the PUF. 
                In order to add an additional layer of security a double encryption technique using cryptographic algorithms
                like AES-128 and AES-256 is implemented. For future proofing against quantum computing challenges,
                CRYSTAL Kyber is also used. BCH or RS error correcting codes are used to identify and resolve 
                the error by using helper data.
                The protocol offers low latency and security which is an efficient way to connect IoT devices."""

        intro_label = Label(frame2, text=intro_pts, justify="center", font=('Arial 20'))
        intro_label.place(x=20, y=100)



    #for novelty display frame
    def novelty():
        # for novelties
        frame4.destroy()
        frame5.destroy()
        frame6.destroy()

        frame3.place(x=40,y=245,relwidth=0.95, relheight=0.68)
        # heading
        heading_font = ("Arial", 40, "bold")
        heading_label = ttk.Label(frame3, text="Novelties", font=heading_font, foreground="#0068b5")
        heading_label.pack(pady=5)
        # for displaying the points
        points_txt = """
                1. Sensitive information and keys are never saved.

                2. Through the use of the enrollment process, the error rate is reduced to 0.5% (as compared to industry),allowing for the use of light-weight 
                ECC which results in a reduction in latency.

                3. Bit Error Rate (BER):10-5 (20° C ) using 800 enrolments.

                4. Fast key generation 256bits : <35ms , 384bits<60ms.

                5. Post quantum cryptographic protocols like CRYSTALKyber are used to protect against
                 quantum computing challenges.

                6. Implementation of Ternary Addressable Public Key Infrastructure (TAPKI) to select memory cells.

                7. High level of randomness.

                8. Use inherent noise as an advantage to increase randomness.
            """

        points_label = Label(frame3, text=points_txt, justify="left", font=('Arial 15'))
        points_label.place(x=20, y=70)
    # label8 = None
    # label9 = None
    # label10 = None
    # label11 = None
    # label12 = None
    # label13 = None
    # label14 = None
    # label15 = None
    # label16 = None
    # label17 = None
    #
    #
    #
    #
    # # for graoh1
    # g1 = Image.open("graph1.png")
    # g1_resize = g1.resize((400, 400))
    # banner_g1 = ImageTk.PhotoImage(g1_resize)
    # # graph2
    # g2 = Image.open("graph2.png")
    # g2_resize = g2.resize((400, 400))
    # banner_g2 = ImageTk.PhotoImage(g2_resize)
    # # graph3
    # g3 = Image.open("graph3.png")
    # g3_resize = g3.resize((400, 400))
    # banner_g3 = ImageTk.PhotoImage(g3_resize)
    # # graoh4
    # g4 = Image.open("graph4.png")
    # g4_resize = g4.resize((400, 400))
    # banner_g4 = ImageTk.PhotoImage(g4_resize)
    # # graoh5
    # g5 = Image.open("graph5.png")
    # g5_resize = g5.resize((400, 400))
    # banner_g5 = ImageTk.PhotoImage(g5_resize)
    # # graoh6
    # g6 = Image.open("graph6.png")
    # g6_resize = g6.resize((400, 400))
    # banner_g6 = ImageTk.PhotoImage(g6_resize)
    # # graph7 for novelty
    # g7 = Image.open("graph3.png")
    # g7_resize = g7.resize((500, 500))
    # banner_g7 = ImageTk.PhotoImage(g7_resize)
    #
    scale_value = DoubleVar()

    #
    #
    # # functions
    # def label_deletion():
    #     # labels_to_destroy = [label8]
    #
    #     for widget in labels_to_destroy:
    #         if widget:
    #             widget.destroy()


    def print_scale_value():
        print("Scale value:", str(scale.get()))

    #
    #
    def on_radio_button_change():
        # global label8
        if var1.get() == "Error Percentage":
            scale.place(x=110, y=115)
            print("Error or Latency:", var1.get())
            # label_deletion()

        else:
            print("Error or Latency:", var1.get())
            scale.place_forget()
            if var1.get() == "Latency":
                pass
                # label8.destroy()
                # label_deletion()


    #
    def encryption_value():
        encryption_selected = encryption.get()
        print("Encryption Selected: ", encryption_selected)

    #
    # # for graphs
    # def graph():
    #     global label8
    #     global label9
    #     global label10
    #     global label11
    #     global label12
    #     global label13
    #     global label14
    #     global label15
    #     global label16
    #     global label17
    #     if (var1.get() == "Error Percentage" and encryption.get() == "AES"):
    #         label7 = Label(frame5, image=banner_g1, bd=0)
    #         label7.place(x=90, y=50)
    #     elif (var1.get() == "Error Percentage" and encryption.get() == "Kyber"):
    #         label7 = Label(frame5, image=banner_g2, bd=0)
    #         label7.place(x=90, y=50)
    #     elif ((var1.get() == "Error Percentage" and encryption.get() == "Delithium")):
    #         label7 = Label(frame5, image=banner_g3, bd=0)
    #         label7.place(x=9, y=50)
    #     elif ((var1.get() == "Latency" and encryption.get() == "AES")):
    #         label7 = Label(frame5, image=banner_g4, bd=0)
    #         label7.place(x=90, y=50)
    #     elif ((var1.get() == "Latency" and encryption.get() == "Kyber")):
    #         label7 = Label(frame5, image=banner_g5, bd=0)
    #         label7.place(x=90, y=50)
    #     else:
    #         label7 = Label(frame5, image=banner_g6, bd=0)
    #         label7.place(x=90, y=50)

    def answer():
        # rp = int(r.get())
        rp = random.randint(1, 10)
        my_font3 = customtkinter.CTkFont(family="Arial", size=30)
        if rp % 2 == 0:
            print("Success")
            answer = customtkinter.CTkLabel(frame5, text="Success!", fg_color="#50C878", width=150, font=my_font3,
                                            text_color="black")
            answer.place(x=300, y=365)
            # graph()


        else:
            print("Failure")
            answer = customtkinter.CTkLabel(frame5, text="Failure!", fg_color="red", width=150, font=my_font3,
                                            text_color="white")
            answer.place(x=300, y=365)

    def start():
        print_scale_value()  # printing error percentage
        label4 = Label(frame5, text="Key Generated:", font=('Arial 20'), fg='#333333', bg="#f3f3f3")
        label4.place(x=30, y=35)
        # randomkeygeneration
        r = random.randint(100000, 200000)
        label5 = Label(frame5, text=r, font=('Arial, 20'), fg='#333333', bg="#f3f3f3")
        label5.place(x=300, y=35)
        print("Key Generated:", r)

        # authenticate button
        my_font_button = customtkinter.CTkFont(family='Arial', size=30, weight='bold')
        b2 = customtkinter.CTkButton(frame5, width=150, height=8, text="Authenticate", border_width=1, hover=True,
                                     fg_color="black",
                                     font=my_font_button, border_spacing=10, anchor="center", corner_radius=5,
                                     hover_color="#3498DB", text_color='#FFFFFF', command=answer).place(x=150, y=200)
        # result
        label6 = Label(frame5, text="Result:", font=('Arial 20'), fg='#333333', bg="#f3f3f3")
        label6.place(x=120, y=365)

    #
    # #for author link
    # def callback(url):
    #     webbrowser.open_new_tab(url)
    #
    #
    # def on_enter(event):
    #     a1.config(fg="blue", underline=True)  # Change foreground color and underline when mouse enters
    #
    #
    # def on_leave(event):
    #     a1.config(fg="black", underline=False)  # Reset to original colors when mouse leaves
    #
    #
    #
    #
    # # another frame in canvas
    #
    #for demo
    #frame 4
    def demo():
        frame2.destroy()
        # for input values
        frame4.place(x=0, y=235)
        # # frame5 for output
        frame5.place(x=515, y=235)
        # # frame6 for graph
        frame6.place(x=1020, y=235)
        #for input
        my_font1 = customtkinter.CTkFont(family='Arial', size=25)

        r1 = customtkinter.CTkRadioButton(frame4, text = "Error Percentage", variable = var1, value = "Error Percentage",
                                          font = my_font1,command=on_radio_button_change )
        r1.place(x=20, y=35)
        r2 = customtkinter.CTkRadioButton(frame4, text = "Latency", variable = var1, value = "Latency",
                                          font = my_font1,command=on_radio_button_change )
        r2.place(x=290, y=35)


        scale.place(x=110, y=115)

        label3 = Label(frame4, text="Encryption:", font='timesnewroman 20', fg='black', bg="#f3f3f3")
        label3.place(x=35, y=200)

        # encryption values


        radiobutton3 = customtkinter.CTkRadioButton(frame4, text="AES", variable=encryption, value="AES", font=my_font1,
                                                    text_color="black", bg_color="#f3f3f3", command=encryption_value)
        radiobutton3.place(x=250, y=208)
        radiobutton4 = customtkinter.CTkRadioButton(frame4, text="Kyber", variable=encryption, value="Kyber", font=my_font1,
                                                    text_color="black", bg_color="#f3f3f3", command=encryption_value)
        radiobutton4.place(x=250, y=260)
        # start button
        my_font_button = customtkinter.CTkFont(family='Arial', size=30, weight='bold')
        b1 = customtkinter.CTkButton(frame4, width=150, height=8, text="Start", border_width=1, hover=True,
            fg_color="black",font=my_font_button, border_spacing=10, anchor="center",corner_radius=5,
            hover_color="#3498DB", text_color='#FFFFFF', command=start).place(x=160, y=360)





    # frame1 for heading
    frame1 = Frame(root, height=180, width=1550, bg="#f4f4f4")
    frame1.place(x=0, y=0, anchor='nw')
    #
    # for heading
    label1 = Label(frame1, text="CONTENT MANAGEMENT SCHEME FOR IOT DEVICES", font=('Arial 40 bold'), fg="#333333",
                   bg="#F4F4F4")
    label1.place(relx=0.5, rely=0.4, anchor='center')
    # for logo image
    image1 = Image.open("logo.png")
    banner1 = ImageTk.PhotoImage(image1)
    labelh = Label(frame1, image=banner1, bd=0)
    labelh.place(relx=0.5, y=140, anchor='center')
    #

    #custom menubar
    menu_frame = customtkinter.CTkFrame(root, fg_color="#C5C6D0", width=10, height=50)  # fg_color="#f4f4f4")
    menu_frame.place(x=0, y=200, relwidth = 1,relheight =0.04)
    f1 = customtkinter.CTkFont('Verdana', 21)
    b1 = customtkinter.CTkButton(menu_frame, text='Introduction', fg_color="transparent", text_color="#0068b5", font=f1,
                                 hover_color="black", command= intro)
    b1.pack(side="left", padx=10)
    b2 = customtkinter.CTkButton(menu_frame, text='Demo', fg_color="transparent", text_color="#0068b5", font=f1,
                                 hover_color="black", command=demo)
    b2.pack(side="left", padx=10)
    b3 = customtkinter.CTkButton(menu_frame, text='Novelties', fg_color="transparent", text_color="#0068b5", font=f1,
                                 hover_color="black", command=novelty)
    b3.pack(side="left", padx=10)
    b4 = customtkinter.CTkButton(menu_frame, text='About Us', fg_color="transparent", text_color="#0068b5", font=f1,
                                 hover_color="#808080", command=aboutus)
    b4.pack(side="left", padx=10)

    #intro part
    intro()

    # frame2 for description
    # frame2 = Frame(root, height=500, width=518, bg="#f3f3f3", highlightbackground="#0068b5", highlightthickness=4)
    # frame2.place(x=0, y=230)
    # frame2.pack_propagate(False)
    # # frame3 for output
    # frame3 = Frame(root, height=500, width=518, bg="#f3f3f3", highlightbackground="#0068b5", highlightthickness=4)
    # frame3.place(x=515, y=230)
    # # frame4 for graphs
    # frame4 = Frame(root, height=500, width=518, bg="#f3f3f3", highlightbackground="#0068b5",
    #                highlightthickness=4)
    # frame4.place(x=1020, y=230)


    # # for authors
    # a1 = Label(frame1, text="Authors:", font=('Arial 25 bold'), fg="black", bg="white",cursor="arrow")
    # a1.place(x=1550, y=10)
    # a1.bind("<Enter>", on_enter)
    # a1.bind("<Leave>", on_leave)


    root.mainloop()


if __name__ == '__main__':
    main()