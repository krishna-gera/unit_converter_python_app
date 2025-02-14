import tkinter as tk
from tkinter import ttk, messagebox

# Conversion factors for length
length_factors = {
    'meters': {'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084, 'meters': 1},
    'kilometers': {'meters': 1000, 'miles': 0.621371, 'feet': 3280.84, 'kilometers': 1},
    'miles': {'meters': 1609.34, 'kilometers': 1.60934, 'feet': 5280, 'miles': 1},
    'feet': {'meters': 0.3048, 'kilometers': 0.0003048, 'miles': 0.000189394, 'feet': 1}
}

# Conversion factors for volume
volume_factors = {
    'liters': {'milliliters': 1000, 'cubic_meters': 0.001, 'gallons': 0.264172, 'liters': 1},
    'milliliters': {'liters': 0.001, 'cubic_meters': 1e-6, 'gallons': 0.000264172, 'milliliters': 1},
    'cubic_meters': {'liters': 1000, 'milliliters': 1e6, 'gallons': 264.172, 'cubic_meters': 1},
    'gallons': {'liters': 3.78541, 'milliliters': 3785.41, 'cubic_meters': 0.00378541, 'gallons': 1}
}

# Conversion factors for mass
mass_factors = {
    'grams': {'kilograms': 0.001, 'pounds': 0.00220462, 'ounces': 0.035274, 'grams': 1},
    'kilograms': {'grams': 1000, 'pounds': 2.20462, 'ounces': 35.274, 'kilograms': 1},
    'pounds': {'grams': 453.592, 'kilograms': 0.453592, 'ounces': 16, 'pounds': 1},
    'ounces': {'grams': 28.3495, 'kilograms': 0.0283495, 'pounds': 0.0625, 'ounces': 1}
}

# Conversion functions for temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

# Main conversion function
def convert_units(value, from_unit, to_unit, unit_type):
    conversion_factors = {
        'length': length_factors,
        'volume': volume_factors,
        'mass': mass_factors
    }
    
    if unit_type == 'temperature':
        return convert_temperature(value, from_unit, to_unit)
    
    factors = conversion_factors.get(unit_type)
    if not factors:
        return None
    
    if from_unit in factors and to_unit in factors[from_unit]:
        conversion_factor = factors[from_unit][to_unit]
        return value * conversion_factor
    else:
        return None

def update_units(event):
    unit_type = combo_unit_type.get()
    if unit_type == 'length':
        units = list(length_factors.keys())
    elif unit_type == 'volume':
        units = list(volume_factors.keys())
    elif unit_type == 'mass':
        units = list(mass_factors.keys())
    elif unit_type == 'temperature':
        units = ['celsius', 'fahrenheit', 'kelvin']
    combo_from_unit['values'] = units
    combo_to_unit['values'] = units

def perform_conversion():
    try:
        value = float(entry_value.get())
        from_unit = combo_from_unit.get()
        to_unit = combo_to_unit.get()
        unit_type = combo_unit_type.get()

        converted_value = convert_units(value, from_unit, to_unit, unit_type)
        if converted_value is not None:
            result.set(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
        else:
            messagebox.showerror("Error", "Conversion not possible with the given units")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for the value to be converted.")

# GUI setup
root = tk.Tk()
root.title("Unit Converter")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Unit Type:").grid(row=0, column=0, sticky=tk.W)
combo_unit_type = ttk.Combobox(frame, values=['length', 'volume', 'mass', 'temperature'])
combo_unit_type.grid(row=0, column=1, sticky=(tk.W, tk.E))
combo_unit_type.bind('<<ComboboxSelected>>', update_units)

ttk.Label(frame, text="Value:").grid(row=1, column=0, sticky=tk.W)
entry_value = ttk.Entry(frame)
entry_value.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="From Unit:").grid(row=2, column=0, sticky=tk.W)
combo_from_unit = ttk.Combobox(frame)
combo_from_unit.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="To Unit:").grid(row=3, column=0, sticky=tk.W)
combo_to_unit = ttk.Combobox(frame)
combo_to_unit.grid(row=3, column=1, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Convert", command=perform_conversion).grid(row=4, column=0, columnspan=2)

result = tk.StringVar()
ttk.Label(frame, textvariable=result, font=('Arial', 14, 'bold')).grid(row=5, column=0, columnspan=2)

root.mainloop()
