import tensorflow as tf
from tkinter import *
from ModelCommands import predict_text

length = 100
dark_mode = False

win = Tk()

length_scale = Scale(win, from_=0, to=500, length=250, width=20)
length_scale.place(x=450, y=60)

prompt = Text(win, width=50, height=25)
prompt.place(x=25, y=25)
def updateColor(event=None):
  prompt.tag_add("color", "1.0", "end")
  if dark_mode:
    prompt.tag_config("color", foreground="white")
  else:
    prompt.tag_config("color", foreground="black")
prompt.bind("<Key>", updateColor)

def extend_text():
  text = prompt.get("1.0", "end")
  print(text)
  print("\n\n" in text)
  prompt.delete("1.0", "end")
  prompt.insert("1.0", predict_text(text, length_scale.get()))
  updateColor()
extend_button = Button(win, text="EXTEND", command=extend_text)
extend_button.place(x=450, y=25)

def darkModeToggle():
  global dark_mode
  dark_mode = not dark_mode
  if dark_mode:
    win.config(bg="#1C0A0A")
    dark_mode_button.config(text="Dark Mode")
    prompt.config(bg="#3B3A3A")
  else:
    win.config(bg="#FEFEFE")
    dark_mode_button.config(text="Light Mode")
    prompt.config(bg="#FDFDFD")
  updateColor()
dark_mode_button = Button(win, text="Light Mode", command=darkModeToggle)
dark_mode_button.place(x=450, y=350)
darkModeToggle()

win.title("Text completion")
win.mainloop()
