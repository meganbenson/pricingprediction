from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

with open("final_rf_model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]          
    feature_columns = data["columns"] 



@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":


        store = 22   
        dept = int(request.form["dept"])
        markdown_total = float(request.form["markdown_total"])
        isholiday = int(request.form["isholiday"])
        temperature = float(request.form["temperature"])
        fuel = float(request.form["fuel"])
        cpi = float(request.form["cpi"])
        unemployment = float(request.form["unemployment"])
        size = int(request.form["size"])
        store_type = request.form["store_type"]  
        year = int(request.form["year"])
        month = int(request.form["month"])
        week = int(request.form["week"])

        df_new = pd.DataFrame({
            "Store": [store],
            "Dept": [dept],
            "markdown_total": [markdown_total],
            "IsHoliday": [isholiday],
            "Temperature": [temperature],
            "Fuel_Price": [fuel],
            "CPI": [cpi],
            "Unemployment": [unemployment],
            "Size": [size],
            "Type": [store_type],     
            "Year": [year],
            "Month": [month],
            "Week": [week]
        })

        df_new = pd.get_dummies(df_new, columns=["Type"], drop_first=True)

        for col in feature_columns:
            if col not in df_new.columns:
                df_new[col] = 0

        df_new = df_new[feature_columns]

        prediction = model.predict(df_new)[0]

    return render_template("index.html", prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True)
