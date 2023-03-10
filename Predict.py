from tkinter import *
from ModelCommands import predict_text

length = 100 # the length of the extended text
dark_mode = False

win = Tk()
# The text prompt that the neural net will extend
prompt = Text(win, width=75, height=30)
prompt.place(x=25, y=25)
# A scale widget for setting the length of the text to be extended
length_scale = Scale(win, from_=0, to=500, length=250, width=20)
length_scale.set(length)
length_scale.place(x=650, y=60)
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
extend_button.place(x=650, y=25)

def darkModeToggle():
  global dark_mode
  dark_mode = not dark_mode
  # if the mode is set to dark
  if dark_mode:
    win.config(bg="#1C0A0A")
    dark_mode_button.config(text="Dark Mode")
    prompt.config(bg="#7B7A7A")
    length_scale.config(bg='#BABABA')
    dark_mode_button.config(bg='#B2B2B2')
  # if the mode is being set to light
  else:
    win.config(bg="#FEFEFE")
    dark_mode_button.config(text="Light Mode")
    prompt.config(bg="#FAFAFA")
    length_scale.config(bg='#F2F2F2')
  updateColor()
dark_mode_button = Button(win, text="Light Mode", command=darkModeToggle)
dark_mode_button.place(x=650, y=350)
dark_mode = not dark_mode
darkModeToggle()

win.title("Text completion")
win.mainloop()
