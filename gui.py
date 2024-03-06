import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from numpy import random
from tkinter import scrolledtext

global root
global placeholder
global prompt_text
global prompt_placeholder
global aspect_ratios
global suffixs
global ar_vars
global raw_prompt
global result_prompt

def on_scroll(*args):
  global prompt_text
  prompt_text.yview(*args)
  prompt_text.xview(*args)

def on_entry(event):
  global prompt_text
  global prompt_placeholder
  if prompt_text.get("1.0", "end-1c") == prompt_placeholder:
    prompt_text.delete("1.0", "end-1c")
    prompt_text.config(fg='black')

def on_exit(event):
  global prompt_text
  global prompt_placeholder
  if not prompt_text.get("1.0", "end-1c"):
    prompt_text.insert("1.0", prompt_placeholder, 'placeholder')
    prompt_text.tag_configure('placeholder', foreground='gray')

def on_focus_in(event, entry):
  global placeholder
  if entry.get() == placeholder:
    entry.delete(0, tk.END)
    entry.config(fg="black")

def on_focus_out(event, entry):
  global placeholder
  if entry.get() == "":
    entry.insert(0, placeholder)
    entry.config(fg="grey")

def on_generate():
  global root
  global raw_prompt
  global prompt_text
  global prompt_placeholder
  global suffixs
  global placeholder
  global ar_vars
  global aspect_ratios
  global result_prompt

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

  #Remove parameters
  result_prompt = ''
  prompt_lines = raw_prompt.splitlines()
  for i, line in enumerate(prompt_lines):
    if line.__contains__('--'): line = line.split('--')[0] #remove parameters --ar --style
    line = line.strip()
    if i < len(prompt_lines) - 1: result_prompt += line + '\n'
    else: result_prompt += line

  #Add suffix to prompt's line
  suffix_list = []
  for suffix in suffixs:
    if suffix.get() != placeholder and suffix.get() != '':
      suffix_list.append(suffix.get())

  if len(suffix_list) > 0:
    result_prompt = os.linesep.join(
      [
        line.strip() + f' {suffix_list[random.randint(len(suffix_list))]}' for line in result_prompt.splitlines()
        if line
      ]
    )

  #Add aspect ratio to prompt's line
  ar_list = []
  for i, ratio in enumerate(aspect_ratios):
    if ar_vars[i].get() == 1:
      ar_list.append(ratio)

  if len(ar_list) > 0:
    result_prompt = os.linesep.join(
      [
        line.strip() + f' --ar {ar_list[random.randint(len(ar_list))]}' for line in result_prompt.splitlines()
        if line
      ]
    )

  prompt_lines = result_prompt.splitlines()
  non_empty_lines = [line for line in prompt_lines if line.strip()]
  result_prompt = '\n'.join(non_empty_lines)

  root.destroy()

def get_result():
  global result_prompt
  return result_prompt

#======================Event update progression======================

# callback for update prompt status
# param line: "1.0" - "n.0" (index of line start at "1.0")
# param color: inprogress: "orange" | done: "green" | error: "red"
def update_prompt_status(line, color):
  global prompt_text
  max_line = str((int(line.split('.')[0]) + 1)) + "." + "0"
  prompt_text.tag_add("colored", line, max_line)
  prompt_text.tag_config("colored", foreground=color)

#====================================================================

def create_gui():
  global root
  global placeholder
  global prompt_text
  global prompt_placeholder
  global aspect_ratios
  global suffixs
  global ar_vars
  global raw_prompt

  root = tk.Tk()
  root.title("Auto Generate")
  root.geometry("1280x445")

  # Disable window resizing
  root.resizable(False, False)

  #======================Prompt Area======================

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

  generate_button = tk.Button(setting_frame, text="Generate", width=84, height=2, command=on_generate)
  generate_button.pack(side=tk.TOP, anchor=tk.NW, pady=5)  # Adjust position as needed

  #====================================================================

  root.mainloop()