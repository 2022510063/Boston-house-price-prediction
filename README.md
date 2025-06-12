# 🏡 Boston House Price Prediction using Flask

This project is a machine learning web application that predicts Boston house prices based on input features. It uses a **Linear Regression model** trained on the Boston Housing dataset and is deployed using **Flask**.

![screenshot](https://user-images.githubusercontent.com/placeholder/demo-preview.png)

---

## 🚀 Features

- Built with Python, Flask, and scikit-learn
- Linear Regression trained on 13 features
- HTML/CSS front-end for user-friendly prediction form
- Deployed on Render

---

## 🧠 Boston Dataset Features

| Feature     | Description                               |
|-------------|-------------------------------------------|
| CRIM        | Per capita crime rate by town             |
| ZN          | Proportion of residential land zoned      |
| INDUS       | Non-retail business acres per town        |
| CHAS        | Charles River dummy variable              |
| NOX         | Nitric oxide concentration                |
| RM          | Avg. number of rooms per dwelling         |
| AGE         | Proportion of old owner-occupied units    |
| DIS         | Distance to employment centers            |
| RAD         | Accessibility to radial highways          |
| TAX         | Property tax rate                         |
| PTRATIO     | Pupil–teacher ratio                       |
| B           | Black population index                    |
| LSTAT       | % of lower status population              |

---

## 🛠 Tech Stack

- Python 3
- Flask
- scikit-learn
- pandas
- numpy
- HTML5 + CSS3 (Bootstrap optional)
- Render (cloud hosting)

---

## 📦 Installation Instructions (Local)

```bash
# 1. Clone the repo
git clone https://github.com/2022510063/Boston-house-price-prediction.git
cd Boston-house-price-prediction

# 2. Create a virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # for Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
