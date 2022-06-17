from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser

root = Tk()
root.title("HTML IDE")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background ="cadetblue")

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))
run_img = ImageTk.PhotoImage(Image.open ("run.jpg"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.3,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,bg = "orange",width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    html_file = open(name,'r')
    paragraph=html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()

def save():
    input_name = input_file_name.get()
    file = open(input_name + ".html", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0, END)
    
def closeWindow():
    root.destroy()
    
def run_html_file():
    global name
    webbrowser.open(name)
    
    
open_button = Button(root, image = open_img, text = "Open File" ,command = openFile)
open_button.place(relx = 0.05, rely = 0.03, anchor = CENTER)

save_button = Button(root, image = save_img, text = "Save File" ,command = save)
save_button.place(relx = 0.11, rely = 0.03, anchor = CENTER)

run_button = Button(root, image = run_img, text = "Run File" ,command = run_html_file)
run_button.place(relx = 0.17, rely = 0.03, anchor = CENTER)

exit_button = Button(root, image = exit_img, text = "Close Window" ,command = closeWindow)
exit_button.place(relx = 0.23, rely = 0.03, anchor = CENTER)

root.mainloop()