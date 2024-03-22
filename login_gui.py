import customtkinter
import tkinter
import os
from PIL import Image
from tkinter import filedialog
from tkinter.filedialog import askdirectory

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark

        self.title("GENBY")
        self.geometry("350x600")
        self.resizable(False, False)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(196, 196))
        self.logo = customtkinter.CTkLabel(self, text="", image=self.logo_image)
        self.logo.place(x=350/2, y=50, anchor=customtkinter.N)

        self.frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=(300,20))
        self.frame.grid_rowconfigure(4, weight=1)

        self.email_label = customtkinter.CTkLabel(self.frame, text="Email", anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.email_label.grid(row=0, column=0, sticky="nsew")

        self.email = customtkinter.CTkEntry(self.frame, placeholder_text="Enter your email", width=310)
        self.email.grid(row=1, column=0, pady=(0, 10), sticky="nsew")

        self.password_label = customtkinter.CTkLabel(self.frame, text="Password", anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.password_label.grid(row=2, column=0, sticky="nsew")

        self.password = customtkinter.CTkEntry(self.frame, placeholder_text="Enter your password", width=310)
        self.password.grid(row=3, column=0, pady=(0, 10), sticky="nsew")

        self.warning = customtkinter.CTkLabel(self.frame, text="", text_color="red", anchor="n")
        self.warning.grid(row=4, column=0, pady=(0,20), sticky="w")
        self.set_warning("warning")

        self.login_button = customtkinter.CTkButton(self.frame, text="Login", height=50, font=customtkinter.CTkFont(size=20, weight="bold"), command=self.on_login)
        self.login_button.grid(row=5, column=0, pady=(0,5), sticky="nsew")
        
        self.register_button = customtkinter.CTkButton(self.frame, text="Register", bg_color="transparent", fg_color="transparent", hover=False, command=self.on_register)
        self.register_button.grid(row=6, column=0, sticky="nsew")

    def on_login(self):
        print("login")

    def on_register(self):
        print("register")

    def set_warning(self, text):
        self.warning.configure(text=text)

if __name__ == "__main__":
    app = App()
    app.mainloop()