from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title("Text Editor")
root.geometry('1200x660')
opened_file_name = False
selected = False


# Create new File function
def new_file():
    global opened_file_name
    opened_file_name = False
    # Delete previous text
    my_text.delete('1.0', END)
    root.title("New File")
    status_bar.config(text="New File >>>>>>>")


# Open Files
def open_file():
    # Delete previous text
    my_text.delete('1.0', END)

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir='D:/', title="Open Files", filetypes=(("Text Files", '*.txt'),
                                                                                            ("HTML Files", '*.html'),
                                                                                            ("All Files", '*.*')))
    # Check if there is a file name
    if text_file:
        global opened_file_name
        opened_file_name = text_file
    # Update Status Bars
    name = text_file
    status_bar.config(text=name)
    root.title(f'{name} - TextPad!')

    # Open the files
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to text box
    my_text.insert(END, stuff)
    text_file.close()


# Save File
def save_file():
    global opened_file_name
    if opened_file_name:
        # Save the file
        text_file = open(opened_file_name, 'w')
        text_file.write(my_text.get('1.0', END))
        text_file.close()
        status_bar.config(text=f"Saved {opened_file_name}")
    else:
        save_as()


# Save as File
def save_as():
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir='D:/',
                                             title="Save File", filetypes=(("Text Files", '*.txt'),
                                                                           ("HTML Files", '*.html'),
                                                                           ("All Files", '*.*')))
    if text_file:
        # Update Status bar
        name = text_file
        name = name.replace('D:/', "")
        status_bar.config(text=f"Saved {name}")
        root.title(f'{name}- TextPad')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get('1.0', END))
        text_file.close()


# Cut Text
def cut_text(e):
    global selected
    # Check to see if we used keyboard shortcut
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grab selected text from text box
            selected = my_text.selection_get()
            # Delete selected text from text box
            my_text.delete("sel.first", 'sel.last')
            root.clipboard_clear()
            root.clipboard_append(selected)


# Copy Text
def copy_text(e):
    global selected
    # Check to see if we used keyboard shortcut
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grab selected text from text box
            selected = my_text.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)


# Paste Text
def paste_text(e):
    global selected
    # Check to see if we used keyboard shortcut
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            # Grab cursor position
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


# Bold Text
def make_bold():
    # Create our font
    bold_font = font.Font(my_text, my_text.cget('font'))
    bold_font.configure(weight='bold')
    # Configure a tag
    my_text.tag_configure('bold', font=bold_font)
    # Define current tags
    current_tags = my_text.tag_names('sel.first')
    if 'bold' in current_tags:
        my_text.tag_remove('bold', "sel.first", 'sel.last')
    else:
        my_text.tag_add('bold', "sel.first", 'sel.last')


# Italic Text
def make_italic():
    # Create our font
    italic_font = font.Font(my_text, my_text.cget('font'))
    italic_font.configure(slant='italic')
    # Configure a tag
    my_text.tag_configure('italic', font=italic_font)
    # Define current tags
    current_tags = my_text.tag_names('sel.first')
    if 'italic' in current_tags:
        my_text.tag_remove('italic', "sel.first", 'sel.last')
    else:
        my_text.tag_add('italic', "sel.first", 'sel.last')


# Change Selected Text Color
def text_color():
    # Pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        # Create our font
        color_font = font.Font(my_text, my_text.cget('font'))
        # Configure a tag
        my_text.tag_configure('colored', font=color_font, foreground=my_color)
        # Define current tags
        current_tags = my_text.tag_names('sel.first')
        if 'colored' in current_tags:
            my_text.tag_remove('colored', "sel.first", 'sel.last')
        else:
            my_text.tag_add('colored', "sel.first", 'sel.last')


# Change BG color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)


# Change all text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)


# Create a toolbar Frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)


# Create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our scrollbar for text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Ariel", 16), selectbackground='yellow', selectforeground='black',
               undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste      ", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")

# Add Color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Colors', menu=color_menu)
color_menu.add_command(label="Change Selected", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# Add status bar to bottom of app
status_bar = Label(root, text='Ready      ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Edit Bindings
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)

# Create Buttons
bold_button = Button(toolbar_frame, text="Bold", command=make_bold)
bold_button.grid(row=0, column=0, sticky=W, padx=5)
# Italic Button
italic_button = Button(toolbar_frame, text="Italic", command=make_italic)
italic_button.grid(row=0, column=1, sticky=W, padx=5)
# Text Color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=2, padx=5)

root.mainloop()
