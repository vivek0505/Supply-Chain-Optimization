from flask import Flask, render_template, request 
import pandas as pd

app = Flask(__name__)

# Define a function to read predictions from CSV files for all medicines
def read_predictions(month, day):
    predictions = {}
    for drug_code in ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']:
        try:
            filename = f"/Users/csuftitan/Desktop/Forecast/{drug_code}_predictions.csv"
            predictions_df = pd.read_csv(filename)
            prediction = predictions_df[(predictions_df['Date'].str.split('-').str[1].astype(int) == month) &
                                       (predictions_df['Date'].str.split('-').str[2].astype(int) == day)]
            if not prediction.empty:
                predictions[drug_code] = prediction['Predicted_Sales'].values[0]
        except FileNotFoundError:
            predictions[drug_code] = f"Error: Prediction file for {drug_code} not found."
    return predictions

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    try:
        month = int(request.form['month'])
        day = int(request.form['day'])
    except (KeyError, ValueError):
        # Handle missing or invalid form data
        return "Error: Please provide valid month and day."

    # Read predictions for all medicines based on the selected month and day
    predictions = read_predictions(month, day)

    # Render the results template with all predictions
    return render_template('results.html', predictions=predictions)

# Assuming the provided index.html template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
