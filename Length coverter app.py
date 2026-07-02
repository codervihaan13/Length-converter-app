from tkinter import *
def convert():
    num = float(entry.get())
    result = num * 2.54
    label_result.config(text="Centimetres: " + str(result))
window=Tk()
window.title("Length Converter App")
window.geometry("400x400")
label=Label(text="Inches:",fg="black",bg="white",height=1,width=250)
entry=Entry(window,fg="black",bg="white")
label.pack()
entry.pack()
btn = Button(window, text="Convert", command=convert)
btn.pack()
label_result = Label(window, text="Centimetres: ")
label_result.pack()
window.mainloop()