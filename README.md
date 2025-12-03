# Dynamic Pricing Recommendation Tool

A Streamlit web application that predicts whether a product’s price should **Increase**, **Decrease**, or **Hold** using a trained machine-learning model. Users input Walmart-style features such as store, department, markdown levels, economic indicators, and seasonal data. The model then returns a data-driven pricing recommendation.

---

## Features

- **User Input Form:** Store, department, markdown1–markdown5, CPI, unemployment, fuel price, temperature, holiday flag, and time features.
- **Machine Learning Model:** Random Forest classifier trained on Walmart-style weekly sales data.
- **Real-Time Predictions:** Outputs an Increase / Decrease / Hold recommendation with contextual reasoning.
- **Streamlit Interface:** Clean, simple layout for fast and intuitive interactions.

---

## Tech Stack

- **Python**
- **Streamlit**
- **NumPy / Pandas**
- **scikit-learn**
- **Pickle** (model serialization)

---

## How It Works

1. A machine-learning model is trained in Jupyter using Walmart-style weekly sales data.
2. The trained model is exported as `model.pkl`.
3. Streamlit loads the model and accepts user inputs.
4. A pricing recommendation is generated in real time based on the input features.

---

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py
