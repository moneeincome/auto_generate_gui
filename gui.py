import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from numpy import random
from tkinter import scrolledtext

root = tk.Tk()
root.title("Auto Generate")
root.geometry("1280x445")

# Disable window resizing
root.resizable(False, False)

#======================Prompt Area======================

def on_scroll(*args):
  prompt_text.yview(*args)
  prompt_text.xview(*args)

def on_entry(event):
  if prompt_text.get("1.0", "end-1c") == prompt_placeholder:
    prompt_text.delete("1.0", "end-1c")
    prompt_text.config(fg='black')

def on_exit(event):
  if not prompt_text.get("1.0", "end-1c"):
    prompt_text.insert("1.0", prompt_placeholder, 'placeholder')
    prompt_text.tag_configure('placeholder', foreground='gray')

prompt_placeholder = 'Enter your prompt here...'

prompt_frame = tk.Frame(root, width=650, height=445)
#prompt_frame.pack_propagate(False)
prompt_frame.pack(anchor=tk.NW, padx=10, ipady=10, expand=True)

prompt_label = tk.Label(prompt_frame, text="Prompt")
prompt_label.pack(anchor=tk.NW)

prompt_text = tk.Text(prompt_frame, wrap="none")
prompt_text.insert("1.0", prompt_placeholder, 'placeholder')
prompt_text.tag_configure('placeholder', foreground='gray')
prompt_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

prompt_text.bind("<FocusIn>", on_entry)
prompt_text.bind("<FocusOut>", on_exit)

prompt_scrollbar_v = tk.Scrollbar(prompt_frame, command=prompt_text.yview)
prompt_scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
prompt_text.config(yscrollcommand=prompt_scrollbar_v.set)

prompt_scrollbar_h = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=prompt_text.xview)
prompt_scrollbar_h.pack(side=tk.BOTTOM, anchor=tk.SW, ipadx=300, padx=5)
prompt_text.config(xscrollcommand=prompt_scrollbar_h.set)

prompt_text.bind("<Configure>", on_scroll)

#======================Setting Area======================

#Aspect Ratio

setting_frame = tk.Frame(root, width=610, height=400)
#setting_frame.pack_propagate(False)
setting_frame.place(x=675, y=10)

ar_label = tk.Label(setting_frame, text="Aspect ratio")
ar_label.pack(anchor=tk.NW)

ar_frame = tk.Frame(setting_frame)
ar_frame.pack(side=tk.TOP, anchor=tk.NW, pady=5)

aspect_ratios = ["1:1", "3:2", "2:3", "4:3", "3:4", "5:4", "4:5", "7:2", "2:7", "16:9", "9:16", "21:9", "9:21"]
ar_vars = []

ar_1_1var = tk.IntVar()
ar_vars.append(ar_1_1var)
ar_1_1 = tk.Checkbutton(ar_frame, text=aspect_ratios[0], variable=ar_1_1var, onvalue=1, offvalue=0)
ar_1_1.grid(row=0//2, column=0%2, sticky="w")

for i, ratio in enumerate(aspect_ratios):
  if i == 0: continue
  var = tk.IntVar()
  ar_vars.append(var)
  checkbox = tk.Checkbutton(ar_frame, text=ratio, variable=var, onvalue=1, offvalue=0)
  checkbox.grid(row=(i+1)//2, column=(i+1)%2, sticky="w")

#Suffix

def on_focus_in(event, entry):
    if entry.get() == placeholder:
      entry.delete(0, tk.END)
      entry.config(fg="black")

def on_focus_out(event, entry):
  if entry.get() == "":
    entry.insert(0, placeholder)
    entry.config(fg="grey")

placeholder = "Enter suffix here"

suffix_label = tk.Label(setting_frame, text="Suffix")
suffix_label.pack(anchor=tk.NW, pady=5)

suffix_frame = tk.Frame(setting_frame)
suffix_frame.pack(side=tk.TOP, anchor=tk.NW)

suffixs = []

# Create and place the entry widgets inside the frame
for i in range(10):
  suffix = tk.Entry(suffix_frame, fg="grey", width=48)
  suffix.insert(0, placeholder)
  suffix.bind("<FocusIn>", lambda event, entry=suffix: on_focus_in(event, entry))
  suffix.bind("<FocusOut>", lambda event, entry=suffix: on_focus_out(event, entry))
  suffix.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="w")
  suffixs.append(suffix)

#Confirm Button

def on_generate():
  #Remove empty line in prompt text
  raw_prompt = prompt_text.get("1.0", "end-1c")
  if raw_prompt == prompt_placeholder or raw_prompt == '':
    messagebox.showinfo("Notice", "Please enter your prompt.")
    return

  raw_prompt = os.linesep.join(
    [
      line for line in raw_prompt.splitlines()
      if line
    ]
  )

  #Add suffix to prompt's line
  suffix_list = []
  for suffix in suffixs:
    if suffix.get() != placeholder and suffix.get() != '':
      suffix_list.append(suffix.get())

  if len(suffix_list) > 0:
    raw_prompt = os.linesep.join(
      [
        line.strip() + f', {suffix_list[random.randint(len(suffix_list))]}' for line in raw_prompt.splitlines()
        if line
      ]
    )

  #Add aspect ratio to prompt's line
  ar_list = []
  for i, ratio in enumerate(aspect_ratios):
    if ar_vars[i].get() == 1:
      ar_list.append(ratio)

  if len(ar_list) > 0:
    raw_prompt = os.linesep.join(
      [
        line.strip() + f' --ar {ar_list[random.randint(len(ar_list))]}' for line in raw_prompt.splitlines()
        if line
      ]
    )
  
  print(raw_prompt)

generate_button = tk.Button(setting_frame, text="Generate", width=84, height=2, command=on_generate)
generate_button.pack(side=tk.TOP, anchor=tk.NW, pady=5)  # Adjust position as needed

#======================Event update progression======================

# callback for update prompt status
# param line: "1.0" - "n.0" (index of line start at "1.0")
# param color: inprogress: "orange" | done: "green" | error: "red"
def update_prompt_status(line, color):
  max_line = str((int(line.split('.')[0]) + 1)) + "." + "0"
  prompt_text.tag_add("colored", line, max_line)
  prompt_text.tag_config("colored", foreground=color)

#===========================================================

# def on_mousewheel(event):
#   canvas.yview_scroll(-1*(event.delta//120), "units")

# canvas_frame = tk.Frame(root)
# canvas_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# canvas = tk.Canvas(canvas_frame, width=780, height=540, bg="white", scrollregion=(0, 0, 780, 540))
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# canvas.config(yscrollcommand=scrollbar.set)

# image_paths = ["your_image.jpg", "your_image.png", "Untitled.png", "your_image.jpg"]  # Example image paths

# cell_size = 128
# num_cols = 780 // cell_size
# num_rows = (len(image_paths) + num_cols - 1) // num_cols

# for i, image_path in enumerate(image_paths):
#     col = i % num_cols
#     row = i // num_cols
#     x = col * cell_size
#     y = row * cell_size
    
#     original_image = Image.open(image_path)
#     original_image = original_image.resize((cell_size, cell_size))
#     img = ImageTk.PhotoImage(original_image)
    
#     canvas.create_image(x, y, anchor=tk.NW, image=img)
#     canvas.img_ref = img  # Keep a reference to prevent garbage collection

# canvas.bind("<MouseWheel>", on_mousewheel)

root.mainloop()