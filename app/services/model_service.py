import joblib

# Cargar modelo UNA sola vez
model = joblib.load("app/model/modelo_pipeline.pkl")


def predict_diabetes(data):
    X = [[
        data.age,
        data.hypertension,
        data.heart_disease,
        data.bmi,
        data.HbA1c_level
    ]]

    pred = model.predict(X)
    proba = model.predict_proba(X)

    prediction = int(pred[0])
    probability = float(proba[0][1])

    return {
        "prediction": prediction,
        "label": "diabetes" if prediction == 1 else "no diabetes",
        "probability": round(probability * 100, 2)
    }