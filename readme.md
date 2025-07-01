# 🚀 SwiftMeds - Smart Medicine Delivery Prediction App

SwiftMeds is a smart web application that predicts the most suitable delivery city/location for a given medicine. It also shows the estimated delivery time, price, and usage of the medicine using a trained machine learning model and a real dataset.

---

## 📦 Features

- ✅ Predict delivery location using ML
- 💰 Get the price of the medicine
- 📖 See medicine usage
- 🕒 Estimate delivery time: *under 1 hour* or *more than a day*
- 🌐 Clean, responsive web UI using HTML + CSS (optionally Tailwind)

---

## 📁 Folder Structure

SwiftMeds/
├── app.py # Main Flask application
├── model/
│ └── city_pridiction.joblib # Trained ML model
├── dataset/
│ └── work_1.csv # Medicine data (name, price, uses)
├── templates/
│ └── index.html # HTML template for the frontend
├── static/
│ └── style.css # Optional custom CSS styles

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/swiftmeds.git
cd swiftmeds
