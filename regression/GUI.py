import joblib
import tkinter as tk
from tkinter import ttk
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from tkinter.messagebox import showinfo

df = pd.read_csv('diamonds.csv')

loaded_model = joblib.load('model.joblib')
model = loaded_model

enc = OneHotEncoder(handle_unknown='ignore')


def pdf1():
    root.quit()


def pdf():
    if (cut.get() == "Fair"):
        a = 0
    elif (cut.get() == "Good"):
        a = 1
    elif (cut.get() == "Ideal"):
        a = 2
    elif (cut.get() == "Premium"):
        a = 3
    elif (cut.get() == "Very Good"):
        a = 4


    if (color.get() == "D"):
        b = 0
    elif (color.get() == "E"):
        b = 1
    elif (color.get() == "F"):
        b = 2
    elif (color.get() == "G"):
        b = 3
    elif (color.get() == "H"):
        b = 4
    elif (color.get() == "I"):
        b = 5
    elif (color.get() == "J"):
        b = 6


    if (clarity.get() == "I1"):
        c = 0
    elif (clarity.get() == "IF"):
        c = 1
    elif (clarity.get() == "SI1"):
        c = 2
    elif (clarity.get() == "SI2"):
        c = 3
    elif (clarity.get() == "VS1"):
        c = 4
    elif (clarity.get() == "VS2"):
        c = 5
    elif (clarity.get() == "VVS1"):
        c = 6
    elif (clarity.get() == "VVS2"):
        c = 7

    x_pred = [[age.get(), a, b, c,  hour.get(), hour1.get(), hour2.get()]]
    print(x_pred)


    tp = model.predict(x_pred)
    tp1 = np.round(tp)
    showinfo(title='Result', message=tp1)


root = tk.Tk()
root.title('Regression Decision Tree')

root.geometry('400x500')

# age
age = tk.StringVar()  # --variable

age_label = ttk.Label(root, text="carat:")
age_label.pack(fill='x', padx=10, pady=0, expand=True)

age_entry = ttk.Entry(root, textvariable=age)
age_entry.pack(fill='x', padx=10, pady=0, expand=True)
age_entry.focus()

# workclass
cut = tk.StringVar()  # --variable

cut_label = ttk.Label(root, text="cut:")
cut_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_cut = list(set(df['cut']))

cut_cb = ttk.Combobox(root, textvariable=cut)
cut_cb['values'] = datalist_cut
cut_cb['state'] = 'readonly'
cut_cb.pack(fill='x', padx=10, pady=5)

# education
color = tk.StringVar()  # --variable

color_label = ttk.Label(root, text="color:")
color_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_color = list(set(df['color']))

color_cb = ttk.Combobox(root, textvariable=color)
color_cb['values'] = datalist_color
color_cb['state'] = 'readonly'
color_cb.pack(fill='x', padx=10, pady=5)


# education
clarity = tk.StringVar()  # --variable

clarity_label = ttk.Label(root, text="clarity:")
clarity_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_clarity = list(set(df['clarity']))

clarity_cb = ttk.Combobox(root, textvariable=clarity)
clarity_cb['values'] = datalist_clarity
clarity_cb['state'] = 'readonly'
clarity_cb.pack(fill='x', padx=10, pady=5)


# age
hour = tk.StringVar()  # --variable

hour_label = ttk.Label(root, text="Chiều dài: ( x > 0)")
hour_label.pack(fill='x', padx=10, pady=0, expand=True)

hour_entry = ttk.Entry(root, textvariable=hour)
hour_entry.pack(fill='x', padx=10, pady=0, expand=True)
hour_entry.focus()

# age
hour1 = tk.StringVar()  # --variable

hour_label1 = ttk.Label(root, text="Chiều rộng: (y > 0)")
hour_label1.pack(fill='x', padx=10, pady=0, expand=True)

hour_entry1 = ttk.Entry(root, textvariable=hour1)
hour_entry1.pack(fill='x', padx=10, pady=0, expand=True)
hour_entry1.focus()

# age
hour2 = tk.StringVar()  # --variable

hour_label2 = ttk.Label(root, text="Chiều cao: (z > 0)")
hour_label2.pack(fill='x', padx=10, pady=0, expand=True)

hour_entry2 = ttk.Entry(root, textvariable=hour2)
hour_entry2.pack(fill='x', padx=10, pady=0, expand=True)
hour_entry2.focus()

# pred button
pred_button = ttk.Button(root, text="Predict", command=pdf)
pred_button.pack(fill='x', expand=True, padx=10, pady=10)

root.mainloop()
