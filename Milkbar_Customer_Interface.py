from tkinter import *  # imports everything from tkinter to make this work
import os.path  # imports os.path to make find and delete work

# main menu window
main_menu = Tk()  # estabilises window
main_menu.iconbitmap("Milkbar.ico")  # add an icon
main_menu.title("Customer Interface Main Menu")  # titles it
main_menu.columnconfigure(1, weight=1)  # adds weight to columns


#  common configurations
heading_fg = "white"  # heading foreground
heading_bg = "orange red"  # heading background
heading_font = ("Bahnschrift Condensed", 40, "bold")  # heading font
label_fg = "aquamarine"  # label foreground
label_font = ("arial", 15, "bold")  # label font
but_fg = "black"  # button foreground
but_bg = ""  # button background
but_font = ("arial", 15, "bold")  # button font
but_height = 5  # button height
but_width = 10  # button width
entry_font = ("arial", 15, "bold")  # entry box font
entry_cspan = 4  # entry box column span
entry_bg = "navajo white"  # entry box background
quit_fg = "red"  # quit foreground
quit_font = ("arial", 15, "bold")  # quit font

# main menu heading
label = Label(main_menu, text="Main Menu", bg=heading_bg, fg=heading_fg, bd=1)
label.config(height=2, width=20, font=heading_font)
label.pack(side=TOP, fill=BOTH)

mm_frame = Frame(main_menu)  # main menu frame

# function to close window
def window_quit(window):
    window.destroy()


# New Customer window
def new_cus_win():
    new_cus = Toplevel(main_menu)  # estabilishes the window
    new_cus.iconbitmap("Milkbar.ico")  # adds an icon
    new_cus.title("New Customer Interface")  # titles it

    # new customer entry box clear function
    def clear():
        # new customer entry boxes list
        entryboxes = [
            name1,
            name2,
            address1,
            suburb1,
            postcode1,
            state1,
            phone1,
            email1,
        ]
        # clears entry boxes
        for entry in entryboxes:
            entry.delete(0, END)

    # save text file function
    def savefile():
        import time  # imports the time module to make the function work

        global text_file  # makes text_file global

        # defines result as the local time (found from the epoch)
        result = time.localtime(time.time())
        # date variable
        date = (
            str(result.tm_year) + "-" + str(result.tm_mon) + "-" + str(result.tm_mday)
        )

        now = time.localtime(time.time())  # sets now as the current time
        # opens the specified file in the background
        file = open(
            "Accounts/"
            + str(name2.get().upper())
            + "-"
            + str(name1.get())
            + "-"
            + date
            + ".txt",
            "w",
        )  # creates a writable text file of the customer info
        file.write(
            "Date created: "
            + time.asctime(now)
            + "\n\nFirst Name: "
            + str(name1.get())
            + "\nLast Name: "
            + str(name2.get())
            + "\nAddress: "
            + str(address1.get())
            + "\nSuburb: "
            + str(suburb1.get())
            + "\nPostcode: "
            + str(postcode1.get())
            + "\nState: "
            + str(state1.get())
            + "\nPhone Number: "
            + str(phone1.get())
            +
            # writes to the text file
            "\nEmail Address: "
            + str(email1.get())
        )
        file.close()  # closes the file

    # new customer frames
    nc_frame = Frame(new_cus)  # new customer main frame
    nc_body_frame = Frame(nc_frame)  # new customer body frame
    nc_but_frame = Frame(nc_frame)  # new customer button frame

    # new customer window heading
    label0 = Label(
        new_cus, text="Add a New Customer", bg=heading_bg, fg=heading_fg, bd=1
    )
    label0.config(height=2, width=20, font=heading_font)
    label0.pack(side=TOP, fill=BOTH)

    # first name label
    label1 = Label(nc_body_frame, text="First Name", bg="white", fg=label_fg)
    label1.config(font=label_font)
    label1.grid(column=1, row=1, sticky=W)

    # frst name entry box
    name1 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    name1.grid(row=1, column=2, columnspan=entry_cspan)

    # last name label
    label2 = Label(nc_body_frame, text="Last Name", bg="white", fg=label_fg)
    label2.config(font=label_font)
    label2.grid(column=1, row=2, sticky=W)

    # last name entry box
    name2 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    name2.grid(row=2, column=2, columnspan=entry_cspan)

    # address label
    label3 = Label(nc_body_frame, text="Address", bg="white", fg=label_fg)
    label3.config(font=label_font)
    label3.grid(column=1, row=3, sticky=W)

    # address entry box
    address1 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    address1.grid(row=3, column=2, columnspan=entry_cspan)

    # suburb label
    label4 = Label(nc_body_frame, text="Suburb", bg="white", fg=label_fg)
    label4.config(font=label_font)
    label4.grid(column=1, row=4, sticky=W)

    # suburb entry box
    suburb1 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    suburb1.grid(row=4, column=2, columnspan=entry_cspan)

    # postcode label
    label5 = Label(nc_body_frame, text="Postcode", bg="white", fg=label_fg)
    label5.config(font=label_font)
    label5.grid(column=1, row=5, sticky=W)

    # postcode entry box
    postcode1 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    postcode1.grid(row=5, column=2, columnspan=entry_cspan)

    # state label
    label6 = Label(nc_body_frame, text="State", bg="white", fg=label_fg)
    label6.config(font=label_font)
    label6.grid(column=1, row=6, sticky=W)

    # state entry box
    state1 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    state1.grid(row=6, column=2, columnspan=entry_cspan)

    # phone number label
    label7 = Label(nc_body_frame, text="Phone number", bg="white", fg=label_fg)
    label7.config(font=label_font)
    label7.grid(column=1, row=7, sticky=W)

    # phone number entry box
    phone1 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    phone1.grid(row=7, column=2, columnspan=entry_cspan)

    # email address label
    label8 = Label(nc_body_frame, text="Email address", bg="white", fg=label_fg)
    label8.config(font=label_font)
    label8.grid(column=1, row=8, sticky=W)

    # email address entry box
    email1 = Entry(nc_body_frame, width=20, bg=entry_bg, font=entry_font)
    email1.grid(row=8, column=2, columnspan=entry_cspan)

    # new customer save text file button
    new_cus_save = Button(
        nc_but_frame, text="Save Customer Information", fg=but_fg, command=savefile
    )
    new_cus_save.config(font=but_font)
    new_cus_save.grid(row=0, column=0)

    # new customer clear entry boxes button
    new_cus_clear = Button(
        nc_but_frame, text="Clear Input", relief=RAISED, fg=but_fg, command=clear
    )
    new_cus_clear.config(font=but_font)
    new_cus_clear.grid(row=0, column=1)

    # new customer quit window button
    new_cus_quit = Button(
        nc_but_frame,
        text="Quit Interface Window",
        command=lambda: window_quit(new_cus),
        fg=quit_fg,
    )
    new_cus_quit.config(font=quit_font)
    new_cus_quit.grid(row=0, column=2)

    # aligns the new customer frames
    nc_but_frame.pack(side=BOTTOM, fill=BOTH)
    nc_body_frame.pack()
    nc_frame.pack()

    # keeps track of the new customer buttons
    # nc_buttons = [new_cus_save, new_cus_quit]

    # new customer widgets lists
    nc_widgets = [
        label1,
        label2,
        label3,
        label4,
        label5,
        label6,
        label7,
        label8,
        nc_frame,
        nc_body_frame,
        nc_but_frame,
    ]

    # changes all the backgrounds of non-entry boxes
    for widget in nc_widgets:
        widget["bg"] = "cornflower blue"


#    for button in nc_buttons:
#        button.config(height=but_height, width=but_width)

# find customer window
def find_cus_win():
    find_cus = Toplevel(main_menu)  # estabilishes it
    find_cus.iconbitmap("Milkbar.ico")  # adds an icon
    find_cus.title("Find Customer Interface")  # titles it

    fc_heading = Label(
        find_cus, text="Find Customer", bg=heading_bg, fg=heading_fg, bd=1
    )
    fc_heading.config(height=2, width=20, font=heading_font)
    fc_heading.pack(side=TOP, fill=BOTH)

    fc_mm_frame = Frame(find_cus)
    fc_body_frame = Frame(fc_mm_frame)
    fc_but_frame = Frame(fc_body_frame)

    label_find_box = Label(fc_body_frame, text="Enter text file name:", fg=label_fg)
    label_find_box.config(font=label_font)
    label_find_box.grid(row=0)

    fc_find_box = Entry(fc_body_frame, width=20, bg=entry_bg, font=entry_font)
    fc_find_box.grid(row=1, columnspan=entry_cspan, pady=10)

    def fc_clear():
        fc_entryboxes = [fc_find_box]

        # clears entry boxes
        for entry in fc_entryboxes:
            entry.delete(0, END)

    # find customer file function
    def find():
        # defines the customer id as the entry box input
        id = str(fc_find_box.get())

        # if the selected exists, the file will be displayed
        if os.path.exists("Accounts/" + str(id) + ".txt"):
            # display customer window
            display_cus = Toplevel(find_cus)
            display_cus.iconbitmap("Milkbar.ico")  # adds an icon
            display_cus.title(str(id) + ".txt")
            display_cus.geometry("1000x1000")

            disc_heading = Label(
                display_cus, text=str(id), bg=heading_bg, fg=heading_fg, bd=1
            )
            disc_heading.config(height=2, width=20, font=heading_font)
            disc_heading.pack(side=TOP, fill=BOTH)

            disc_mm_frame = Frame(display_cus)
            disc_but_frame = Frame(disc_mm_frame)

            # opens the specified file as readable
            file = open("Accounts/" + str(id) + ".txt", "r")
            # creates labels with the lines
            lname1 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            lname1.config(font=label_font)
            lname1.grid(column=0, row=0, sticky=W)

            lname2 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            lname2.config(font=label_font)
            lname2.grid(column=0, row=1, sticky=W)

            laddress1 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            laddress1.config(font=label_font)
            laddress1.grid(column=0, row=2, sticky=W)

            lsuburb1 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            lsuburb1.config(font=label_font)
            lsuburb1.grid(column=0, row=3, sticky=W)

            lpostcode1 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            lpostcode1.config(font=label_font)
            lpostcode1.grid(column=0, row=4, sticky=W)

            lstate1 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            lstate1.config(font=label_font)
            lstate1.grid(column=0, row=5, sticky=W)

            lphone1 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            lphone1.config(font=label_font)
            lphone1.grid(column=0, row=6, sticky=W)

            lemail1 = Label(
                disc_mm_frame, text=str(file.readline().rstrip()), fg=label_fg
            )
            lemail1.config(font=label_font)
            lemail1.grid(column=0, row=7, sticky=W)

            disc_quit = Button(
            disc_but_frame, text="Quit Customer File", command=lambda: window_quit(display_cus), fg=quit_fg
            )
            disc_quit.config(font=quit_font)
            disc_quit.grid(row=0)

            disc_mm_frame.pack(fill=BOTH)
            disc_but_frame.grid(row=8)

            disc_widgets = [
                lname1,
                lname2,
                laddress1,
                lsuburb1,
                lpostcode1,
                lstate1,
                lphone1,
                lemail1,
                disc_mm_frame,
                disc_but_frame
            ]

            # changes all the backgrounds of non-entry boxes
            for widget in disc_widgets:
                widget["bg"] = "cornflower blue"

    fc_find_but = Button(
        fc_but_frame, text="Find Customer Information", fg=but_fg, command=find
    )
    fc_find_but.config(font=but_font)
    fc_find_but.grid(row=0, column=0)

    fc_clear = Button(
        fc_but_frame, text="Clear Input", relief=RAISED, fg=but_fg, command=fc_clear
    )
    fc_clear.config(font=but_font)
    fc_clear.grid(row=0, column=1)

    fc_quit = Button(
    fc_but_frame, text="Quit Interface Menu", command=lambda: window_quit(find_cus), fg=quit_fg
    )
    fc_quit.config(font=quit_font)
    fc_quit.grid(row=0, column=2)

    fc_mm_frame.pack()
    fc_body_frame.pack(fill=BOTH)
    fc_but_frame.grid(row=2)

    fc_widgets = [fc_mm_frame, fc_body_frame, fc_but_frame, label_find_box]

    # changes all the backgrounds of non-entry boxes
    for widget in fc_widgets:
        widget["bg"] = "cornflower blue"


# delete customer window
def del_cus_win():
    del_cus = Toplevel(main_menu)  # estabilishes the window
    del_cus.iconbitmap("Milkbar.ico")  # adds an icon
    del_cus.title("Delete Customer Interface")  # titles the window

    # delete customer heading
    dc_heading = Label(
        del_cus, text="Delete a Customer", bg=heading_bg, fg=heading_fg, bd=1
    )
    dc_heading.config(height=2, width=20, font=heading_font)
    dc_heading.pack(side=TOP, fill=BOTH)

    # delete customer clear entry boxes function
    def clear():
        entryboxes = [del_customer_txt]

        # clears entry boxes
        for entry in entryboxes:
            entry.delete(0, END)

    # delete customer delete text file
    def delete():
        id = del_customer_txt.get()

        if os.path.exists("Accounts/" + str(id) + ".txt"):
            os.remove("Accounts/" + str(id) + ".txt")

    # delete customer frames
    dc_frame = Frame(del_cus)  # delete customer main frame
    dc_body_frame = Frame(dc_frame)  # delete customer body frame
    dc_entry_frame = Frame(dc_body_frame)  # delete customer entry box frame
    dc_but_frame = Frame(dc_frame)  # delete customer button frame

    # delete customer entry box label
    label_del_customer_txt = Label(
        dc_body_frame, text="Enter text file name:", fg=label_fg
    )
    label_del_customer_txt.config(font=label_font)
    label_del_customer_txt.grid(row=0)

    # delete customer customer text file name input
    del_customer_txt = Entry(dc_entry_frame, width=20, bg=entry_bg, font=entry_font)
    del_customer_txt.grid(row=1, columnspan=entry_cspan)

    # delete customer delete text file button
    del_cus_but = Button(
        dc_but_frame, text="Delete Customer", command=delete, fg=but_fg
    )
    del_cus_but.config(font=but_font)
    del_cus_but.grid(row=0, column=0)

    # delete customer clear entry box button
    del_cus_clear = Button(
        dc_but_frame, text="Clear Input", relief=RAISED, fg=but_fg, command=clear
    )
    del_cus_clear.config(font=but_font)
    del_cus_clear.grid(row=0, column=1)

    # delete customer quit window button
    del_cus_quit = Button(
        dc_but_frame,
        text="Quit Interface Window",
        command=lambda: window_quit(del_cus),
        fg=quit_fg,
    )
    del_cus_quit.config(font=quit_font)
    del_cus_quit.grid(row=0, column=2)

    # aligns the frames
    dc_entry_frame.grid(row=1, pady=10)
    dc_body_frame.grid(row=0, pady=5)
    dc_but_frame.grid(row=2)
    dc_frame.pack(fill=BOTH)

    # delete customer widgets list
    dc_widgets = [
        label_del_customer_txt,
        dc_frame,
        dc_entry_frame,
        dc_body_frame,
        dc_but_frame,
    ]

    # changes all the backgrounds of non-entry boxes
    for widget in dc_widgets:
        widget["bg"] = "cornflower blue"


# main menu new customer window button
new_cus_but = Button(
    mm_frame, text="New Customer Window", command=new_cus_win, fg=but_fg
)
new_cus_but.config(font=but_font)
new_cus_but.grid(row=1, column=0)

# main menu find customer window button
find_cus_but = Button(
    mm_frame, text="Find Customer Window", command=find_cus_win, fg=but_fg
)
find_cus_but.config(font=but_font)
find_cus_but.grid(row=1, column=1)

# main menu delete customer window button
del_cus_but = Button(
    mm_frame, text="Delete Customer Window", command=del_cus_win, fg=but_fg
)
del_cus_but.config(font=but_font)
del_cus_but.grid(row=1, column=2)

# main menu quit button
main_menu_quit = Button(
    mm_frame, text="Quit Program", command=lambda: window_quit(main_menu), fg=quit_fg
)
main_menu_quit.config(font=quit_font)
main_menu_quit.grid(row=1, column=3)

# main menu buttons list
mm_buttons = [new_cus_but, find_cus_but, del_cus_but, main_menu_quit]

# main menu buttons config
for button in mm_buttons:
    button.config(height=5, width=25)

mm_frame.pack()  # aligns the frame

main_menu.mainloop()  # executes the main menu code
