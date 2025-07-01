from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and dataset
model = joblib.load(os.path.join(BASE_DIR, 'model', 'city_pridiction.joblib'))
df = pd.read_csv(os.path.join(BASE_DIR, 'dataset', 'work_1.csv'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_city_location', methods=['POST'])
def get_city_location():
    medicine_name = request.form['medicine_name'].lower()
    location = request.form['location']

    # Data for prediction (make sure this matches model training structure)
    new_data = pd.DataFrame({'Medicine Name': [medicine_name], 'Stock Quantity': [10]})

    # Predict city/location
    try:
        predicted_location = model.predict(new_data)
    except Exception as e:
        return render_template('index.html', error=f"Prediction failed: {e}")

    # Get price
    price = get_price(medicine_name)

    # Get usage
    usage = get_medicine_usage(medicine_name)

    # Estimate delivery time
    if predicted_location[0].lower() == location.lower():
        time_status = "under 1 hour"
    else:
        time_status = "more than a day"

    return render_template('index.html',
                           medicine_name=medicine_name,
                           location=location,
                           predicted_location=predicted_location[0],
                           price=price,
                           usage=usage,
                           time_status=time_status)

def get_price(medicine_name):
    result = df[df['Medicine Name'].str.contains(medicine_name, case=False, na=False)]
    return result.iloc[0]['Price'] if not result.empty else "Medicine not found"

def get_medicine_usage(medicine_name):
    result = df[df['Medicine Name'].str.contains(medicine_name, case=False, na=False)]
    return result.iloc[0]['Uses'] if not result.empty and 'Uses' in result.columns else "Usage info not available"

if __name__ == '__main__':
    app.run(debug=True)