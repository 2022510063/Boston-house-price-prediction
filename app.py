from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        features = [float(x) for x in request.form.values()]

        # Predict using the model
        prediction = model.predict([features])

        # Fix: Convert numpy array to scalar float using .item()
        predicted_price = prediction[0].item()

        # Show prediction in index.html
        return render_template('index.html',
                               prediction_text=f'Predicted House Price: ${predicted_price:,.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {e}')

if __name__ == '__main__':
    app.run(debug=True)
