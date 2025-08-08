import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())

        # Convert height in feet and inches to meters
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())

        total_inches = (feet * 12) + inches
        height_m = total_inches * 0.0254  # 1 inch = 0.0254 meters

        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        # Display result
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obese"

        result_label.config(text=f"BMI: {bmi} ({status})")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def reset_fields():
    weight_entry.delete(0, tk.END)
    feet_entry.delete(0, tk.END)
    inches_entry.delete(0, tk.END)
    result_label.config(text="")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("350x300")
window.resizable(False, False)

# Weight input
tk.Label(window, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Height input (Feet and Inches)
tk.Label(window, text="Height (feet):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
feet_entry = tk.Entry(window)
feet_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Height (inches):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
inches_entry = tk.Entry(window)
inches_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons
tk.Button(window, text="Calculate BMI", command=calculate_bmi).grid(row=3, column=0, padx=10, pady=20)
tk.Button(window, text="Reset", command=reset_fields).grid(row=3, column=1, padx=10, pady=20)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the app
window.mainloop()
