import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    'age': 45,
    'hypertension': 0,
    'heart_disease': 0,
    'avg_glucose_level': 85.6,
    'bmi': 26.5,
    'gender_Male': 1,
    'ever_married_Yes': 1,
    'work_type_Private': 1,
    'work_type_Self-employed': 0,
    'work_type_children': 0,
    'Residence_type_Urban': 1,
    'smoking_status_formerly smoked': 0,
    'smoking_status_never smoked': 1,
    'smoking_status_smokes': 0
}

response = requests.post(url, json=data)
print(response.json())
