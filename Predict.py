from tkinter import *
import ModelCommands

length = 100 # the length of the extended text
dark_mode = False

win = Tk() # the root window

# The text prompt that the neural net will extend
prompt = Text(win, width=75, height=30)
prompt.place(x=25, y=25)

# A scale widget for setting the length of the text to be extended
length_scale = Scale(win, from_=0, to=500, length=250, width=20)
length_scale.set(length) # set the default value
length_scale.place(x=650, y=60)

# Update the color of the text
def updateColor(event=None):
  prompt.tag_add("color", "1.0", "end")
  if dark_mode:
    prompt.tag_config("color", foreground="white")
  else:
    prompt.tag_config("color", foreground="black")
# the updateColor command will run ever time a key is pressed in the text prompt
prompt.bind("<Key>", updateColor) 


extend_button = Button(win, text="EXTEND", command=ModelCommands.extend_text(prompt, length_scale, updateColor))
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
    dark_mode_button.config(bg='#A6A6A6')
    extend_button.config(bg='#A6A6A6')
  # if the mode is being set to light
  else:
    win.config(bg="#FEFEFE")
    dark_mode_button.config(text="Light Mode")
    prompt.config(bg="#FAFAFA")
    length_scale.config(bg='#F2F2F2')
    dark_mode_button.config(bg='#F7F7F7')
    extend_button.config(bg='#F7F7F7')
  updateColor()
dark_mode_button = Button(win, text="Light Mode", command=darkModeToggle)
dark_mode_button.place(x=650, y=350)
dark_mode = not dark_mode
darkModeToggle()

win.title("Text completion")
win.mainloop()
