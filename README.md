# Dynamic Pricing Recommendation Tool

This project is a web application built with Flask that uses machine learning to help users make informed pricing decisions. By analyzing retail and economic features, the tool predicts whether a product’s price should be increased, decreased, or kept the same. The goal is to provide clear, data-driven recommendations that users can apply directly.
The model is trained on historical sales data similar to what large retailers use. It takes into account markdown activity, economic indicators, time-related features, and store information to make accurate pricing suggestions. This approach helps users quickly understand what pricing action is recommended based on the data.

---

## Overview

Retail pricing decisions are complex and often influenced by discount patterns, seasonality, economic conditions, and product category behavior, directly impacting profitability and competitive advantage.  
The tool acts as a pricing assistant by allowing users to enter product and market information. It uses a trained Random Forest classifier to provide immediate price recommendations: increase, decrease, or hold. Each recommendation comes with an explanation, so users can understand the reasoning behind the suggestion. This helps make the decision process faster and more transparent.

---

## Features

### **User Input Form**
Users provide key retail and market features:
- Department  
- Markdown total  
- Holiday indicator  
- Temperature  
- Fuel price  
- CPI & unemployment rate  
- Store size  
- Store type (A, B, or C)  
- Time features (year, month, week)

The model uses a Random Forest classifier that has been tuned with GridSearchCV and improved through feature engineering. It considers markdown activities, time-based variables, and store information to give more realistic and detailed pricing guidance.

The tool gives users one of three possible actions: increase the price if demand is strong, decrease the price if the model predicts weaker performance, or hold the price if there is no clear signal. This helps users respond quickly and confidently to changing conditions.

The web application is built using Flask, HTML, and CSS. The interface is designed to be straightforward so users can quickly get predictions and see explanations for each recommendation. The app can be deployed easily using Git LFS.

---

## Tech Stack

**Languages:** Python, HTML, CSS  
**Libraries:** Pandas, NumPy, Scikit-Learn, Flask  
**Tools:** Git, GitHub, Jupyter Notebook, Git LFS  
**Modeling:** Random Forest, GridSearchCV, Feature Engineering  

---



