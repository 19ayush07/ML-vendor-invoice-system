# 📦 Vendor Invoice Intelligence Portal

An AI-powered analytics system for predicting freight costs and detecting risky vendor invoices using Machine Learning.

---

# 🚀 Project Overview

The Vendor Invoice Intelligence Portal helps finance and procurement teams:

- Predict freight costs accurately
- Detect abnormal or risky invoices
- Reduce manual approval workload
- Improve operational efficiency
- Support vendor negotiation and budgeting

The system combines:
- Regression models for freight cost prediction
- Classification models for invoice risk flagging
- Interactive Streamlit dashboard for real-time predictions

---

# 🧠 Machine Learning Objectives

## 1. Freight Cost Prediction
Predict expected freight cost using invoice-related features such as:
- Quantity
- Invoice Dollars

### Model Type
Regression

### Goal
Improve:
- Budget forecasting
- Freight estimation
- Cost optimization

---

## 2. Invoice Risk Flag Prediction
Predict whether an invoice should be flagged for manual approval.

### Model Type
Classification

### Goal
Detect:
- Abnormal invoice values
- Freight inconsistencies
- Delayed receiving patterns

---

# 📂 Project Structure

```text
Vendor_Invoice_Intelligence/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── inventory.db
│
├── model/
│   ├── freight_model.pkl
│   ├── invoice_flag_model.pkl
│   └── scaler.pkl
│
├── training/
│   ├── data_loader.py
│   ├── train_freight_model.py
│   └── train_invoice_model.py
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
└── notebooks/
    └── analysis.ipynb
```

---

# 📊 Dataset Features

## Freight Prediction Features
- Quantity
- Dollars

## Invoice Risk Features
- invoice_quantity
- invoice_dollars
- Freight
- total_item_quantity
- total_item_dollars
- avg_receiving_delay

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SQLite
- Streamlit
- Joblib

---

# 🛠️ Model Training

## Freight Cost Prediction
Model Used:
- Random Forest Regressor

Evaluation Metrics:
- MAE
- RMSE
- R² Score

---

## Invoice Risk Prediction
Model Used:
- Random Forest Classifier

Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1 Score

---

# 📈 Feature Engineering

The project generates advanced business intelligence features such as:

- Freight Per Unit
- Days to Pay
- Days PO to Invoice
- Average Receiving Delay
- Total Item Dollars
- Total Brands per Purchase Order

---

# 💻 Streamlit Dashboard

The dashboard allows users to:

✅ Predict freight cost  
✅ Predict invoice risk  
✅ Interact with ML models in real time  
✅ Support operational decision making

---

# ▶️ How to Run the Project

## 1. Clone Repository

```bash
git clone <your_repo_link>
cd Vendor_Invoice_Intelligence
```

---

## 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 3. Run Streamlit App

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
joblib
```

---


## 🚀 Live Demo

👉 https://vendor-invoice-portal.streamlit.app


# 📌 Future Improvements

- XGBoost implementation
- Fraud anomaly detection
- Vendor performance analytics
- Interactive business dashboards
- Cloud deployment integration

---

# 👨‍💻 Author

Developed as an end-to-end Machine Learning project for intelligent invoice analytics and freight cost optimization.
