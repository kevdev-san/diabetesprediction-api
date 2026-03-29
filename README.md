# diabetesprediction-api
#  Diabetes Prediction API

API desarrollada con **FastAPI** que utiliza un modelo de Machine Learning para predecir la probabilidad de diabetes a partir de datos clínicos del paciente.


##  Tecnologías utilizadas

* FastAPI
* Scikit-learn
* XGBoost
* Joblib
* Python

---

##  Modelo de Machine Learning

El modelo es un **ensamble (VotingClassifier)** compuesto por:

* Logistic Regression
* Support Vector Machine (SVM)
* XGBoost

Se entrena utilizando las siguientes características:

* `age`
* `hypertension`
* `heart_disease`
* `bmi`
* `HbA1c_level`

El modelo está encapsulado dentro de un **Pipeline** que incluye escalado de datos.

---

## 📁 Estructura del proyecto

```
backend/
├── main.py
├── models/
│   └── modelo_pipeline.pkl
├── routers/
│   └── predict.py
├── services/
│   └── model_service.py
└── schemas/
    └── schemas.py
```

---

## ⚙️ Instalación

1. Clonar el repositorio:

```
git clone https://github.com/kevdev-san/diabetesprediction-api.git
cd diabetesprediction-api
```

2. Crear entorno virtual:

```
python -m venv .venv
```

3. Activar entorno:

* Windows:

```
.venv\Scripts\activate
```

4. Instalar dependencias:

```
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la API

```
uvicorn main:app --reload
```

Acceder a la documentación automática:

👉 http://127.0.0.1:8000/docs

---

##  Endpoint

### POST `/api/predict`

#### 🔹 Request

```json
{
  "age": 50,
  "hypertension": 1,
  "heart_disease": 0,
  "bmi": 32,
  "HbA1c_level": 7.0
}
```

#### 🔹 Response

```json
{
  "prediction": 1,
  "label": "diabetes",
  "probability_percent": 82.7
}
```

---

## 📌 Interpretación

* `prediction`:

  * `0` → No diabetes
  * `1` → Diabetes

* `probability_percent`:
  Probabilidad estimada de que el paciente tenga diabetes.

---

##  Ejemplos de prueba

### Bajo riesgo

```json
{
  "age": 25,
  "hypertension": 0,
  "heart_disease": 0,
  "bmi": 22.0,
  "HbA1c_level": 5.2
}
```

### Alto riesgo

```json
{
  "age": 60,
  "hypertension": 1,
  "heart_disease": 1,
  "bmi": 32.0,
  "HbA1c_level": 7.5
}
```



---

## 👨‍💻 Autores

KEVIN LEONARDO BAÑOS SÁNCHEZ, ITZEL ALEJANDRA LESAMA APOLINAR, NORMA INÉS LLERGO SÁNCHEZ
