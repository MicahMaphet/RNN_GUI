from tkinter import *
from ModelCommands import predict_text

length = 100 # the length of the extended text
dark_mode = False

win = Tk()
# The text prompt that the neural net will extend
prompt = Text(win, width=75, height=30)
prompt.place(x=25, y=25)

# keeps track of all of the versions of the text prompt
text_versions = [prompt.get("1.0", "end")]
# the version being used
current_text_version = 0
# saves the text in the prompt
def save():
  global current_text_version
  print("|current version:")
  print(text_versions[current_text_version])
  print("actual prompt:")
  print(prompt.get("1.0", "end") + "|")
  if text_versions[current_text_version] != prompt.get("1.0", "end"):
    current_text_version += 1 # updates the version to keep in sync
    text_versions.insert(current_text_version+1, prompt.get("1.0", "end"))
    print(f"| { current_text_version } |")

# A scale widget for setting the length of the text to be extended
length_scale = Scale(win, from_=0, to=500, length=250, width=20)
length_scale.set(length)
length_scale.place(x=650, y=60)
def updateColor():
  prompt.tag_add("color", "1.0", "end")
  if dark_mode:
    prompt.tag_config("color", foreground="white")
  else:
    prompt.tag_config("color", foreground="black")
def onKeyPress(event=None):
  save() # saves the text prompt (for undo and redo)
  updateColor() # updates the color (for dark mode)
prompt.bind("<Key>", onKeyPress)

def extend_text():
  save() # saves the model (for undo and redo)
  text = prompt.get("1.0", "end")
  print(text)
  print("\n\n" in text)
  prompt.delete("1.0", "end")
  prompt.insert("1.0", predict_text(text, length_scale.get()))
  updateColor()
extend_button = Button(win, text="EXTEND", command=extend_text)
extend_button.place(x=650, y=25)

# revert back to the previous state of the text in the prompt
def undo():
  global current_text_version
  if current_text_version > 0: 
    save() # save the text before deleting it (for redoing)
    current_text_version -= 2
  
  print(f"current version: { current_text_version } \
          \ntext versions length: { len(text_versions) }")
  prompt.delete("1.0", "end") # delete the text in the prompt
  # adds the text of the previous text version to the prompt
  prompt.insert("1.0", text_versions[current_text_version])
# the button to undo the text
undo_button = Button(win, text="undo", command=undo)
undo_button.place(x=700, y=25)

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
