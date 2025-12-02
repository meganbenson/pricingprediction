Dynamic Pricing Recommendation Tool
This project is a web-based application that predicts whether a product’s price should Increase, Decrease, or Hold based on Walmart-style historical features. Users can enter product-level information—such as store, department, markdown levels, economic indicators, holidays, and seasonal data—and the model returns a recommended pricing action.
The tool demonstrates how machine-learning models can support dynamic pricing decisions by combining sales context, inventory conditions, and external economic factors.
Features
Input Form: Enter all relevant product attributes (store, department, markdown1–markdown5, CPI, unemployment, fuel price, temperature, holidays, and time features).
Machine Learning Model: A trained Random Forest classifier predicts one of three price actions: Increase, Decrease, or Hold.
Simple Web Interface: Built with Streamlit for fast deployment and clean presentation.
Real-time Recommendations: The model outputs both the action and an explanation.
Tech Stack
Python (model training, preprocessing)
scikit-learn (Random Forest classifier)
Streamlit (web UI)
NumPy / Pandas
Pickle (model storage)
How It Works
The ML model is trained on Walmart-style weekly sales data.
The model is saved as model.pkl.
Users enter feature values through a Streamlit interface.
The app loads the model and generates a pricing recommendation.
Running the App
pip install -r requirements.txt
streamlit run app.py
The app will launch in your browser at http://localhost:8501.
Project Goals
This project demonstrates how data-driven pricing strategies can replace static rules by reacting to real-world conditions such as demand shifts, inventory pressure, and economic change. It serves as an educational example of deploying a machine-learning model into a simple, user-friendly website.
