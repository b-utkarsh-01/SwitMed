from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model using joblib
model = joblib.load(r'./model/city_pridiction.joblib')  # Correct the path as per your setup

# Read the dataset for price lookup
df = pd.read_csv(r'dataset/work_1.csv')  # Adjust this path

# Route to display the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the form submission and display city and location
@app.route('/get_city_location', methods=['POST'])
def get_city_location():
    # Get the form inputs
    medicine_name = request.form['medicine_name']
    location = request.form['location']
    
    # Clean the medicine name input by making it lowercase for comparison
    medicine_name = medicine_name.lower()

    # Create a new DataFrame with the medicine name and other required data for prediction
    new_data = pd.DataFrame({'Medicine Name': [medicine_name], 'Stock Quantity': [10]})  # Adjust other features if necessary

    # Make the prediction
    predicted_location = model.predict(new_data)
    
    # Lookup the price from the dataset
    def get_price(medicine_name):
        # Search for the medicine by name and get its price
        result = df[df['Medicine Name'].str.contains(medicine_name, case=False, na=False)]
        if not result.empty:
            return result.iloc[0]['Price']
        else:
            return "Medicine not found"
    
    price = get_price(medicine_name)
    
    # Function to get the usage of the medicine
    def get_medicine_usage(medicine_name):
        # Filter the dataframe for the given medicine name
        medicine_data = df[df['Medicine Name'].str.contains(medicine_name, case=False, na=False)]
        
        if not medicine_data.empty:
            # Extract the usage column (you might need to adjust the column name depending on your dataset)
            usage = medicine_data['Uses'].iloc[0]  # Assuming the column name is 'Usage'
            return usage
        else:
            return "Medicine not found"
    
    usage = get_medicine_usage(medicine_name)
    
    # Compare predicted location with the input location and determine the time status
    if predicted_location[0] == location:
        time_status = "under 1 hour"
    else:
        time_status = "more than a day"
    
    # Return the template with the prediction, price, time status, and usage
    return render_template('index.html', medicine_name=medicine_name, location=location, 
                           predicted_location=predicted_location[0], price=price, 
                           time_status=time_status, usage=usage)

if __name__ == '__main__':
    app.run(debug=True)
