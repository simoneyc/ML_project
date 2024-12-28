import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

try:
    model = joblib.load('random_forest_model.pkl') 
except FileNotFoundError as e:
    print(f"模型文件未找到：{e}")
    exit()

dropdown_options = {
    "Salary": [],  # 自由輸入
    "Job Satisfaction": [i for i in range(1, 11)],
    "Work-Life Balance": [i for i in range(1, 11)],
    "Job Security": [i for i in range(1, 11)],
    "Industry Growth Rate": ["High", "Medium", "Low"],
}

growth_rate_mapping = {
    "High": 0,
    "Medium": 2,
    "Low": 1
}

def predict():
    try:
        input_data = []
        for i, (feature, values) in enumerate(dropdown_options.items()):
            if feature == "Salary":  # Salary 自由輸入
                value = entries[i].get()
                if not value or not value.replace('.', '', 1).isdigit():
                    raise ValueError(f"{feature} 必須是一個數值啦^^")
                value = float(value)
            elif feature == "Industry Growth Rate":

                value = growth_rate_mapping[entries[i].get()]
            else:
                value = entries[i].get()
            input_data.append(value)

        input_data_np = np.array([input_data])

        prediction = model.predict(input_data_np)
        prediction_proba = model.predict_proba(input_data_np)[:, 1]

        if prediction[0] == 0:
            result = "不會離職"
        else:
            result = "會離職"
        result_text = f"Prediction: {result}\n"
        if prediction[0] == 0:
            prediction_proba[0] = 1 - prediction_proba[0]
            result_text += f"不會離職的機率: {prediction_proba[0]:.2f}"
        else:
            result_text += f"會離職的機率: {prediction_proba[0]:.2f}"


        popup = ttk.Frame(root, padding=(20, 10), relief="solid", borderwidth=1, style="TFrame")
        popup.place(x=200, y=150, width=300, height=150)

        label = ttk.Label(popup, text=result_text, padding=(20, 10))
        label.pack(expand=True, fill=BOTH)

        button_frame = ttk.Frame(popup, padding=(10, 5))
        button_frame.pack(expand=False, fill=X)

        ok_button = ttk.Button(button_frame, text="OK", command=popup.destroy, bootstyle=SUCCESS)
        ok_button.pack(side=RIGHT, padx=5)

        root.update_idletasks()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or error occurred: {e}")


root = ttk.Window(themename="superhero")
root.title("Career Change Prediction")
root.geometry("1000x400")

container = ttk.Frame(root)
container.place(relx=0.5, rely=0.5, anchor="center")

entries = []
row, col = 0, 0
for i, (feature, values) in enumerate(dropdown_options.items()):
    if col == 0:
        frame = ttk.Frame(container, padding=(10, 5))
        frame.grid(row=row, column=0, columnspan=3, sticky=W)

    label = ttk.Label(frame, text=feature, width=20, anchor="e")
    label.pack(side=LEFT, padx=5)

    if feature == "Salary":  # Salary 自由輸入
        entry = ttk.Entry(frame, width=10)
        entry.insert(0, "Enter $$")
    else:
        entry = ttk.Combobox(frame, values=values, state="readonly", width=8)
        if values:
            entry.set(values[0])
    
    entry.pack(side=LEFT, padx=5)
    entries.append(entry)

    col += 1
    if col == 3: 
        col = 0
        row += 1

predict_button = ttk.Button(container, text="Predict", command=predict, bootstyle=SUCCESS, width=10)
predict_button.grid(row=row + 1, column=0, columnspan=3, pady=20, sticky="n", padx=5)

root.mainloop()