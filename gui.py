import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Auto Generate")
root.geometry("800x600")

#======================Prompt Area======================

def on_text_area_scroll(event):
  prompt_text.yview_scroll(int(-1 * (event.delta / 120)), "units")

def on_entry(event):
  if prompt_text.get("1.0", "end-1c") == prompt_placeholder:
    prompt_text.delete("1.0", "end-1c")
    prompt_text.config(fg='black')

def on_exit(event):
  if not prompt_text.get("1.0", "end-1c"):
    prompt_text.insert("1.0", prompt_placeholder, 'placeholder')
    prompt_text.tag_configure('placeholder', foreground='gray')

prompt_placeholder = 'Enter your prompt here...'

prompt_frame = tk.Frame(root, width=650, height=400)
prompt_frame.pack_propagate(False)
prompt_frame.place(x=10, y=10)

prompt_label = tk.Label(prompt_frame, text="Prompt")
prompt_label.pack(anchor=tk.NW)

prompt_text = tk.Text(prompt_frame, wrap="none")
prompt_text.insert("1.0", prompt_placeholder, 'placeholder')
prompt_text.tag_configure('placeholder', foreground='gray')
prompt_text.pack(fill=tk.BOTH, expand=True)

prompt_text.bind("<FocusIn>", on_entry)
prompt_text.bind("<FocusOut>", on_exit)

prompt_scrollbar = tk.Scrollbar(prompt_frame, command=prompt_text.yview)
prompt_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
prompt_text.config(yscrollcommand=prompt_scrollbar.set)

prompt_text.bind("<MouseWheel>", on_text_area_scroll)

#======================Setting Area======================

#Aspect Ratio

setting_frame = tk.Frame(root, width=150, height=400)
setting_frame.pack_propagate(False)
setting_frame.place(x=665, y=10)

ar_label = tk.Label(setting_frame, text="Aspect ratio")
ar_label.pack(anchor=tk.NW)

ar_var = tk.StringVar()

ar_none = tk.Radiobutton(setting_frame, text="None", variable=ar_var, value="None")
ar_none.pack(side=tk.TOP, anchor=tk.NW)

ar_1_1 = tk.Radiobutton(setting_frame, text="1:1", variable=ar_var, value="1:1")
ar_1_1.pack(side=tk.TOP, anchor=tk.NW)

ar_3_2 = tk.Radiobutton(setting_frame, text="3:2", variable=ar_var, value="3:2")
ar_3_2.pack(side=tk.TOP, anchor=tk.NW)

ar_4_3 = tk.Radiobutton(setting_frame, text="4:3", variable=ar_var, value="4:3")
ar_4_3.pack(side=tk.TOP, anchor=tk.NW)

ar_16_9 = tk.Radiobutton(setting_frame, text="16:9", variable=ar_var, value="16:9")
ar_16_9.pack(side=tk.TOP, anchor=tk.NW)

ar_21_9 = tk.Radiobutton(setting_frame, text="21:9", variable=ar_var, value="21:9")
ar_21_9.pack(side=tk.TOP, anchor=tk.NW)

ar_none.select()

# orientation

or_label = tk.Label(setting_frame, text="Orientation")
or_label.pack(anchor=tk.NW)

or_var = tk.StringVar()

or_horizontal = tk.Radiobutton(setting_frame, text="Horizontal", variable=or_var, value="Horizontal")
or_horizontal.pack(side=tk.TOP, anchor=tk.NW)

or_vertical = tk.Radiobutton(setting_frame, text="Vertical", variable=or_var, value="Vertical")
or_vertical.pack(side=tk.TOP, anchor=tk.NW)

or_horizontal.select()

#Suffix

def on_focus_in(event):
  if suffix.get() == placeholder:
    suffix.delete(0, tk.END)
    suffix.config(fg="black")

def on_focus_out(event):
  if suffix.get() == "":
    suffix.insert(0, placeholder)
    suffix.config(fg="grey")

placeholder = "Enter suffix here"

suffix_label = tk.Label(setting_frame, text="Suffix")
suffix_label.pack(anchor=tk.NW)

suffix = tk.Entry(setting_frame, fg="grey")
suffix.insert(0, placeholder)
suffix.bind("<FocusIn>", on_focus_in)
suffix.bind("<FocusOut>", on_focus_out)
suffix.pack(side=tk.TOP, anchor=tk.NW)

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
  if suffix.get() != placeholder and suffix.get() != '':
    raw_prompt = os.linesep.join(
      [
        line.strip() + f' {suffix.get()}' for line in raw_prompt.splitlines()
        if line
      ]
    )

  #Add aspect ratio to prompt's line
  if ar_var.get() != 'None':
    aspect_ratio = ar_var.get()
    if or_var.get() == 'Vertical':
      raw_aspect_ratio = ar_var.get().split(':')
      aspect_ratio = raw_aspect_ratio[1] + ':' + raw_aspect_ratio[0]
    raw_prompt = os.linesep.join(
      [
        line.strip() + f' --ar {aspect_ratio}' for line in raw_prompt.splitlines()
        if line
      ]
    )
  
  print(raw_prompt)

generate_button = tk.Button(setting_frame, text="Generate", width=17, height=4, command=on_generate)
generate_button.pack(side=tk.TOP, anchor=tk.NW, pady=10)  # Adjust position as needed

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