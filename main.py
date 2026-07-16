import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter Demo v1.0")
        self.geometry("450x550")

        self.count = 0

        self.logo = ctk.CTkLabel(self, text="CustomTkinter", text_color="green", font=ctk.CTkFont(family="Arial", size=25))
        self.logo.pack()

        self.frame_ = ctk.CTkFrame(self, width=350, height=450)
        self.frame_.pack_propagate(False)
        self.frame_.pack(pady=(0, 10))

        self.btn = ctk.CTkButton(self.frame_, text="Click me", hover_color="darkgreen", command=self.on_clicked)
        self.btn.pack(pady=10)

        self.label = ctk.CTkLabel(self.frame_, text="Counter: 0", font=ctk.CTkFont(family="Arial", size=20))
        self.label.pack(pady=10)

        self.clear = ctk.CTkButton(self.frame_, text="Clear", hover_color="darkgreen", command=self.clear_event)
        self.clear.pack(pady=10)

        self.prbar = ctk.CTkProgressBar(self.frame_, height=15)
        self.prbar.pack(pady=5)

        self.slider = ctk.CTkSlider(self.frame_, from_=0, to=100, command=self.slider_event)
        self.slider.pack(pady=5)

        self.switch = ctk.CTkSwitch(self.frame_, text="CTK Swith")
        self.switch.pack(pady=5)

        self.radios = ctk.IntVar(value=1)

        self.radio1 = ctk.CTkRadioButton(self.frame_, text="Option 1", variable=self.radios, value=1, command=self.radio_event)
        self.radio1.pack(pady=5)

        self.radio2 = ctk.CTkRadioButton(self.frame_, text="Option 2", variable=self.radios, value=2, command=self.radio_event)
        self.radio2.pack(pady=5)

        self.radio3 = ctk.CTkRadioButton(self.frame_, text="Option 3", variable=self.radios, value=3, command=self.radio_event)
        self.radio3.pack(pady=5)

        self.check = ctk.CTkCheckBox(self.frame_, text="CTK Check Box")
        self.check.pack(pady=5)

        self.combo = ctk.CTkComboBox(self.frame_, values=["Dark", "Light", "System"], command=self.theme)
        self.combo.set("System")
        self.combo.pack(pady=5)

    def theme(self, choice):
        ctk.set_appearance_mode(choice)

    def on_clicked(self):
        self.count += 1
        self.label.configure(text=f"Counter: {self.count}")

    def clear_event(self):
        self.count = 0
        self.label.configure(text=f"Counter: {self.count}")

    def slider_event(self, value):
        self.prbar.set(value/100)

    def radio_event(self):
        print(f"You are select: {self.radios.get()} option")


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
