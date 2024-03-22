import customtkinter
import tkinter
import os
from PIL import Image
from tkinter import filedialog
from tkinter.filedialog import askdirectory

MENU = ["Automate work", "Generate Image From Mid Journey", "Generate prompt", "Generate Keyword for image (jpeg)", "Upscale Image (png -> jpeg)", "Connect to your discord"]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark

        self.title("GENBY")
        self.geometry("770x510")
        self.resizable(False, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(64, 64))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=12, weight="bold"), wraplength=120, anchor="w")
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.set_email()

        self.automate_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=MENU[0], fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.automate_button_event)
        self.automate_button.grid(row=1, column=0, sticky="ew")

        self.gen_img_from_mid_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=MENU[1], fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.gen_img_from_mid_button_event)
        self.gen_img_from_mid_button.grid(row=2, column=0, sticky="ew")

        self.gen_prompt_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=MENU[2], fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.gen_prompt_button_event)
        self.gen_prompt_button.grid(row=3, column=0, sticky="ew")

        self.gen_key_for_img_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=MENU[3], fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.gen_key_for_img_button_event)
        self.gen_key_for_img_button.grid(row=4, column=0, sticky="ew")

        self.upscale_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=MENU[4], fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.upscale_button_event)
        self.upscale_button.grid(row=5, column=0, sticky="ew")

        self.connect_discord_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=MENU[5], fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.connect_discord_button_event)
        self.connect_discord_button.grid(row=6, column=0, sticky="ew")

        self.automate = AutomateFrame(self)
        self.gen_img_from_mid = GenerateImageFromMidJourneyFrame(self)
        self.gen_prompt = GeneratePromptFrame(self)
        self.gen_key_for_img = GenerateKeywordForImageFrame(self)
        self.upscale = UpscaleImageFrame(self)

        # select default frame
        self.select_frame_by_name(MENU[0])

    def select_frame_by_name(self, name):

        # set button color for selected button
        self.automate_button.configure(fg_color=("gray75", "gray25") if name == MENU[0] else "transparent")
        self.gen_img_from_mid_button.configure(fg_color=("gray75", "gray25") if name == MENU[1] else "transparent")
        self.gen_prompt_button.configure(fg_color=("gray75", "gray25") if name == MENU[2] else "transparent")
        self.gen_key_for_img_button.configure(fg_color=("gray75", "gray25") if name == MENU[3] else "transparent")
        self.upscale_button.configure(fg_color=("gray75", "gray25") if name == MENU[4] else "transparent")
        self.connect_discord_button.configure(fg_color=("gray75", "gray25") if name == MENU[5] else "transparent")

        # show selected frame
        if name == MENU[0]:
            self.automate.get_frame().grid(row=0, column=1, sticky="nsew")
            self.automate.reset_state()
        else:
            self.automate.get_frame().grid_forget()
        if name == MENU[1]:
            self.gen_img_from_mid.get_frame().grid(row=0, column=1, sticky="nsew")
            self.gen_img_from_mid.reset_state()
        else:
            self.gen_img_from_mid.get_frame().grid_forget()
        if name == MENU[2]:
            self.gen_prompt.get_frame().grid(row=0, column=1, sticky="nsew")
            self.gen_prompt.reset_state()
        else:
            self.gen_prompt.get_frame().grid_forget()
        if name == MENU[3]:
            self.gen_key_for_img.get_frame().grid(row=0, column=1, sticky="nsew")
            self.gen_key_for_img.reset_state()
        else:
            self.gen_key_for_img.get_frame().grid_forget()
        if name == MENU[4]:
            self.upscale.get_frame().grid(row=0, column=1, sticky="nsew")
            self.upscale.reset_state()
        else:
            self.upscale.get_frame().grid_forget()

    def automate_button_event(self):
        self.select_frame_by_name(MENU[0])

    def gen_img_from_mid_button_event(self):
        self.select_frame_by_name(MENU[1])

    def gen_prompt_button_event(self):
        self.select_frame_by_name(MENU[2])

    def gen_key_for_img_button_event(self):
        self.select_frame_by_name(MENU[3])

    def upscale_button_event(self):
        self.select_frame_by_name(MENU[4])

    def connect_discord_button_event(self):
        print("Connect Discord")

    def set_email(self):
        email = "email@example"
        self.navigation_frame_label.configure(text=f"  {email}")

class AutomateFrame():
    def __init__(self, parent):
        super().__init__()
        
        self.src_prompt_var = tkinter.IntVar(value=0)
        self.generate_keyword_var = tkinter.IntVar(value=0)
        self.frame = customtkinter.CTkFrame(parent, corner_radius=0, fg_color="transparent")

        GroupTitle(self.frame, "Source of Prompt", 0)
        self.prompt_from_file = PromptFromFile(self.frame, 1, self.src_prompt_var, 0)
        self.gen_rand_prompt = GenerateRandomPrompt(self.frame, 2, self.src_prompt_var, 1)
        self.gen_prompt_csv =GeneratePromptFromCSV(self.frame, 3, self.src_prompt_var, 2)
        
        GroupTitle(self.frame, "Generate Keyword", 4)
        self.gen_key_img_gemini = GenerateKeywordImageGemini(self.frame, 5, self.generate_keyword_var, 0)
        self.gen_key_prompt_gemini = GenerateKeywordPromptGemini(self.frame, 6, self.generate_keyword_var, 1)
        self.gen_key_gpt = GenerateKeywordChatGPT(self.frame, 7, self.generate_keyword_var, 2)

        self.warning = Warning(self.frame, 11, (62, 0))
        StartButton(self.frame, 12, "Start Automate", self.on_start_automate)

    def on_start_automate(self):
        selected_source = self.src_prompt_var.get()
        if selected_source == 0:    #Select From my prompt
            self.prompt_from_file.on_gen_from_file(self.warning)    
        elif selected_source == 1:    #Generate random prompt
            self.gen_rand_prompt.on_gen_rand_prompt(self.warning)
        elif selected_source == 2:    #Generate prompt from concept_sequence.csv
            self.gen_prompt_csv.on_gen_from_csv(self.warning)
        
        selected_gen_key = self.generate_keyword_var.get()
        if selected_gen_key == 0:    #Generate keyword from Image by Gemini
            self.gen_key_img_gemini.on_gen_key_img_gemini()
        elif selected_gen_key == 1:    #Generate keyword from prompt by Gemini
            self.gen_key_prompt_gemini.on_gen_key_prompt_gemini()
        elif selected_gen_key == 2:    #Generate keyword from prompt by Chat GPT 3.5
            self.gen_key_gpt.on_gen_key_gpt()

    def get_frame(self):
        return self.frame
    
    def reset_state(self):
        self.src_prompt_var = tkinter.IntVar(value=0)
        self.generate_keyword_var = tkinter.IntVar(value=0)
        self.prompt_from_file.reset_state(self.src_prompt_var)
        self.gen_rand_prompt.reset_state(self.src_prompt_var)
        self.gen_prompt_csv.reset_state(self.src_prompt_var)
        self.gen_key_img_gemini.reset_state(self.generate_keyword_var)
        self.gen_key_prompt_gemini.reset_state(self.generate_keyword_var)
        self.gen_key_gpt.reset_state(self.generate_keyword_var)
        self.warning.set_warning(text="")

class GenerateImageFromMidJourneyFrame():
    def __init__(self, parent):
        super().__init__()
        
        self.src_prompt_var = tkinter.IntVar(value=0)
        self.frame = customtkinter.CTkFrame(parent, corner_radius=0, fg_color="transparent")

        GroupTitle(self.frame, "Source of Prompt", 0)
        self.prompt_from_file = PromptFromFile(self.frame, 1, self.src_prompt_var, 0)
        self.gen_rand_prompt = GenerateRandomPrompt(self.frame, 2, self.src_prompt_var, 1)
        self.gen_prompt_csv =GeneratePromptFromCSV(self.frame, 3, self.src_prompt_var, 2)

        self.warning = Warning(self.frame, 11, (236, 0))
        StartButton(self.frame, 12, "Start Automate", self.on_start_automate)
    
    def on_start_automate(self):
        selected_source = self.src_prompt_var.get()
        if selected_source == 0:    #Select From my prompt
            self.prompt_from_file.on_gen_from_file(self.warning)    
        elif selected_source == 1:    #Generate random prompt
            self.gen_rand_prompt.on_gen_rand_prompt(self.warning)
        elif selected_source == 2:    #Generate prompt from concept_sequence.csv
            self.gen_prompt_csv.on_gen_from_csv(self.warning)

    def get_frame(self):
        return self.frame

    def reset_state(self):
        self.src_prompt_var = tkinter.IntVar(value=0)
        self.prompt_from_file.reset_state(self.src_prompt_var)
        self.gen_rand_prompt.reset_state(self.src_prompt_var)
        self.gen_prompt_csv.reset_state(self.src_prompt_var)
        self.warning.set_warning(text="")

class GeneratePromptFrame():
    def __init__(self, parent):
        super().__init__()
        
        self.src_prompt_var = tkinter.IntVar(value=0)
        self.frame = customtkinter.CTkFrame(parent, corner_radius=0, fg_color="transparent")

        GroupTitle(self.frame, "Source of Concept", 0)
        self.gen_rand_prompt = GenerateRandomPrompt(self.frame, 1, self.src_prompt_var, 0)
        self.gen_prompt_csv =GeneratePromptFromCSV(self.frame, 2, self.src_prompt_var, 1)

        self.warning = Warning(self.frame, 11, (284, 0))
        StartButton(self.frame, 12, "Start Automate", self.on_start_automate)
    
    def on_start_automate(self):
        selected_source = self.src_prompt_var.get()  
        if selected_source == 0:    #Generate random prompt
            self.gen_rand_prompt.on_gen_rand_prompt(self.warning)
        elif selected_source == 1:    #Generate prompt from concept_sequence.csv
            self.gen_prompt_csv.on_gen_from_csv(self.warning)

    def get_frame(self):
        return self.frame

    def reset_state(self):
        self.src_prompt_var = tkinter.IntVar(value=0)
        self.gen_rand_prompt.reset_state(self.src_prompt_var)
        self.gen_prompt_csv.reset_state(self.src_prompt_var)
        self.warning.set_warning(text="")

class GenerateKeywordForImageFrame():
    def __init__(self, parent):
        super().__init__()
        
        self.generate_keyword_var = tkinter.IntVar(value=0)
        self.frame = customtkinter.CTkFrame(parent, corner_radius=0, fg_color="transparent")

        GroupTitle(self.frame, "Image Folder", 0)
        self.open_img_folder = customtkinter.CTkButton(master=self.frame, text="Open", width=50, command=self.on_open_img_folder)
        self.open_img_folder.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="w")
        self.img_folder_path = customtkinter.CTkEntry(master=self.frame, placeholder_text="Image folder path", width=280)
        self.img_folder_path.configure(state="disabled")
        self.img_folder_path.grid(row=1, column=0, padx=80, pady=(5, 5), sticky="w")

        GroupTitle(self.frame, "Prompt File", 2)
        self.open_prompt_file = customtkinter.CTkButton(master=self.frame, text="Open", width=50, command=self.on_open_prompt_file)
        self.open_prompt_file.grid(row=3, column=0, padx=20, pady=(5, 5), sticky="w")
        self.prompt_file_path = customtkinter.CTkEntry(master=self.frame, placeholder_text="Prompt file path", width=280)
        self.prompt_file_path.configure(state="disabled")
        self.prompt_file_path.grid(row=3, column=0, padx=80, pady=(5, 5), sticky="w")

        self.total_img_label = customtkinter.CTkLabel(master=self.frame, text="Total Image:", anchor="w")
        self.total_img_label.grid(row=4, column=0, pady=(10, 5), padx=20, sticky="nsew")

        self.match_prompt_label = customtkinter.CTkLabel(master=self.frame, text="Match with prompt:", anchor="w")
        self.match_prompt_label.grid(row=5, column=0, pady=(0, 5), padx=20, sticky="nsew")
        
        GroupTitle(self.frame, "Generate Keyword", 6)
        self.gen_key_img_gemini = GenerateKeywordImageGemini(self.frame, 7, self.generate_keyword_var, 0)
        self.gen_key_prompt_gemini = GenerateKeywordPromptGemini(self.frame, 8, self.generate_keyword_var, 1)
        self.gen_key_gpt = GenerateKeywordChatGPT(self.frame, 9, self.generate_keyword_var, 2)

        self.warning = Warning(self.frame, 10, (0, 0))
        StartButton(self.frame, 11, "Start Automate", self.on_start_automate)

    def on_open_img_folder(self):
        input_path = filedialog.askdirectory()
        self.img_folder_path.configure(state="normal")
        self.img_folder_path.delete(0, len(self.img_folder_path.get()))
        self.img_folder_path.insert(0, input_path)
        self.img_folder_path.configure(state="disabled")

    def on_open_prompt_file(self):
        input_path = filedialog.askdirectory()
        prompt_file = os.path.join(input_path, 'prompt.txt')
        self.prompt_file_path.configure(state="normal")
        self.prompt_file_path.delete(0, len(self.prompt_file_path.get()))
        self.prompt_file_path.insert(0, prompt_file)
        self.prompt_file_path.configure(state="disabled")

    def on_start_automate(self):
        if self.img_folder_path.get() == "" and self.prompt_file_path.get() != "":
            self.warning.set_warning(text="Please select image folder")
        elif self.img_folder_path.get() != "" and self.prompt_file_path.get() == "":
            self.warning.set_warning(text="Please select a prompt file")
        elif self.img_folder_path.get() == "" and self.prompt_file_path.get() == "":
            self.warning.set_warning(text="Please select image folder and a prompt file")
        else:
            print(f"Image folder path : {self.img_folder_path.get()}")
            print(f"Prompt file path : {self.prompt_file_path.get()}")
            self.set_result_image()
            self.warning.set_warning(text="")

        selected_gen_key = self.generate_keyword_var.get()
        if selected_gen_key == 0:    #Generate keyword from Image by Gemini
            self.gen_key_img_gemini.on_gen_key_img_gemini()
        elif selected_gen_key == 1:    #Generate keyword from prompt by Gemini
            self.gen_key_prompt_gemini.on_gen_key_prompt_gemini()
        elif selected_gen_key == 2:    #Generate keyword from prompt by Chat GPT 3.5
            self.gen_key_gpt.on_gen_key_gpt()

    def set_result_image(self):
        self.total_img = 0
        self.match_prompt = 0
        self.total_img_label.configure(text=f"Total Image: {self.total_img}")
        self.match_prompt_label.configure(text=f"Match with prompt: {self.match_prompt}")

    def get_frame(self):
        return self.frame
    
    def reset_state(self):
        self.generate_keyword_var = tkinter.IntVar(value=0)
        self.gen_key_img_gemini.reset_state(self.generate_keyword_var)
        self.gen_key_prompt_gemini.reset_state(self.generate_keyword_var)
        self.gen_key_gpt.reset_state(self.generate_keyword_var)
        self.warning.set_warning(text="")

        self.img_folder_path.configure(state="normal")
        self.img_folder_path.delete(0, len(self.img_folder_path.get()))
        self.img_folder_path.configure(placeholder_text="Image folder path")
        self.img_folder_path.configure(state="disabled")

        self.prompt_file_path.configure(state="normal")
        self.prompt_file_path.delete(0, len(self.prompt_file_path.get()))
        self.prompt_file_path.configure(placeholder_text="Prompt file path")
        self.prompt_file_path.configure(state="disabled")

class UpscaleImageFrame():
    def __init__(self, parent):
        super().__init__()
        
        self.upscale_var = tkinter.IntVar(value=0)
        self.frame = customtkinter.CTkFrame(parent, corner_radius=0, fg_color="transparent")

        GroupTitle(self.frame, "Project Folder", 0)
        self.open_img_folder = customtkinter.CTkButton(master=self.frame, text="Open", width=50, command=self.on_open_img_folder)
        self.open_img_folder.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="w")
        self.img_folder_path = customtkinter.CTkEntry(master=self.frame, placeholder_text="Project folder path", width=280)
        self.img_folder_path.configure(state="disabled")
        self.img_folder_path.grid(row=1, column=0, padx=80, pady=(5, 5), sticky="w")

        self.total_img_label = customtkinter.CTkLabel(master=self.frame, text="Total Image:", anchor="w")
        self.total_img_label.grid(row=4, column=0, pady=(10, 5), padx=20, sticky="nsew")

        self.upscale_2x = customtkinter.CTkRadioButton(master=self.frame, text="Upscale 2X", variable=self.upscale_var, value=0)
        self.upscale_2x.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")

        self.upscale_4x = customtkinter.CTkRadioButton(master=self.frame, text="Upscale 4X", variable=self.upscale_var, value=1)
        self.upscale_4x.grid(row=6, column=0, pady=10, padx=20, sticky="nsew")

        self.warning = Warning(self.frame, 10, (209, 0))
        StartButton(self.frame, 11, "Start Automate", self.on_start_automate)

    def on_open_img_folder(self):
        input_path = filedialog.askdirectory()
        self.img_folder_path.configure(state="normal")
        self.img_folder_path.delete(0, len(self.img_folder_path.get()))
        self.img_folder_path.insert(0, input_path)
        self.img_folder_path.configure(state="disabled")

    def on_start_automate(self):
        if self.img_folder_path.get() == "":
            self.warning.set_warning(text="Please select project folder")
        else:
            print(f"Project folder path : {self.img_folder_path.get()}")
            self.set_result_image()
            self.warning.set_warning(text="")

        selected_upscale = self.upscale_var.get()
        if selected_upscale == 0:    #Upscale 2X
            print("Upscale 2X")
        elif selected_upscale == 1:  #Upscale 4X
            print("Upscale 4X")

    def set_result_image(self):
        self.total_img = 0
        self.total_img_label.configure(text=f"Total Image: {self.total_img}")

    def get_frame(self):
        return self.frame
    
    def reset_state(self):
        self.upscale_var = tkinter.IntVar(value=0)
        self.warning.set_warning(text="")

        self.img_folder_path.configure(state="normal")
        self.img_folder_path.delete(0, len(self.img_folder_path.get()))
        self.img_folder_path.configure(placeholder_text="Project folder path")
        self.img_folder_path.configure(state="disabled")

        self.upscale_2x.configure(variable=self.upscale_var)
        self.upscale_4x.configure(variable=self.upscale_var)

class GroupTitle:
    def __init__(self, frame, text, row):
        self.src_prompt_label = customtkinter.CTkLabel(master=frame, text=text, anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.src_prompt_label.grid(row=row, column=0, pady=10, padx=20, sticky="nsew")

class PromptFromFile(tkinter.IntVar):
    def __init__(self, frame, row, var, value):
        self.from_my_prompt = customtkinter.CTkRadioButton(master=frame, text="From my prompt", variable=var, value=value)
        self.from_my_prompt.grid(row=row, column=0, pady=10, padx=20, sticky="nsew")
        self.open_file = customtkinter.CTkButton(master=frame, text="Open", width=50, command=self.on_open_file)
        self.open_file.grid(row=row, column=0, padx=150, pady=10, sticky="w")
        self.file_path = customtkinter.CTkEntry(master=frame, placeholder_text="Prompt file path", width=280)
        self.file_path.configure(state="disabled")
        self.file_path.grid(row=row, column=0, padx=210, pady=10, sticky="w")

    def on_open_file(self):
        input_path = filedialog.askdirectory()
        prompt_file = os.path.join(input_path, 'prompt.txt')
        self.file_path.configure(state="normal")
        self.file_path.delete(0, len(self.file_path.get()))
        self.file_path.insert(0, prompt_file)
        self.file_path.configure(state="disabled")

    def on_gen_from_file(self, warning: Warning):
        if self.file_path.get() != "":
            print(f"Prompt file : {self.file_path.get()}")
            warning.set_warning(text="")
        else:
            warning.set_warning(text="Please select a prompt file")

    def reset_state(self, var):
        self.from_my_prompt.configure(variable=var)
        self.file_path.configure(state="normal")
        self.file_path.delete(0, len(self.file_path.get()))
        self.file_path.configure(placeholder_text="File path")
        self.file_path.configure(state="disabled")

class GenerateRandomPrompt(tkinter.IntVar):
    def __init__(self, frame, row, var, value):
        self.gen_rand_prompt = customtkinter.CTkRadioButton(master=frame, text="Generate random prompt", variable=var, value=value)
        self.gen_rand_prompt.grid(row=row, column=0, pady=10, padx=20, sticky="nsew")
        self.gen_rand_prompt_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Max random prompt (up to 300)", width=290)
        self.gen_rand_prompt_entry.grid(row=row, column=0, padx=200, pady=10, sticky="w")
    
    def on_gen_rand_prompt(self, warning: Warning):
        if self.gen_rand_prompt_entry.get() != "":
            try:
                prompt_count = int(self.gen_rand_prompt_entry.get())
                if prompt_count >= 1 and prompt_count <= 300:
                    print(f"Max random prompt : {prompt_count}")
                    warning.set_warning(text="")
                else:
                    warning.set_warning(text="Please enter max random prompt between 1 and 300")
            except ValueError:
                warning.set_warning(text="Max random prompt did not contain a number!")
        else:
            warning.set_warning(text="Please enter a max random prompt")

    def reset_state(self, var):
        self.gen_rand_prompt.configure(variable=var)
        self.gen_rand_prompt_entry.delete(0, len(self.gen_rand_prompt_entry.get()))

class GeneratePromptFromCSV(tkinter.IntVar):
    def __init__(self, frame, row, var, value):
        self.gen_prompt_csv = customtkinter.CTkRadioButton(master=frame, text="Generate prompt from concept_sequence.csv", variable=var, value=value)
        self.gen_prompt_csv.grid(row=row, column=0, pady=10, padx=20, sticky="nsew")

    def on_gen_from_csv(self, warning: Warning):
        print("Generate prompt from concept_sequence.csv")
        warning.set_warning(text="")

    def reset_state(self, var):
        self.gen_prompt_csv.configure(variable=var)

class GenerateKeywordImageGemini(tkinter.IntVar):
    def __init__(self, frame, row, var, value):
        self.gen_key_img_gemini = customtkinter.CTkRadioButton(master=frame, text="Generate keyword from Image by Gemini", variable=var, value=value)
        self.gen_key_img_gemini.grid(row=row, column=0, pady=10, padx=20, sticky="nsew")

    def on_gen_key_img_gemini(self):
        print("Generate keyword from Image by Gemini")

    def reset_state(self, var):
        self.gen_key_img_gemini.configure(variable=var)

class GenerateKeywordPromptGemini(tkinter.IntVar):
    def __init__(self, frame, row, var, value):
        self.gen_key_prompt_gemini = customtkinter.CTkRadioButton(master=frame, text="Generate keyword from prompt by Gemini", variable=var, value=value)
        self.gen_key_prompt_gemini.grid(row=row, column=0, pady=10, padx=20, sticky="nsew")

    def on_gen_key_prompt_gemini(self):
        print("Generate keyword from prompt by Gemini")

    def reset_state(self, var):
        self.gen_key_prompt_gemini.configure(variable=var)

class GenerateKeywordChatGPT(tkinter.IntVar):
    def __init__(self, frame, row, var, value):
        self.gen_key_prompt_gpt = customtkinter.CTkRadioButton(master=frame, text="Generate keyword from prompt by Chat GPT 3.5", variable=var, value=value)
        self.gen_key_prompt_gpt.grid(row=row, column=0, pady=10, padx=20, sticky="nsew")

    def on_gen_key_gpt(self):
        print("Generate keyword from prompt by Chat GPT 3.5")

    def reset_state(self, var):
        self.gen_key_prompt_gpt.configure(variable=var)

class Warning:
    def __init__(self, frame, row, pady):
        self.warning = customtkinter.CTkLabel(master=frame, text="", text_color="red", anchor="n")
        self.warning.grid(row=row, column=0, padx=(20, 20), pady=pady, sticky="w")

    def set_warning(self, text):
        self.warning.configure(text=text)

class StartButton:
    def __init__(self, frame, row, text, callback):
        self.start_automate = customtkinter.CTkButton(frame, text=text, width=510, height=50, font=customtkinter.CTkFont(size=20, weight="bold"), command=callback)
        self.start_automate.grid(row=row, column=0, padx=(20, 20), sticky="w")

if __name__ == "__main__":
    app = App()
    app.mainloop()