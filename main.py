import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox
import joblib
import os

# Assuming LOCAL_MODEL_PATH and LOCAL_ENCODER_PATH are defined elsewhere, if not define them or use direct paths.
LOCAL_MODEL_PATH = 'model.joblib'  # Update this path if the model is in another directory
LOCAL_ENCODER_PATH = 'label_encoder.joblib'  # Update this path if the encoder is in another directory

# Load the trained model and label encoder
model = joblib.load(LOCAL_MODEL_PATH)
label_encoder = joblib.load(LOCAL_ENCODER_PATH)

# Example product data (normally this would be loaded from a database or a file)
all_products = pd.DataFrame({
    'Dinex Product': ['ProductA', 'ProductB'],  # Example data
    'Dinex Number': [123, 456]
})

def predict(zipcode):
    try:
        products = all_products[['Dinex Product', 'Dinex Number']].drop_duplicates()
        products['Zipcode'] = zipcode
        products['Dinex Product Encoded'] = label_encoder.transform(products['Dinex Product'])

        predicted_fleet_sizes = model.predict(products[['Zipcode', 'Dinex Product Encoded']])
        products['2024 Compatible VIOs'] = np.ceil(predicted_fleet_sizes)
        top_products = products.sort_values(by='2024 Compatible VIOs', ascending=False).head(10)
        return top_products.to_string(index=False)
    except Exception as e:
        return str(e)

# GUI Setup
root = tk.Tk()
root.title("Dinex Product Predictor")

def on_predict():
    zipcode = simpledialog.askstring("Input", "Enter the Zipcode:", parent=root)
    if zipcode:
        result = predict(zipcode)
        messagebox.showinfo("Prediction Result", result)

predict_button = tk.Button(root, text="Predict Fleet Sizes", command=on_predict)
predict_button.pack(pady=20)

root.mainloop()
