import tkinter as tk
from PIL import ImageTk, Image
import os
root = tk.Tk()
root.title("Image Explorer")
#root.iconbitmap(os.path.join(os.getcwd()+'/images/codemy.ico'))

try:
    file = input("Enter Relative file name (Leave blank for default):")
    if file == '':
        raise 
    if not file.startswith('./'):
        temp = './'+file
        file = temp
    filename = [f for f in os.listdir(file)]
except:
    filename = [f for f in os.listdir('./images/')]
image_list = []
for f in filename:
    try:
        img = ImageTk.PhotoImage(Image.open('images/'+f).resize((500,500)))
        image_list.append(img)
    except:
        print("Not an Image")

print(len(image_list))
my_label = tk.Label(image = image_list[0], width=500, height=500)
my_label.pack(expand=True)

def button_place():
    button_back.place(x=200, y=600)
    button_forward.place(x=1200, y=600)
    button_quit.place(x=680, y=650)
    my_label.pack(expand=True)

def back(image_no):
    global my_label
    global button_forward
    global button_back
    # Deleting the old Grid
    my_label.pack_forget()
    my_label.place_forget()
    # Remaking the Grid
    my_label = tk.Label(image=image_list[image_no-1], width=500, height=500)
    button_forward = tk.Button(root, text='>>', command=lambda: forward(image_no+1))
    button_back = tk.Button(root, text='<<', command=lambda: back(image_no-1))
    
    if image_no == 1:
        button_back = tk.Button(root, text="<<", state=tk.DISABLED)

    button_place()

def forward(image_no):
    global my_label
    global button_forward
    global button_back

    my_label.pack_forget()
    my_label.place_forget()
    my_label = tk.Label(image=image_list[image_no-1], width=500, height=500)
    button_forward = tk.Button(root, text='>>', command=lambda: forward(image_no+1))
    button_back = tk.Button(root, text='<<', command=lambda: back(image_no-1))
    
    if image_no == len(image_list)-1:
        button_forward = tk.Button(root, text=">>", state=tk.DISABLED)

    button_place()



# Initialize Buttons
button_back = tk.Button(root, text='<<', command=back, state=tk.DISABLED)
button_forward = tk.Button(root, text='>>', command=lambda:forward(2))
button_quit = tk.Button(root, text='Exit', command=root.quit)

# Placing Buttons
button_place()

root.mainloop()