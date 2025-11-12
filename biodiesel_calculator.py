import customtkinter as ctk
from tkinter import messagebox

# Popular oils with densities (g/ml) and approximate molar mass of triglyceride
OILS = {
    "Palmolein": (0.92, 885),
    "Soybean Oil": (0.92, 885),
    "Sunflower Oil": (0.92, 885),
    "Coconut Oil": (0.92, 885),
    "Olive Oil": (0.91, 885)
}

# 🔹 Global font settings
FONT_SIZE = 49
FONT_BIG = ("Arial", FONT_SIZE + 4, "bold")
FONT_NORMAL = ("Arial", FONT_SIZE)

def calculate_requirements(oil_ml, oil_type, catalyst_type, alcohol_type):
    density_oil, molar_mass = OILS[oil_type]
    oil_g = oil_ml * density_oil
    oil_mol = oil_g / molar_mass

    if alcohol_type == "Methyl Alcohol (Methanol)":
        alcohol_density = 0.792
        alcohol_molar_mass = 32.04
    else:  # Ethyl Alcohol (Ethanol)
        alcohol_density = 0.789
        alcohol_molar_mass = 46.07

    molar_ratio = 6
    alcohol_needed_mol = oil_mol * molar_ratio
    alcohol_needed_g = alcohol_needed_mol * alcohol_molar_mass
    alcohol_needed_ml = alcohol_needed_g / alcohol_density

    catalyst_percent = 1.5 if catalyst_type == "NaOH" else 1.2
    catalyst_needed_g = oil_g * catalyst_percent / 100

    return round(alcohol_needed_ml, 2), round(catalyst_needed_g, 2)

class BiodieselApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Biodiesel Calculator")
        self.geometry("600x600")  # bigger window to fit large text
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Title
        self.label = ctk.CTkLabel(self, text="Biodiesel Calculator", font=FONT_BIG, text_color="#42c2ff")
        self.label.pack(pady=10)

        # Oil amount
        self.entry_label = ctk.CTkLabel(self, text="Oil Amount (ml):", font=FONT_NORMAL)
        self.entry_label.pack()
        self.oil_entry = ctk.CTkEntry(self, font=FONT_NORMAL, width=250)
        self.oil_entry.pack(pady=5)

        # Oil type
        self.oil_label = ctk.CTkLabel(self, text="Oil Type:", font=FONT_NORMAL)
        self.oil_label.pack()
        self.oil_option = ctk.CTkOptionMenu(
            self,
            values=list(OILS.keys()),
            font=FONT_NORMAL,
            dropdown_font=FONT_NORMAL
        )
        self.oil_option.pack(pady=5)

        # Catalyst
        self.cat_label = ctk.CTkLabel(self, text="Catalyst:", font=FONT_NORMAL)
        self.cat_label.pack()
        self.cat_option = ctk.CTkOptionMenu(
            self,
            values=["NaOH", "KOH"],
            font=FONT_NORMAL,
            dropdown_font=FONT_NORMAL
        )
        self.cat_option.pack(pady=5)

        # Alcohol
        self.alc_label = ctk.CTkLabel(self, text="Alcohol:", font=FONT_NORMAL)
        self.alc_label.pack()
        self.alc_option = ctk.CTkOptionMenu(
            self,
            values=["Methyl Alcohol (Methanol)", "Ethyl Alcohol (Ethanol)"],
            font=FONT_NORMAL,
            dropdown_font=FONT_NORMAL
        )
        self.alc_option.pack(pady=5)

        # Result
        self.result_label = ctk.CTkLabel(self, text="", font=FONT_NORMAL)
        self.result_label.pack(pady=15)

        # Button
        self.calc_button = ctk.CTkButton(self, text="Calculate", command=self.show_results, font=FONT_NORMAL, fg_color="#42c2ff", text_color="black")
        self.calc_button.pack(pady=10)

        self.configure(bg="#2a2d2e")

    def show_results(self):
        try:
            oil_ml = float(self.oil_entry.get())
            oil_type = self.oil_option.get()
            catalyst = self.cat_option.get()
            alcohol = self.alc_option.get()
            alc_ml, cat_g = calculate_requirements(oil_ml, oil_type, catalyst, alcohol)
            self.result_label.configure(
                text=f"Alcohol: {alc_ml} ml\nCatalyst: {cat_g} g"
            )
        except Exception:
            messagebox.showerror("Error", "Enter a valid number for oil amount.")

if __name__ == "__main__":
    app = BiodieselApp()
    app.mainloop()