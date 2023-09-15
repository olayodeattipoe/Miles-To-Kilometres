from tkinter import *

# windows
window = Tk()
window.title("Converter")
window.minsize(width=400, height=300)

# Labels
miles_label = Label(text='Miles', font=("Arial", 12, 'bold'))
miles_label.place(x=300, y=20)

kilometres_label = Label(text="Kilometres", font=("Arial", 12, "bold"))
kilometres_label.place(x=300, y=50)

# entry boxes
entry1 = Entry(width=10)
entry1.place(x=220, y=20)


entry2 = Entry(width=10)
entry2.place(x=220, y=50)

# function


def convert():
    user_input = int(entry1.get())
    answer = str(user_input * 1.609)
    entry2.insert(END, string=answer)


# buttons
button = Button(text="Calculate", font=("New Times Roman", 12, 'bold'), command=convert)
button.place(x=120, y=70)


window.mainloop()
