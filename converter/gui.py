import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
from converter import (
    LengthConverter, 
    TemperatureConverter, 
    TimeConverter, 
    SpeedConverter, 
    VolumeConverter
)

class UnitConverterApp:
    def __init__(self, root):
        self.style = Style(theme='flatly')
        self.root = root
        self.root.title("Unit Converter")
        self.create_widgets()

    def create_widgets(self):
        # Unit selection
        self.from_unit = ttk.Combobox(self.root, values=["Meters", "Kilometers", "Celsius", "Fahrenheit", 
                                                          "Seconds", "Minutes", "Kmph", "Mps", 
                                                          "Liters", "Milliliters"])
        self.from_unit.grid(column=0, row=0, padx=10, pady=10)
        self.from_unit.set("Select From Unit")

        self.to_unit = ttk.Combobox(self.root, values=["Meters", "Kilometers", "Celsius", "Fahrenheit", 
                                                        "Seconds", "Minutes", "Kmph", "Mps", 
                                                        "Liters", "Milliliters"])
        self.to_unit.grid(column=1, row=0, padx=10, pady=10)
        self.to_unit.set("Select To Unit")

        self.value_entry = ttk.Entry(self.root)
        self.value_entry.grid(column=0, row=1, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=3, padx=10, pady=10)

        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.grid(column=0, row=2, padx=10, pady=10)

        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.grid(column=1, row=2, padx=10, pady=10)

        # Adding tooltips
        self.create_tooltips()

    def create_tooltips(self):
        tooltip_texts = {
            self.from_unit: "Select the unit to convert from",
            self.to_unit: "Select the unit to convert to",
            self.value_entry: "Enter the value to convert",
            self.convert_button: "Click to perform conversion",
            self.reset_button: "Click to reset the inputs"
        }
        for widget, text in tooltip_texts.items():
            widget.bind("<Enter>", lambda e, t=text: self.show_tooltip(e, t))
            widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event, text):
        x = event.x_root + 10
        y = event.y_root + 10
        self.tooltip = tk.Toplevel(self.root)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = ttk.Label(self.tooltip, text=text, background="lightyellow")
        label.pack()

    def hide_tooltip(self, event):
        if hasattr(self, 'tooltip'):
            self.tooltip.destroy()

    def convert(self):
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            # Conversion logic
            if from_unit == "Meters" and to_unit == "Kilometers":
                result = LengthConverter.meters_to_kilometers(value)
            elif from_unit == "Kilometers" and to_unit == "Meters":
                result = LengthConverter.kilometers_to_meters(value)
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = TemperatureConverter.celsius_to_fahrenheit(value)
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = TemperatureConverter.fahrenheit_to_celsius(value)
            elif from_unit == "Seconds" and to_unit == "Minutes":
                result = TimeConverter.seconds_to_minutes(value)
            elif from_unit == "Minutes" and to_unit == "Seconds":
                result = TimeConverter.minutes_to_seconds(value)
            elif from_unit == "Kmph" and to_unit == "Mps":
                result = SpeedConverter.kilometers_per_hour_to_meters_per_second(value)
            elif from_unit == "Mps" and to_unit == "Kmph":
                result = SpeedConverter.meters_per_second_to_kilometers_per_hour(value)
            elif from_unit == "Liters" and to_unit == "Milliliters":
                result = VolumeConverter.liters_to_milliliters(value)
            elif from_unit == "Milliliters" and to_unit == "Liters":
                result = VolumeConverter.milliliters_to_liters(value)
            else:
                raise ValueError("Invalid conversion selected.")

            self.result_label.config(text=f"Result: {result:.2f}")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for conversion.")

    def reset(self):
        self.from_unit.set("Select From Unit")
        self.to_unit.set("Select To Unit")
        self.value_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
