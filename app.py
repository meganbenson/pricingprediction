from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# ---------------------------------------
# LOAD MODEL + METADATA
# ---------------------------------------
model_path = os.path.abspath("final_rf_model.pkl")
print("Loading model from:", model_path)

data = joblib.load(model_path)
model = data["model"]
feature_columns = data["columns"]   # exact training columns


# ---------------------------------------
# ROUTES
# ---------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":

        # ---- Extract inputs from form ----
        store = 22  # fixed
        dept = int(request.form["dept"])
        markdown_total = float(request.form["markdown_total"])
        isholiday = int(request.form["isholiday"])
        temperature = float(request.form["temperature"])
        fuel = float(request.form["fuel"])
        cpi = float(request.form["cpi"])
        unemployment = float(request.form["unemployment"])
        size = int(request.form["size"])
        store_type = request.form["store_type"]  # A, B, or C
        year = int(request.form["year"])
        month = int(request.form["month"])
        week = int(request.form["week"])

        # ---- Convert store_type into the dummy columns the model expects ----
        type_B = 1 if store_type == "B" else 0
        type_C = 1 if store_type == "C" else 0

        # ---- Build the dataframe with only the correct columns ----
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
            "Year": [year],
            "Month": [month],
            "Week": [week],
            "Type_B": [type_B],
            "Type_C": [type_C],
        })

        # ---- Ensure ALL expected model columns exist ----
        for col in feature_columns:
            if col not in df_new.columns:
                df_new[col] = 0

        # ---- Reorder columns to training order ----
        df_new = df_new[feature_columns]

        # ---- Predict ----
        prediction = model.predict(df_new)[0]


    return render_template("index.html", prediction=prediction)


# ---------------------------------------
# RUN APP
# ---------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
