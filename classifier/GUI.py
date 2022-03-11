import joblib
import tkinter as tk
from tkinter import ttk
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from tkinter.messagebox import showinfo

df = pd.read_csv('titanic.csv')

loaded_model = joblib.load('model.joblib')
model = loaded_model

enc = OneHotEncoder(handle_unknown='ignore')


def pdf1():
    root.quit()


def pdf():
    if (Pclass.get() == "1"):
        a = 1
    elif (Pclass.get() == "2"):
        a = 2
    elif (Pclass.get() == "3"):
        a = 3


    if (Sex.get() == "female"):
        b = 0
    elif (Sex.get() == "male"):
        b = 1


    if (Embarked.get() == "C"):
        c = 0
    elif (Embarked.get() == "Q"):
        c = 1
    elif (Embarked.get() == "S"):
        c = 2
    elif (Embarked.get() == ""):
        c = 3

    x_pred = [[a, b, age.get(), hour.get(), hour1.get(), hour2.get(), c]]
    print(x_pred)


    tp = model.predict(x_pred)
    print(tp)

    if (tp == 1):
        msg = f' Survived '
    else:
        msg = f' Unsurvived '
    showinfo(title='Result', message=msg)


root = tk.Tk()
root.title('Regression Decision Tree')

root.geometry('400x500')


# workclass
Pclass = tk.StringVar()  # --variable

Pclass_label = ttk.Label(root, text="Passenger Class:")
Pclass_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_Pclass = list(set(df['Pclass']))

Pclass_cb = ttk.Combobox(root, textvariable=Pclass)
Pclass_cb['values'] = datalist_Pclass
Pclass_cb['state'] = 'readonly'
Pclass_cb.pack(fill='x', padx=10, pady=5)

# education
Sex = tk.StringVar()  # --variable

Sex_label = ttk.Label(root, text="Sex:")
Sex_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_Sex = list(set(df['Sex']))

Sex_cb = ttk.Combobox(root, textvariable=Sex)
Sex_cb['values'] = datalist_Sex
Sex_cb['state'] = 'readonly'
Sex_cb.pack(fill='x', padx=10, pady=5)

# age
age = tk.StringVar()  # --variable

age_label = ttk.Label(root, text="Age:")
age_label.pack(fill='x', padx=10, pady=0, expand=True)

age_entry = ttk.Entry(root, textvariable=age)
age_entry.pack(fill='x', padx=10, pady=0, expand=True)
age_entry.focus()


# age
hour = tk.StringVar()  # --variable

hour_label = ttk.Label(root, text="Siblings Aboard:")
hour_label.pack(fill='x', padx=10, pady=0, expand=True)

hour_entry = ttk.Entry(root, textvariable=hour)
hour_entry.pack(fill='x', padx=10, pady=0, expand=True)
hour_entry.focus()

# age
hour1 = tk.StringVar()  # --variable

hour_label1 = ttk.Label(root, text="Parents Aboard:")
hour_label1.pack(fill='x', padx=10, pady=0, expand=True)

hour_entry1 = ttk.Entry(root, textvariable=hour1)
hour_entry1.pack(fill='x', padx=10, pady=0, expand=True)
hour_entry1.focus()

# age
hour2 = tk.StringVar()  # --variable

hour_label2 = ttk.Label(root, text="Fare paid (£):")
hour_label2.pack(fill='x', padx=10, pady=0, expand=True)

hour_entry2 = ttk.Entry(root, textvariable=hour2)
hour_entry2.pack(fill='x', padx=10, pady=0, expand=True)
hour_entry2.focus()



# education
Embarked = tk.StringVar()  # --variable

Embarked_label = ttk.Label(root, text="Embarked:")
Embarked_label.pack(fill='x', padx=10, pady=0, expand=True)
datalist_Embarked = list(set(df['Embarked']))

Embarked_cb = ttk.Combobox(root, textvariable=Embarked)
Embarked_cb['values'] = datalist_Embarked
Embarked_cb['state'] = 'readonly'
Embarked_cb.pack(fill='x', padx=10, pady=5)


# pred button
pred_button = ttk.Button(root, text="Predict", command=pdf)
pred_button.pack(fill='x', expand=True, padx=10, pady=10)

root.mainloop()
